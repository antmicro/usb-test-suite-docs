Running the tests
=================

Tests are controlled by a makefile stored in usb-test-suite-testbenches.
To run them using the default parameters simply use:

.. code-block:: bash

    cd usb-test-suite-testbenches
    make

Test results will be available by default in *results.xml*. The default target that will be run is ``sim``, which will execute the *test-enum.py* script on valentyUSB IP core.
Signal states will be saved to a *dump.vcd* file to be opened for example in GTKWave or decoded using sigrok. You can also save the transaction packets from the test to a *usb.pcap* file. This can be done by invoking ``make decode`` target.

Note that with ``make decode`` only USB line states are saved to a separate file called ``usb.vcd``.

Some options taken by the makefile are:

    * ``TARGET`` - by default *valentyUSB*. This is the IP core that will be used as device under test.
    * ``TEST_SCRIPT`` - name of the file from the *tests* directory to be scanned for test cases. Default value is *test-enum*

Since we use cocotb for testing, options and variables used there are also available to be set, for example:

    * ``SIM`` - simulator to be used. The test suite was developed using iverilog.
    * ``TESTCASE`` - specify a single function to be run.

To clean the simulation output, use ``make clean``.
