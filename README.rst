Tapioca Asana: Smart python client for Asana.com API
====================================================

Install
-------

.. code-block:: console

    pip install tapioca-asana

How to use it
-------------

.. code-block:: python

    from tapioca_asana import Asana


    asana = Asana(personal_key='{your-key}')
    print(asana.projects().get())

What to do next?
----------------

* Learn more about `Tapioca Wrapper`_.
* Explore this package using `Jupyter Notebook`_.
* Have fun!

.. _Tapioca Wrapper: http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html
.. _Jupyter Notebook: http://jupyter.org/

License
-------

The MIT License (MIT)

Copyright (c) 2017 Henrique Bastos <henrique@bastos.net>
