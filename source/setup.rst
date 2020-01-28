.. _setup:

Quickstart
==========

Base repository for the project is located at https://github.com/antmicro/usb-test-suite-build

Prerequisites
-------------

* `litex <https://github.com/enjoy-digital/litex>`_
* `cocotb <https://github.com/cocotb/cocotb>`_
* `iverilog <http://iverilog.icarus.com/>`_

Steps
-----

#. Clone the base repository

    .. code-block:: bash

        git clone --recursive https://github.com/antmicro/usb-test-suite-build

#. Run the setup script

    .. code-block:: bash

        cd usb-test-suite-build
        ./setup.sh

#. Run the tests

    .. code-block:: bash

       cd usb-test-suite-testbenches
       make

Additional setup
----------------

Signal traces are saved in **.vcd** format. They can be viewed using `GTKWave`_.

In order to decode USB signals sigrok decodes are used. You can obtain **sigrok-cli** and **libsigrokdecode** from `its website`_ or use `conda package`_.

.. note:: Packages provided by your repository manager may be out-of-date, which can lead to significantly longer decoding times.


.. _`GTKWave`: http://gtkwave.sourceforge.net/
.. _`its website`: https://sigrok.org
.. _`conda package`: https://anaconda.org/symbiflow/sigrok-cli
