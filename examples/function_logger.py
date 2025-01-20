from pydeco.decorators import FunctionLogger
from pydeco.decorators import Timer, Memory

function_logger = FunctionLogger(
    activated=True,
    signature_name_format='{name}',
    logger_utils=[Timer, Memory],
    log_format='cumulative')

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

print(function_logger)