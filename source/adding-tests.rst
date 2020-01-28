Adding new tests
----------------

Each new test needs to follow all usual guidelines specified for cocotb. Basically this means each test function should be decorated with ``cocotb.test()``, they then get the device passed as the first parameter (named ``dut`` in existing test cases) and you should use ``yield`` keyword whenever you want to transfer control to the simulator. See `cocotb documentation <https://cocotb.readthedocs.io/en/latest/>`_ for details.


Obtaining test harness
~~~~~~~~~~~~~~~~~~~~~~

The device under test as seen by cocotb is the Verilog testbench file. To imitate USB host we attach to it one of the classes defined in ``cocotb_usb.*_host``.

In order for the tests to be applicable to multiple devices, the host class is determined dynamically using ``TARGET`` variable from Makefile. At the beginning of the test script, use:

.. code-block:: python

    from cocotb_usb.harness import get_harness

Then in the test function pass the ``dut`` parameter to obtain correct harness:

.. code-block:: python

    harness = get_harness(dut)


Resetting the device
~~~~~~~~~~~~~~~~~~~~

The test harness provides methods for both device reset and USB bus reset. At the beginning of the test, use

.. code-block:: python

    yield harness.reset()

to bring the device to a known state. Note that you have to use the ``yield`` keyword.

To issue a USB bus reset, use:

.. code-block:: python

    yield harness.port_reset()

Optionally you can provide reset duration as an argument.
Remember that bus reset time mentioned in the USB specification is 10-20 ms, though most cores will work with much shorter periods.


Providing clock signals
~~~~~~~~~~~~~~~~~~~~~~~

By default harness shares its 48 MHz clock with the DUT. If you want to provide your own clock signal, set optional argument ``decouple_clocks`` to ``True`` and drive the input in the test script, for example using the standard ``cocotb.clock.Clock`` object.

.. code-block:: python

    device_clock = Clock(dut.clk48_device, 20830, 'ps')
    cocotb.fork(device_clock.start())

    harness = get_harness(dut, decouple_clocks=True)

Standard testbench provides provides ``clk48_host`` and ``clk48_device`` signals for this purpose, as well as ``clkdiff`` for tracking the difference during simulation.


Waiting and recovery periods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

USB specifications mandates that the device is allowed some time to initialize. Most common cases are recovey period after port reset (10 ms) and after completing a SET_ADDRESS requests (2 ms after completing status phase). During this time the device is not required to accept any packets.

The test harness provides a dedicated ``wait`` function to use for these longer periods. It outputs a log entry every millisecond to make sure the simulation is still proceeding.


Sending requests
~~~~~~~~~~~~~~~~

Some standard USB requests are abstracted by the harness to provide a more readable interface. These include setting device address and features, requesting descriptors and sending start-of-frame markers.
There are also a number of lower level functions to verify more non-standard or specific situations the device will react to.


Verifying responses
~~~~~~~~~~~~~~~~~~~

Each target provides a JSON config file containg values for the various descriptors the device supports. This file is passed using ``TARGET_CONFIG`` variable to the test script. Then, a ``UsbDevice`` class can be instantiated to store those descriptors as Python objects.

Functions provided by the harness will verify the responses received from device against provided list of bytes. This expected response can be passed to the request function as follows:

.. code-block:: python

    yield harness.get_configuration_descriptor(
        total_length, response=model.configDescriptor[1].get())

If the response received from the device differs, the test fails.

Using low-level functions
~~~~~~~~~~~~~~~~~~~~~~~~~

Apart from the readily available methods, you can send any kind of data to the device and monitor its response. Folowing functions are available in the ``UsbTest`` class:

* ``host_send`` and ``host_recv`` for sending any byte sequence
* ``transaction_setup``, ``transaction_data_in``, ``transaction_data_out``, ``transaction_status_in`` and ``transaction_status_out`` for specifying only parts of transaction
* ``control_transfer_out`` and ``control_transfer_in`` for arbitrary transfers

See :ref:`module reference <cocotb-usb-module-reference>` for details.
