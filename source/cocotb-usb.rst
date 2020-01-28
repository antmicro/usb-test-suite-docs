cocotb_usb module
=================

Module providing functions to test USB IP cores using *cocotb*.

Setup
-----

*cocotb_usb* can be installed as part of the *usb-test-suite* (see :ref:`Setup section <setup>`) or on its own:

.. code-block:: bash

    pip install cocotb
    git clone https://github.com/antmicro/usb-test-suite-cocotb-usb
    pip install ./usb-test-suite-cocotb-usb/

Usage
-----

*cocotb_usb* was designed to use with `usb-test-suite-testbenches`_ repository. You can browse its `tests`_ directory for examples.

Quickstart
^^^^^^^^^^

.. code-block:: python

    from cocotb_usb.host import UsbTest
    from cocotb_usb.device import UsbDevice

    # Get a test harness that will act as host
    harness = UsbTest(your_dut_object)              # cocotb will pass dut for each test case

    # Store expected responses in an object
    model = UsbDevice("path/to/your/config.json")

    harness.reset()                                 # Reset DUT
    yield harness.connect()                         # Simulate USB connect

    # Now you can interface with the device using high-level functions

    yield harness.port_reset()                      # Reset USB device to known state

    expected = model.deviceDescriptor.get()         # Get descriptor as list of bytes
    yield harness.get_device_descriptor(response=expected)

    yield harness.set_device_address(20)


.. _usb-test-suite-testbenches: https://github.com/antmicro/usb-test-suite-testbenches
.. _tests: https://github.com/antmicro/usb-test-suite-testbenches/tree/master/tests
