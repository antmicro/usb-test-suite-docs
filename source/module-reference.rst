.. _cocotb-usb-module-reference:

cocotb_usb module reference
===========================

Descriptors
-----------
This module provides classes for standard USB descriptors and requests.

.. automodule:: cocotb_usb.descriptors
    :members:
    :member-order: bysource

Supported USB device classes
----------------------------

DFU
^^^
.. automodule:: cocotb_usb.descriptors.dfu
    :members:
    :member-order: bysource

CDC
^^^
.. automodule:: cocotb_usb.descriptors.cdc
    :members:
    :member-order: bysource


Clocks and triggers
-------------------

This module provides extended cocotb classes for unprecise and drifting clocks.

.. automodule:: cocotb_usb.clocks
    :members:
    :member-order: bysource


Device
------
This module provides a class for containing the set of USB descriptors for a given device.

The descriptors are read from a JSON file. See :ref:`here <config-descriptors-json>` for its structure.

.. autoclass:: cocotb_usb.device.UsbDevice

Host
----
This module provides classes that imitate USB host for tests, abstract lower levels of USB communication and verify the device responses.

.. automodule:: cocotb_usb.host
    :members:
    :member-order: bysource

.. automodule:: cocotb_usb.host_valenty
    :members:
    :member-order: bysource

Monitor
-------
This module provides an object that checks the bus state and returns detected packets.

.. automodule:: cocotb_usb.monitor
    :members:
    :member-order: bysource

Harness
-------

This module provides a function for dynamically assigning a test harness.

.. automodule:: cocotb_usb.harness
    :members:
