Adding new USB class
--------------------

If the device uses a USB class not supported in cocotb-usb, you are welcome to extend it. It should be placed as a separate file in *cocotb_usb/descriptors*.

Class descriptors
~~~~~~~~~~~~~~~~~

All descriptors for the new class should inherit from the Descriptor class. It provides some basic types and methods to access the descriptor in the test functions.

Descriptor functions should implement a ``__bytes__`` functions to represent the object in a byte form. For this the inbuilt Python ``struct`` module is used. Descriptor class can either include a format string describing its structure or generate it dynamically, for example when its length is not fixed.

Class requests
~~~~~~~~~~~~~~
Class-specific requests are implemented as functions, internally using ``USBDeviceRequest`` to build the request.

Parser and config file support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each class needs a parser function to make sure its descriptors can be filled with device-specific values and compared in the test cases. The class file should include a parsing function that takes a field from the JSON file and returns an initialized descriptor object specific to this class.

Class specific parsers should be stored in a dictionary with keys corresponding to their descriptor types. This dictionary should then be added along with the class code to ``getClassParsers`` in ``device.py``.


Documentation
~~~~~~~~~~~~~

Documentation for the module is generated using sphinx and autodoc, so it relies on proper docstrings. All objects that are intended to be used in tests (including all descriptors and requests) should be documented.
