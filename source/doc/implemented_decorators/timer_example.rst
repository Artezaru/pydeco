Timer Usage
===========

The :class:`pydeco.decorators.Timer` decorator is used to measure the runtime of a function.
``Timer`` is a sub-class of the class :class:`pydeco.ProfilerUtils` and can be use for the :class:`pydeco.decorators.FunctionProfiler` decorator.
In this example, we will only show how to use the ``Timer`` decorator as a standalone decorator.
The usage of the ``Timer`` decorator into the ``FunctionProfiler`` decorator is described in the documentation :doc:`./function_profiler_example`.

First we need to import the ``Timer`` decorator with the following command:

.. code-block:: python

    from pydeco.decorators import Timer

Then we can use the ``Timer`` as describe in the documentation :doc:`../use_decorator`.

.. code-block:: python

    timer = Timer(activated=True, signature_name_format='{name}')

    @timer
    def example_function():
        import time
        print("Hello")
        time.sleep(70)
    
    example_function()

The output will be:

.. code-block:: console

    Hello
    example_function - runtime : 0h 1m 10.0000s