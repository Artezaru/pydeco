from pydeco.decorators import Timer

timer = Timer(activated=True, signature_name_format='{name}')

@timer
def example_function():
    import time
    print("Hello")
    time.sleep(70)

example_function()
