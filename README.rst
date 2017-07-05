PyMixer
=======

Wrapping class for linux command line ``amixer`` to get/set volume from python.

Example
~~~~~~~

But everything you need to know is this:

.. code:: python

    from pymixer import PyMixer

        mixer = PyMixer()
        # to set volume you can do just
        mixer.set_volume(50)
        # if you want to know current volume call
        volume = mixer.get_volume()

License
~~~~~~~

This piece of code is licensed under The MIT License.
