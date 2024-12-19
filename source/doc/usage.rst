How to use a decorator
======================

General usage
-------------

pydeco provides a number of decorators that can be used to modify the behavior of functions.
You can also create your own decorators.

.. seealso:: :doc:`decorators`

.. seealso::

   :doc:`create_decorator`

To use a decorator of pydeco, first import the decorator you want to use and create an instance of it.

.. code-block:: python

   from pydeco.decorators import Logger
   logger = Logger()

Next, you can use the decorator by adding it to the function you want to decorate.

.. code-block:: python

   @logger
   def my_function():
       print('Hello, world!')

If you want to decorate a method of a class, you can use the decorator in the same way.

.. code-block:: python

   class MyClass:
       @logger
       def my_method(self):
           print('Hello, world!')

But a better way to decorate a method of a class is to use the ``class_propagate`` function of pydeco.
First import the ``class_propagate`` function from the ``pydeco`` package.

.. code-block:: python

   from pydeco import class_propagate

Next, you can use the ``class_propagate`` function to decorate the method of a class. 
The ``class_propagate`` function will automatically propagate the decorator to all methods of the class.

.. code-block:: python

   @class_propagate(logger)
   class MyClass:

       def my_method(self):
           print('Hello, world!')

To select the methods to decorate, you can use the ``methods`` parameter of the ``class_propagate`` function.
In the following example, the ``logger`` decorator is only applied to the ``my_method`` method of the ``MyClass`` class.
The ``my_other_method`` method is not decorated.

.. code-block:: python

   @class_propagate(logger, methods=['my_method'])
   class MyClass:

       def my_method(self):
           print('Hello, world!')

       def my_other_method(self):
           print('Goodbye, world!')





More advanced usage
-------------------

If your decorator use the name of the function (as the ``logger`` decorator does), the following example will have a problem:

.. code-block:: python

    @logger
    def my_function():
        print('Hello, world!')
    
    @class_propagate(logger)
    class MyClass:
    
        def my_function(self):
            print('Hello, world!')

For the ``logger`` decorator, the two functions will be considered as the same function, because the name of the function is used to identify it.
To avoid this problem, you can set the name_format of the decorator.

.. seealso::

   :class:`Decorator`

The name_format can be set when creating the decorator or when using it. The following line of code will solve the issue:

.. code-block:: python

    logger.set_name_format('{module}.{qualname}')

Now the two functions will be considered as different functions.