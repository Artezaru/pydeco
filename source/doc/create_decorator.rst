How to create a decorator
=========================

To create a new decorator, first import the ``Decorator`` class from the
``pydeco`` package.

.. code-block:: python

    from pydeco import Decorator

Next, create a new class that inherits from the ``Decorator`` class. 
The new class should implement the ``_wrapped`` method, which is called 
when the decorated function is called. The ``_wrapped`` method should be defined as follows:

.. code-block:: python

    class MyDecorator(Decorator):
        def _wrapped(self, func, *args, **kwargs):
            # If you want to get the function name:
            func_name = self._get_func_name(func)
            # Do something before calling the decorated function
            result = func(*args, **kwargs)
            # Do something after calling the decorated function
            return result

.. seealso:: :class:`Decorator`