FunctionLogger Usage
====================

The :class:`pydeco.decorators.FunctionLogger` decorator is used to log some data about the function execution as the runtime, the memory usage, etc.
``FunctionLogger`` is a sub-class of the class :class:`pydeco.Decorator`.

First we need to import the ``FunctionLogger`` decorator with the following command:

.. code-block:: python

    from pydeco.decorators import FunctionLogger

Then we can connect some :class:`pydeco.LoggerUtils` decorators to the ``FunctionLogger`` decorator.
By connecting a ``LoggerUtils`` decorator to the ``FunctionLogger`` decorator, the ``LoggerUtils`` decorator will be activated when the ``FunctionLogger`` decorator is activated and the ``FonctionLogger`` decorator will log the results of the ``LoggerUtils`` decorators.
In this example, we will connect the :class:`pydeco.decorators.Timer` and :class:`pydeco.decorators.Memory` decorators to the ``FunctionLogger`` decorator.
To do this, we have three possibilities:

- giving the ``LoggerUtils`` decorators as arguments of the ``FunctionLogger`` decorator.

.. code-block:: python

    from pydeco.decorators import Timer, Memory

    function_logger = FunctionLogger(
        activated=True, 
        signature_name_format='{name}', 
        logger_utils=[Timer, Memory],
        log_format='datetime')

- using the method ``connect_logger_utils`` of the ``FunctionLogger`` decorator.

.. code-block:: python

    from pydeco.decorators import Timer, Memory

    function_logger = FunctionLogger(activate=True, signature_name_format='{name}')
    function_logger.connect_logger_utils([Timer, Memory])

- using the method ``autoconnect_logger_utils`` of the ``FunctionLogger`` decorator.

.. code-block:: python

    function_logger = FunctionLogger(activate=True, signature_name_format='{name}')
    function_logger.autoconnect_logger_utils()

The method ``autoconnect_logger_utils`` connects all the implemented ``LoggerUtils`` decorators of ``pydeco``.
This auto-method can't be used if the user has implemented a new ``LoggerUtils`` decorator.

Then we can use the ``FunctionLogger`` as describe in the documentation :doc:`../use_decorator`.

.. code-block:: python

    @function_logger
    def example_function():
        import time
        time.sleep(10)
        return [i for i in range(1000000)]

    @function_logger
    def other_example_function():
        import time
        time.sleep(5)
        return [i for i in range(5000)]

    example_function()
    example_function()
    other_example_function()
    example_function()

To store the log of the ``FunctionLogger`` decorator, just print the ``function_logger`` object.

.. code-block:: python

    print(function_logger)

The output when printing the ``function_logger`` object depends on the ``log_format`` attribute of the ``FunctionLogger`` object.

Selecting the log format
------------------------

To change the log format, use the method :func:`pydeco.decorators.FunctionLogger.set_log_format`.

If the log_format is set to "datetime", the output will be:

.. code-block:: console

    [2025-01-20 16:23:08.696188] - [example_function] - runtime : 0h 0m 10.0217s - memory usage : 38MB 320KB 0B
    [2025-01-20 16:23:18.723690] - [example_function] - runtime : 0h 0m 10.0239s - memory usage : 36MB 256KB 0B
    [2025-01-20 16:23:28.752144] - [other_example_function] - runtime : 0h 0m 5.0006s - memory usage : 0MB 0KB 0B
    [2025-01-20 16:23:33.753020] - [example_function] - runtime : 0h 0m 10.0304s - memory usage : 28MB 512KB 0B

If the log_format is set to "function", the output will be:

.. code-block:: console

    [example_function]
        [2025-01-20 16:36:44.569795] - runtime : 0h 0m 10.0225s - memory usage : 38MB 380KB 0B
        [2025-01-20 16:36:54.597933] - runtime : 0h 0m 10.0218s - memory usage : 37MB 256KB 0B
        [2025-01-20 16:37:09.626250] - runtime : 0h 0m 10.0193s - memory usage : 28MB 0KB 0B
    [other_example_function]
            [2025-01-20 16:37:04.625249] - runtime : 0h 0m 5.0006s - memory : 0MB 0KB 0B

If the log_format is set to "cumulative", the output will be:

.. code-block:: console

    [example_function] - 3 calls - runtime : 0h 0m 30.0666s - memory usage : 103MB 232KB 0B
    [other_example_function] - 1 calls - runtime : 0h 0m 5.0008s - memory usage : 0MB 0KB 0B


