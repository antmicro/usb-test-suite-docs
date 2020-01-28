Example tests
=============

The usb-test-suite-testbenches repository contains example test modules in the
*tests* folder. They can serve as a basis to write your own tests.


test-basic
----------

This script verifies low-level functionality of the IP core, like ability to
perform simple control transfers.

test-sequence
-------------

Another basic script that verifies that multiple control transfers in a sequence are processed correctly.

test-sof
--------

This script verifies device behavior when exposed to SOF packet.

test-enum
---------

This test simulates enumeration process on a Linux system. The device is
queried for its basic descriptors, their content is verified against supplied
config file, then a configuration is chosen and set.

If the device implements string descriptors, they will also be read.

This script does not verify any class-related behavior.


test-w10enum
------------

In this test we simulate the enumeration process on a Windows machine.

test-macOSenum
--------------

This test script corresponds to an enumeration process under macOS 10.X system.


test-clocks
-----------

This script verifies device behavior in presence of clock mismatch between the
device and host. Three test cases are defined:

    * ``test_accurate``

      Reference behavior with no clock discrepancy. Device is queried for its
      USB device descriptor.

    * ``test_drift``

      Host and device clocks are decoupled and a slight period mismatch is
      introduced to the second. Then the device is queried the same descriptors
      as in test-accurate.

    * ``test_jitter``

      The device is fed an unstable clock with period deviation of up
      to +- 3500 ps. The period variation is introduced using Python rand()
      function.

test-cdc
--------

A script providing sample CDC transfers to a TinyFPGA bootloader device. Apart from a couple of control requests, the test send a BOOT command to the core and checks status of corresponding line in DUT.


test-valenty-cdc
----------------

A similar test for ValentyUSB IP core.
