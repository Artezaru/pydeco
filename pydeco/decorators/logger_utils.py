from ..decorator import Decorator

class LoggerUtils(Decorator):
    """
    ``LoggerUtils`` class is a base class for utils of the :class:`pydeco.decorators.FunctionLogger` decorator.

    The subclasses must implement the following methods:

    .. code-block:: python

        def pre_execute(func, *args, **kwargs) -> None:
            pass

        def post_execute(func, *args, **kwargs) -> None:
            pass

        def handle_result(self):
            pass

        def string_result(self, result) -> str:
            pass

    The subclasses must contain the following attributes:

    - `data_name`: str
        The name of the data collected by the logger.

    .. note::

        The subclasses can also be used as a simple decorator that prints on the console the result.
    """
    data_name: str = None

    def _wrapper(self, func, *args, **kwargs):
        pre_execute = self.pre_execute(func, *args, **kwargs)
        outputs = func(*args, **kwargs)
        post_execute = self.post_execute(func, *args, **kwargs)
        # print the result of the logger utils
        function_signature_name = self.get_signature_name(func)
        print(f"{function_signature_name} - {self.string_result(self.handle_result())}")
        return outputs

    # To be implemented in subclasses
    def pre_execute(self, func, *args, **kwargs) -> None:
        """
        Method to be implemented in subclasses.
        """
        raise NotImplementedError("Method pre_execute must be implemented in subclasses.")

    def post_execute(self, func, *args, **kwargs) -> None:
        """
        Method to be implemented in subclasses.
        """
        raise NotImplementedError("Method post_execute must be implemented in subclasses.")
    
    def handle_result(self):
        """
        Method to be implemented in subclasses.
        """
        raise NotImplementedError("Method handle_result must be implemented in subclasses.")

    def string_result(self, result) -> str:
        """
        Method to be implemented in subclasses.
        """
        raise NotImplementedError("Method string_result must be implemented in subclasses.")
    