Adding new test target
----------------------

Necessary files
~~~~~~~~~~~~~~~

#. Wrapper file for litex
#. Makefile
#. Testbench
#. Descriptor config file

Naming scheme
~~~~~~~~~~~~~

Choose a unique name for your target. This will need to be passed to a Makefile variable during test runs.

Other files should be called as follows:

* /wrappers/generate_TARGET.py
* /wrappers/Makefile.TARGET
* /wrappers/tb_TARGET.v
* /configs/decriptors_TARGET.json


LiteX wrapper
~~~~~~~~~~~~~

We use LiteX to generate glue code in order to have a stable and readable interface to various IP cores. This is true whether the target is already written in LiteX or is available as Verilog/VHDL module.

Testing LiteX cores
^^^^^^^^^^^^^^^^^^^

Take a look at ValentyUSB target. This is an IP core written in LiteX.
The *generate_valentyusb.py* script generates a minimal wrapper, routing clocks and reset signals, and assigning the USB pins.


Testing non-LiteX cores
^^^^^^^^^^^^^^^^^^^^^^^

Cores writtel in other HDL languages can be instantiated in LiteX. Take a look at *generate_usb1device.py*. Apart from providing clocks and routing pads, you need the following lines:

.. code-block:: python

    platform.add_source("../usb1_device/rtl/verilog/usb1_core.v")

This will add the Verilog files for your device to be used by LiteX.

.. code-block:: python

    self.specials += Instance(
        "usb1_core",
        i_clk_i=self.crg.cd_sys.clk,
        i_rst_i=usb_reset,
        # USB lines
        o_tx_dp=usb_p_tx,
        o_tx_dn=usb_n_tx,
        i_rx_dp=usb_p_rx,
        i_rx_dn=usb_n_rx,
        o_tx_oe=usb_tx_en_dut,
        i_rx_d=usb_p_rx,
        i_phy_tx_mode=0b1)  # You can hardwire signal state
        # Not needed signals can be omitted

This block instantiates the IP core in LiteX design. First argument is module name, and the rest are its signals assigned to corresponding LiteX objects.

Note that module signals are prefixed with either **i\_** or **o\_** to denote their direction.

In the makefile you need to point to your module sources for the simulator:

.. code-block:: makefile

    VERILOG_SOURCES += $(WPWD)/../usb1_device/rtl/verilog/*.v


Testing targets with a software stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The wrapper can include a CPU that will execute whatever code you need in the simulation. We rely on LiteX to instantiate the module.
An example is available in *generate_foboot.py*, where we add a VexRiscV CPU and then run Foboot firmware (limited to the USB part in order not to simulate every peripheral on FOMU). Important part here is to include a ROM init file for LiteX, which will set the start address automatically in ``SoCCore`` class. CPU type is passed as parameter in the makefile:

.. code-block:: makefile

    TARGET_OPTIONS = --cpu-type vexriscv --variant epfifo --rom-init ../foboot/sw/foboot.bin
    VERILOG_SOURCES += $(WPWD)/../litex/litex/soc/cores/cpu/vexriscv/verilog/VexRiscv.v


Target-specific makefile
~~~~~~~~~~~~~~~~~~~~~~~~

Options and variables specific to the target are contained in a separate makefile. It is *included* by the main one, so any paths here should be relative to the *usb-test-suite* directory.


Testbench file
~~~~~~~~~~~~~~

A testbench is the top-level module for the simulator. It should provide common interface to the DUT to be used between tests. For Icarus Verilog the setting to dump simulation signals is also contained here.Device under test is instantiated as a module here.


.. _config-descriptors-json:

Descriptor config file
~~~~~~~~~~~~~~~~~~~~~~

Descriptor values expected from the device are stored in a JSON file. At a top level, it contains an array the parser will iterate over. Each descriptor is stored as a JSON object.


Device Descriptor
^^^^^^^^^^^^^^^^^

Fields in this descriptor follow the USB standard specification. Note that as JSON does not allow for hex values, they can be stored as strings or decimal values.


Configuration Descriptor
^^^^^^^^^^^^^^^^^^^^^^^^

Fields in this descriptor follow the USB standard specification. Last element is an array  of Interface Descriptors supported by this configuration.


Interface Descriptor
^^^^^^^^^^^^^^^^^^^^

Last element here is an array of subdescriptors. They can either be Endpoint Descriptors or class-specific ones.


Endpoint Descriptors
^^^^^^^^^^^^^^^^^^^^

Endpoint descriptor attributes and address can be given either as a byte value or spelled out as ``key : value`` pairs.

.. code-block:: json

          {
            "name":                "Endpoint",
            "bLength":                      7,
            "bDescriptorType":              5,
            "bEndpointAddress":     [2, "IN"],
            "bmAttributes": {
              "Transfer":              "Bulk",
              "Synch":                 "None",
              "Usage":                 "Data"
            },
            "wMaxPacketSize":        "0x0200",
            "bInterval":                    0
          }


String Descriptors
^^^^^^^^^^^^^^^^^^

String descriptors are a bit special in that the descriptor at index 0 should contain an array of supported language IDs. This descriptor should have the same content regardless of langId specified in the USB request. Then the rest of the string descriptors should be provided for each language that was declared as supported.

To cope with this difference in the JSON file at index 0 (what could be interpreted as unspecified langId just as well) there should be the said array of language IDs. Then, for each element in that array there should be a field in the JSON object, containing a set of paired indexes and strings that the device should report for this index.

Consider a following entry in the JSON file:

.. code-block:: json

  {
    "name":     "String",
    "bDescriptorType": 3,
    "0":      ["0x0409"],
    "0x0409" : {
      "1":     "Generic",
      "2":      "IpCore",
      "3":  "1234567890"
    }
  }

Here the device supports only one language ID (English), then reports three strings for that ID. If queried with following requests:

* ``langId 0x0000, idx 0`` - would respond with descriptor content ``0x0409``
* ``langId 0x0409, idx 0`` - would respond with descriptor content ``0x0409``
* ``langId 0x0409, idx 2`` - would respond with descriptor content ``IpCore``


Other Descriptors
^^^^^^^^^^^^^^^^^

Non-standard descriptors that are not stored as part of the configuration can be added to the descriptor array in config file. It is up to the parser to determine if they can be extracted and used in test.
