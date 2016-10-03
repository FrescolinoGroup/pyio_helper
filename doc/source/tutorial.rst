Tutorial
========

This tutorial will guide you through the basic steps of using the ``iohelper`` module. 

Creating a :class:`.SerializerDispatch` instance
------------------------------------------------

The first thing you need to do is creating an instance of the :class:`.SerializerDispatch` class. The constructor takes a single argument -- an object which has two members ``encode`` and ``decode``. The ``encode`` function should convert the object into a JSON / msgpack - compatible type, and ``decode`` should do the inverse. When saving / loading, the functions are passed as the ``default`` and ``object_hook`` parameters, respectively (see :py:func:`json.dump` and :py:func:`json.load`).

Unless you want to specify a custom encoding, you can use :mod:`.encoding.default`. This encoding handles common numpy and built-in types.

.. code :: python

    import fsc.iohelper as io
    IO_HANDLER = io.SerializerDispatch(io.encoding.default)

Saving and loading
------------------

Having created the :class:`.SerializerDispatch` instance, you can use it to save data to a file:

.. code :: python

    IO_HANDLER = ...
    data = [1, 2, 3, 4]
    IO_HANDLER.save(data, 'filename.json')
    
To get the data back, you can use the :meth:`.load` method:
    
.. code :: python

    IO_HANDLER = ...
    result = IO_HANDLER.load('filename.json')

In both cases, the file format is automatically detected from the file ending. Possible file endings are ``.json`` for JSON files, ``.msgpack`` for msgpack, and ``.p`` or ``.pickle`` for pickle.

You can also specify the serializer explicitly, by passing the ``json``, ``msgpack`` or ``pickle`` module as the ``serializer`` keyword argument.

.. code :: python

    import json
    import numpy as np
    
    IO_HANDLER = ...
    data = np.arange(4)
    IO_HANDLER.save(data, 'filename_without_ending', serializer=json)
    
    result = IO_HANDLER.load('filename_without_ending', serializer=json)

.. note :: If no serializer is given and the file ending is not understood, the ``json`` serializer will be used for saving data. When loading, an error is thrown instead to avoid accidentally loading corrupted data.
