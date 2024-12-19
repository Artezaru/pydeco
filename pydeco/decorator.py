class Decorator(object):
    """
    Base class for decorators.

    The subclasses must implement the _wrapper method with the following signature:

    .. code-block:: python

        def _wrapper(self, func, *args, **kwargs):
            do_something()
            return func(*args, **kwargs)

    The _wrapper method is can access the function name using the self._get_func_name(func) method.

    The function func is the function to decorate, func_name is the name of the function to decorate.
    The func_name is constructed usign the name_format attribute. (see below)
    
    Parameters
    ----------
        activated: bool, optional
            The activation status of the decorator.
            Default value is True

        name_format: str, optional
            The format of the name to display.
            Default value is "{name}"

    Attributes
    ----------
        activated: bool
            The activation status of the decorator.
        
        name_format: str
            The format of the name to display. (see below)
        
    Methods
    -------
        is_activated()
            Returns decorator activation status.
        
        is_deactivated()
            Returns decorator deactivation status.
        
        set_activated(activated: bool = True)
            Sets the decorator activation status.
        
        set_deactivated(deactivated: bool = True)
            Sets the decorator deactivation status.

        set_name_format(name_format: str)
            Sets the name format of the decorator.
        
        get_name_format()
            Get the name format of the decorator.
    
    Formatting name
    ----------------
    The name_format attribute is a string that can contain the following format arguments:

    - {name}: The name of the function
    - {module}: The module of the function
    - {qualname}: The qualname of the function

    Example of valid name_format:

    - "{name}": Display the name of the function
    - "{module}.{qualname}": Display the module and qualname of the function
    - "Function {name} from {module}": Display a custom message with the function name and module
    - "{name} and \\{other}": Display the string "{other}" (use \\ to escape the brackets)
    - "\\{other {name} other}": Display the string "{other {name} other}" (use \\ to escape the brackets)

    Example of invalid name_format:

    - "{other}": The format argument "other" is not valid
    - "{name} and {qualname": The brackets are not correctly closed
    """
    
    correct_format_args = ["name", "module", "qualname"]

    def __init__(self, *, 
        activated: bool = True,
        name_format: str = "{name}",
        ):
        # Check if given arguments are right types
        if not isinstance(activated, bool):
            raise TypeError("Parameter activated is not a booleen.")
        if not isinstance(deep_name, str):
            raise TypeError("Parameter name_format is not a string.")
        # Set the decorator activation status
        self._activated = True
        self._deep_name = deep_name

    # Properties getters and setters
    @property
    def activated(self) -> bool:
        return self._activated

    @activated.setter
    def activated(self, activated: bool):
        if not isinstance(activated, bool):
            raise TypeError("Parameter activated is not a booleen.")
        self._activated = activated
    
    @property
    def name_format(self) -> str:
        return self._name_format
    
    @name_format.setter
    def name_format(self, name_format: str):
        if not self._check_name_format(name_format):
            raise ValueError("Parameter name_format is not correct.")
        self._name_format = name_format
    
    # Decorator activation and deactivation (other way around)
    def is_activated(self) -> bool:
        """ 
        Returns decorator activation status.
        
        Returns
        -------
            activated: bool
                If the decorator is activated.

        .. seealso::
        
            - :meth:`is_deactivated` : Returns decorator deactivation status.
            - :meth:`set_activated` : Sets the decorator activation status.
        """
        return self.activated

    def is_deactivated(self) -> bool:
        """ 
        Returns decorator deactivation status.
        
        Returns
        -------
            desactivated: bool
                If the decorator is deactivated.

        .. seealso::
        
            - :meth:`is_activated` : Returns decorator activation status.
            - :meth:`set_deactivated` : Sets the decorator deactivation status.
        """
        return not self.activated

    def set_activated(self, activated: bool = True) -> None:
        """
        Sets the decorator activation status.
        
        Parameters
        ----------
            activated: bool, optional
                The activation status to apply to the decorator.
                Default value is True
        
        Raises
        ------
            TypeError: If the given argument is not a booleen.

        .. seealso::
        
            - :meth:`is_activated` : Returns decorator activation status.
            - :meth:`set_deactivated` : Sets the decorator deactivation status.
        """
        self.activated = activated

    def set_deactivated(self, deactivated: bool = True) -> None:
        """
        Sets the decorator deactivation status.
        
        Parameters
        ----------
            deactivated: bool, optional
                The negation of the activation status to apply to the decorator.
                Default value is True
        
        Raises
        ------
            TypeError: If the given argument is not a booleen.

        .. seealso::

            - :meth:`is_deactivated` : Returns decorator deactivation status.
            - :meth:`set_activated` : Sets the decorator activation status.
        """
        self.activated = not deactivated

    # Decorator name formatting
    def set_name_format(self, name_format: str) -> None:
        """
        Sets the name format of the decorator.
        
        Parameters
        ----------
            name_format: str
                The format of the name to display.
        
        Raises
        ------
            ValueError: If the given name format is not correct.
            TypeError: If the given argument is not a string.

        .. seealso::

            - :meth:`get_name_format` : Allows to get the format of the name of the decorator.
            
        """
        self.name_format = name_format
    
    def get_name_format(self) -> str:
        """
        Get the name format of the decorator.
        
        Returns
        -------
            name_format: str
                The format of the name to display.

        .. seealso::

            - :meth:`set_name_format` : Allows to set the format of the name of the decorator.
        """
        return self.name_format

    # Private methods
    def _check_accolades(self, name_format: str) -> bool:
        """
        Check if the accolades are correctly closed.

        Parameters
        ----------
            name_format: str
                The name format to check.
        
        Returns
        -------
            is_correct: bool
                If the accolades are correctly closed.
        """
        if not isinstance(name_format, str):
            raise TypeError("Parameter name_format is not a string.")
        stack = []
        for char in name_format:
            if char == "{":
                stack.append("{")
            elif char == "}":
                if len(stack) == 0:
                    return False
                stack.pop()
        return len(stack) == 0

    def _check_name_format(self, name_format: str) -> bool:
        """
        Check if the name format is correct.

        Parameters
        ----------
            name_format: str
                The name format to check.
        
        Returns
        -------
            is_correct: bool
                If the name format is correct.
        """
        if not isinstance(name_format, str):
            raise TypeError("Parameter name_format is not a string.")
        if not self._check_accolades(name_format):
            return False
        pattern = r'(?<!\\)\{(.*?)(?<!\\)\}'
        matches = re.findall(pattern, name_format)
        for match in matches:
            if match not in self.correct_format_args:
                return False
        return True

    def _get_func_name(self, func) -> str:
        """
        Get the function name.

        Parameters
        ----------
            func: function
                The function to get the name from.
            
        Returns
        -------
            func_name: str
                The function name.
        """
        pattern = r'(?<!\\)\{(.*?)(?<!\\)\}'
        # Replace the format with the function attributes
        def replace(match, format_args: dict) -> str:
            key = match.group(1)
            return format_args.get(key, f"{{{key}}}") # Return the key if not found
        # Get the function attributes
        format_args = {
            "name": func.__name__,
            "module": func.__module__,
            "qualname": func.__qualname__,
        }
        # Replace the format with the function attributes
        formatted_name = re.sub(pattern, lambda match: replace(match, format_args), self._name_format)
        formatted_name = formatted_name.replace(r'\{', '{').replace(r'\}', '}')
        return formatted_name

    # Decorator wrapper
    def __call__(self, func):
        def wrapped(*args, **kwargs):
            if self._activated:
                return self._wrapper(func, *args, **kwargs)
            else:
                return func(*args, **kwargs)
        return wrapped

    def _wrapper(self, func_name, *args, **kwargs):
        """
        Wrapper method to be implemented in subclasses.
        """
        raise NotImplementedError("Method _wrapper must be implemented in subclasses.")