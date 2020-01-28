Introduction
============

While there are numerous USB IP cores available, it is not obvious how to verify their functionality and features.
The code usually comes with tests, but the scenarios seldom correspond between the cores, they are primarily device-specific and test low-level core behavior.

USB-test-suite aims to amend that by providing a comprehesive test bench for testing USB IP cores - in Python.

The objective is to test open source IP cores in behavioral simulation for:

* logic signal correctness
* handling of USB protocol
* validation of enumeration procedure

Currently we support USB1.1. Main project repository is located `here`_.

.. _`here`: https://github.com/antmicro/usb-test-suite-build

Structure of this document
--------------------------

* :doc:`setup` - this section details first steps needed to get the testbench running.
* :doc:`architecture` - description of files and concepts used in the project.
* :doc:`usage` - this section describes parameters and targets for running existing tests.
* :doc:`targets` - list of currently supported IP cores.
* :doc:`tests` - list of available tests.
* :doc:`development` - details on how to add new targets and tests.
* :doc:`cocotb-usb` - description of Python module at the heart of the testbench.
* :doc:`module-reference`
