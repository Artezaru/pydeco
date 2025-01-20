Memory Usage
============

The :class:`pydeco.decorators.Memory` decorator is used to measure the runtime of a function.
``Memory`` is a sub-class of the class :class:`pydeco.LoggerUtils` and can be use for the :class:`pydeco.decorators.FunctionLogger` decorator.
In this example, we will only show how to use the ``Memory`` decorator as a standalone decorator.
The usage of the ``Memory`` decorator into the ``FunctionLogger`` decorator is described in the documentation :doc:`./function_logger_example`.

First we need to import the ``Memory`` decorator with the following command:

.. code-block:: python

    from pydeco.decorators import Memory

Then we can use the ``Memory`` as describe in the documentation :doc:`../use_decorator`.

.. code-block:: python

    memory = Memory(activated=True, signature_name_format='{name}')

    @memory
    def example_function():
        return [i for i in range(1000000)]
    
    bigdata = example_function()

The output will be:

.. code-block:: console

    example_function - memory usage : 38MB 308KB 0B