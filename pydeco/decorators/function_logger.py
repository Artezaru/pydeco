from ..decorator import Decorator
from .logger_utils import LoggerUtils
from .timer import Timer
from .memory import Memory

from typing import List, Union, Type
import datetime

class FunctionLogger(Decorator):
    """
    ``FunctionLogger`` is a :class:`pydeco.Decorator` that logs the execution of a function.
    Several loggers utils :class:`pydeco.decorators.LoggerUtils` can be connected to the ``FunctionLogger`` according to the user's needs.

    .. warning::
        If 2 functions/methods have the same 'function_signature_name' attribute, the Logger will combined the two in one.
        To solve this issue, set the `signature_name_format` attribute.

    Properties
    ----------
    logger_utils : Union[Type, List[Type]]
        The list of sub-classes of the ``LoggerUtils`` class connected to the ``FunctionLogger``.
        Default is None.

    log_format : str
        The format of the log string. (see :meth:`pydeco.decorators.function_logger.FunctionLogger.set_log_format`).
        Default is "datetime". 

    Methods
    -------
    connect_logger_utils(logger_utils: Union[Type, List[Type]])
        Connects a sub-class of the ``LoggerUtils`` class to the ``FunctionLogger``.

    autoconnect_logger_utils():
        Connects the default ``LoggerUtils`` to the ``FunctionLogger``.

    disconnect_all()
        Disconnects all the ``LoggerUtils`` to the ``FunctionLogger``.

    initialize()
        Initializes the ``FunctionLogger`` by removing all the logged data.

    set_log_format(log_format: str)
        Sets the log format of the ``FunctionLogger``.
    
    get_log_format() -> str
        Gets the log format of the ``FunctionLogger``.

    extract_loggeg_functions() -> List[str]
        Extracts the list of the logged functions.

    generate_logs() -> str
        Generates the logs of the ``FunctionLogger`` according to the log format.

    generate_logs_datetime() -> str
        Generates the logs of the ``FunctionLogger`` in the datetime format.

    generate_logs_function() -> str
        Generates the logs of the ``FunctionLogger`` in the function format.

    generate_logs_cumulative() -> str
        Generates the logs of the ``FunctionLogger`` in the cumulative format.

    write_logs(file_path: str)
        Writes the logs of the ``FunctionLogger`` in a file at the specified path.
    """
    correct_log_format = ["datetime", "function", "cumulative"]

    def __init__(self, logger_utils: Union[Type, List[Type]] = None,
                 log_format: str = "datetime", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.disconnect_all()
        self.initialize()
        self.connect_logger_utils(logger_utils)
        self.log_format = log_format

    # Properties getters and setters
    @property
    def log_format(self) -> str:
        return self._log_format

    @log_format.setter
    def log_format(self, log_format: str) -> None:
        if not isinstance(log_format, str):
            raise TypeError("The log_format must be a string.")
        if log_format not in self.correct_log_format:
            raise ValueError(f"The log_format must be one of the following: {self.correct_log_format}.")
        self._log_format = log_format

    # Decorator log format (other way around)
    def set_log_format(self, log_format: str) -> None:
        """
        Sets the log format of the ``FunctionLogger``.

        .. note:: 

            The log format can also be set using the 'log_format' attribute.

        .. important::

            The correct log format are: "datetime", "function", "cumulative". (see below)

            If the log format is set to "datetime", the log string will be in the following format:

            .. code-block:: console
            
                [datetime] - [function_signature_name] - data_name: data - other_data_name: other_data
                [datetime] - [other_function_signature_name] - data_name: data - other_data_name: other_data
                [datetime] - [function_signature_name] - data_name: data - other_data_name: other_data
                
            If the log format is set to "function", the log string will be in the following format:

            .. code-block:: console

                [function_signature_name]
                    [datetime] - data_name: data - other_data_name: other_data
                    [datetime] - data_name: data - other_data_name: other_data
                [other_function_signature_name]
                    [datetime] - data_name: data - other_data_name: other_data
                    [datetime] - data_name: data - other_data_name: other_data

            If the log format is set to "cumulative", the log string will be in the following format:

            .. code-block:: console

                [function_signature_name] - N calls - data_name: cumulative_data - other_data_name: cumulative_other_date
                [other_function_signature_name] - N calls - data_name: cumulative_data - other_data_name: cumulative_other_date

            .. warning::
                The `cumulative` log format can be break if one logger utils returns non-numeric data.

        Parameters
        ----------
        log_format : str
            The log format of the ``FunctionLogger``.

        Raises
        ------
        TypeError
            If the log_format is not a string.
        ValueError
            If the log_format is not in the correct log format.
        """
        self.log_format = log_format

    def get_log_format(self) -> str:
        """
        Gets the log format of the ``FunctionLogger``.

        .. note::
        
            The log format can also be get using the 'log_format' attribute.

        Returns
        -------
        str
            The log format of the ``FunctionLogger``.
        """
        return self.log_format

    # FunctionLogger methods
    def initialize(self) -> None:
        """
        Initializes the ``FunctionLogger`` by removing all the logger data.

        The connected loggers utils are not removed.
        """
        self._logged_data = [] # [datetime, function_signature_name, {data_name: data}]

    def disconnect_all(self) -> None:
        """
        Disconnects all the logger utils connected to the ``FunctionLogger``.

        .. note::

            The logged data are not removed.
        """
        self._logged_utils = {} # {data_name: LoggerUtils}
    
    def connect_logger_utils(self, logger_utils: Union[Type, List[Type]] = None) -> None:
        """
        Connects a sub-class of the ``LoggerUtils`` class to the ``FunctionLogger``.
        If a logger utils is None, it will be ignored.

        .. note::
            If a sub-class of the ``LoggerUtils`` with same 'data_name' attribute is already connected, the new logger will replace the old one.

        Parameters
        ----------
        logger_utils : Union[Type, List[Type]]
            The sub-class of the ``LoggerUtils`` class to connect to the ``FunctionLogger``.

        Raises
        ------
        TypeError
            If the logger is not an instance of ``LoggerUtils`` or a list of ``FunctionLogger``.
        """
        # Recursively connect the logger
        if isinstance(logger_utils, list):
            for log_utils in logger_utils:
                self.connect_logger_utils(log_utils)
        else:
            if logger_utils is None:
                return
            if not issubclass(logger_utils, LoggerUtils):
                raise TypeError("The logger must be a sub-class of LoggerUtils.")
            self._logged_utils[logger_utils.data_name] = logger_utils()
    
    def autoconnect_logger_utils(self) -> None:
        """
        Connects the default logger utils to the ``FunctionLogger``.

        The default logger utils are: 

        - Timer, see :class:`pydeco.decorators.timer.Timer`.
        - Memory, see :class:`pydeco.decorators.memory.Memory`.
        """
        self.connect_logger_utils([Timer, Memory])

    # Wrapper method
    def _wrapper(self, func, *args, **kwargs):
        """
        Compute the logged data of the function execution.
        """
        function_signature_name = self.get_signature_name(func)
        date = datetime.datetime.now()
        data = {}
        # Pre-execute
        for log_utils in self._logged_utils.values():
            log_utils.pre_execute(func, *args, **kwargs)
        # Execute the function
        outputs = func(*args, **kwargs)
        # Post-execute
        for log_utils in self._logged_utils.values():
            log_utils.post_execute(func, *args, **kwargs)
        # Handle the logged data
        for log_utils in self._logged_utils.values():
            data[log_utils.data_name] = log_utils.handle_result()
        # Append the logged data
        self._logged_data.append([date, function_signature_name, data])
        return outputs

    # Log methods
    def extract_loggeg_functions(self) -> List[str]:
        """
        Extracts the list of the logged functions.

        Returns
        -------
        List[str]
            The sorted list of the logged functions.
        """
        loggeg_functions = list(set([log[1] for log in self._logged_data]))
        sorted(loggeg_functions)
        return loggeg_functions

    def generate_logs_datetime(self) -> str:
        """
        Generates the logs of the ``FunctionLogger`` in the datetime format.

        Returns
        -------
        str
            The logs of the ``FunctionLogger`` in the datetime format.

        .. seealso::

            :func:`pydeco.decorators.FunctionLogger.set_log_format()`
        """
        logs = ""
        for log in self._logged_data:
            date = log[0]
            function_signature_name = log[1]
            data = log[2]
            logs += f"[{date}] - [{function_signature_name}]"
            for data_name, data_value in data.items():
                log_utils = self._logged_utils[data_name]
                logs += f" - {log_utils.string_result(data_value)}"
            logs += "\n"
        return logs

    def generate_logs_function(self) -> str:
        """
        Generates the logs of the ``FunctionLogger`` in the function format.

        Returns
        -------
        str
            The logs of the ``FunctionLogger`` in the function format.

        .. seealso::

            :func:`pydeco.decorators.FunctionLogger.set_log_format()`
        """
        logs = ""
        for function_signature_name in self.extract_loggeg_functions():
            logs += f"[{function_signature_name}]\n"
            for log in self._logged_data:
                if log[1] == function_signature_name:
                    date = log[0]
                    data = log[2]
                    logs += f"\t[{date}]"
                    for data_name, data_value in data.items():
                        log_utils = self._logged_utils[data_name]
                        logs += f" - {log_utils.string_result(data_value)}"
                    logs += "\n"
        return logs

    def generate_logs_cumulative(self) -> str:
        """
        Generates the logs of the ``FunctionLogger`` in the cumulative format.

        Returns
        -------
        str
            The logs of the ``FunctionLogger`` in the cumulative format.

        .. seealso::

            :func:`pydeco.decorators.FunctionLogger.set_log_format()`
        """
        logs = ""
        for function_signature_name in self.extract_loggeg_functions():
            logs += f"[{function_signature_name}]"
            data = {data_name: 0 for data_name in self._logged_utils.keys()}
            calls = 0
            for log in self._logged_data:
                if log[1] == function_signature_name:
                    calls += 1
                    for data_name, data_value in log[2].items():
                        data[data_name] += data_value
            logs += f" - {calls} calls"
            for data_name, data_value in data.items():
                log_utils = self._logged_utils[data_name]
                logs += f" - {log_utils.string_result(data_value)}"
            logs += "\n"
        return logs
    
    def generate_logs(self) -> str:
        """
        Generates the logs of the ``FunctionLogger`` according to the log format.

        Returns
        -------
        str
            The logs of the ``FunctionLogger`` in the specified log format.

        .. seealso::

            :func:`pydeco.decorators.FunctionLogger.set_log_format()`
        """
        if self.log_format == "datetime":
            return self.generate_logs_datetime()
        elif self.log_format == "function":
            return self.generate_logs_function()
        elif self.log_format == "cumulative":
            return self.generate_logs_cumulative()

    def write_logs(self, file_path: str) -> None:
        """
        Writes the logs of the ``FunctionLogger`` in a file at the specified path.

        Parameters
        ----------
        file_path : str
            The path of the file where the logs will be written.
        """
        with open(file_path, "w") as file:
            file.write(self.generate_logs())
                
    def __repr__(self) -> str:
        return self.generate_logs()
    
    def __str__(self) -> str:
        return self.generate_logs()