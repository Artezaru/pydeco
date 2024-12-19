import time 
from ..decorator import Decorator

class Timer(Decorator):
    """
    Compute the runtime of various functions. 

    .. warning::
        If 2 functions/methods have the same 'name', the Timer will combined the two runtimes. 
        Set the format_name attribute to solve this issue. 

    .. seealso:: :class:`pydeco.Decorator`

    Parameters
    ----------
        activated: bool
            If True, the timer is activated. Default is True.
        
        format_name: str
            The timer will format the name of the functions. Default is "{name}". (See :class:`pydeco.Decorator`)

    Methods
    ----------
        initialize()
            Sets the timer to 0 for each functions.

    How to Use
    ----------
    
    Create a timer with :

    .. code-block:: python

        timer = Timer()

    Then decorate functions with the timer. 

    .. code-block:: python

        @timer
        def func_name():
            pass

    Initialize and clear the timer with : 

    .. code-block:: python

        timer.initialize()

    Use the functions and the timer will compute runtimes.

    To deactivate and re-activate the timer, use :

    .. code-block:: python

        timer.set_activated()
        timer.set_deactivated()

    Print the runtimes with :
    
    .. code-block:: python

        print(timer.name_repr) # equivalent of print(timer)

    The result will be :
    
    .. code-block:: console
    
        Timer(
        [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
        [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
        [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
        [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
        -----------
        total runtime : {total_runtime_hours}h {total_runtime_minutes}m {total_runtime_seconds}s
        )
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize()

    @property
    def total_runtime(self) -> float:
        """
        Returns the total runtime in seconds.
        """
        return sum(self._timer[func_name] for func_name in self._timer.keys())

    def initialize(self) -> None:
        """
        Sets the timer to 0 for each functions.
        """
        self._timer = {} # key: str = function name // value: float = runtime

    def __repr__(self) -> str:
        """
        Returns the string representation.
        Default = self.name_repr
        """
        return self.name_repr

    def _wrapper(self, func, *args, **kwargs):
        """
        Runs the function with runtime measurement.
        """
        func_name = self._get_func_name(func)
        # Adding the name into the dictionnary.
        if func_name not in self._timer.keys():
            self._timer[func_name] = 0
        # Runtime measurement.
        tic = time.time()
        outputs = func(*args, **kwargs)
        toc = time.time()
        self._timer[func_name] += toc - tic
        # Return outputs of func.
        return outputs

    @property
    def name_repr(self) -> str:
        """
        Returns the string representation in the following format:

        .. code-block:: console

            Timer(
            [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
            [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
            [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
            [{func_name}] cumulative runtime : {hours}h {minutes}m {seconds}s
            -----------
            total runtime : {total_runtime_hours}h {total_runtime_minutes}m {total_runtime_seconds}s
            )
        """
        string = "Timer(\n"
        for func_name in self._timer.keys():
            # Conversion in hours, minutes, seconds.
            hours, remainder = divmod(self._timer[func_name], 3600)
            minutes, seconds = divmod(remainder, 60)
            string += f"[{func_name}] cumulative runtime : {int(hours)}h {int(minutes)}m {seconds:.4f}s\n"
        # Adding total runtime.
        hours, remainder = divmod(self.total_runtime, 3600)
        minutes, seconds = divmod(remainder, 60)
        string += f"-----------\ntotal runtime : {int(hours)}h {int(minutes)}m {seconds:.4f}s\n)"
        return string