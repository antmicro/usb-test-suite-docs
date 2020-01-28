Supported targets
=================

`ValentyUSB IP core`_
---------------------

CPU-less target with **eptri** interface written in LiteX.


`usb1_device`_
--------------

A USB1.1 IP core developed by asics.ws in Verilog.


`Foboot`_
---------

Target with VexRiscV CPU running bare-metal Foboot firmware. It utilizes **epfifo** interface of ValentyUSB core.


`TinyFPGA-Bootloader`_
----------------------

IP core written in Verilog with interesting features, like providing an interface to program SPI flash memory over USB.


`tnt`s USB IP core`_
--------------------

Target with a picorv32 CPU, running bare-metal firmware interfacing with Verilog IP core.


.. _`ValentyUSB IP core`: https://github.com/im-tomu/valentyusb
.. _`usb1_device`: https://github.com/www-asics-ws/usb1_device
.. _`Foboot`: https://github.com/im-tomu/foboot
.. _`TinyFPGA-Bootloader`: https://github.com/tinyfpga/TinyFPGA-Bootloader
.. _`tnt`s USB IP core`: https://github.com/smunaut/ice40-playground/tree/master/cores/usb
