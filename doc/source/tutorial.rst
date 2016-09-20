Tutorial
========

This tutorial will guide you through the basic steps of using the ``io_helper`` module. 

Saving and loading
------------------

First off, let's try saving some data to a file, using the :func:`.save` function:

.. code :: python

    from fsc.io_helper import save
    
    data = [1, 2, 3, 4]
    save(data, 'filename.json')
    
To get the data back, you can use the :func:`.load` function:
    
.. code :: python

    from fsc.io_helper import load
    
    result = load('filename.json')

In both cases, the file format is automatically detected from the file ending. Possible file endings are ``.json`` for JSON files, ``.msgpack`` for msgpack, and ``.p`` or ``.pickle`` for pickle.

You can also specify the serializer explicitly, by passing the ``json``, ``msgpack`` or ``pickle`` module as the ``serializer`` keyword argument.

.. code :: python

    import json
    import numpy as np
    from fsc.io_helper import save, load
    
    data = np.arange(4)
    save(data, 'filename_without_ending', serializer=json)
    
    result = load('filename_without_ending', serializer=json)

.. note :: If no serializer is given and the file ending is not understood, the ``json`` serializer will be used for saving data. When loading, an error is thrown instead to avoid accidentally loading corrupted data.

Custom encoding
---------------

When serializing complex objects to and from the ``pickle`` and ``msgpack`` formats, custom encoding and decoding functions are needed. This can be done by setting a custom encoder, using the :func:`.set_encoding` function. 

The argument to this function (the encoder) must have two methods named ``encode`` and ``decode``. They will be passed as the ``default`` argument in case of encoding and ``object_hook`` argument in case of decoding, as defined in the ``json`` module.

To see how such an encoder / decoder could be done, you can have a look at ``io_helper/default_encoding.py``.
