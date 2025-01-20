from pydeco.decorators import Memory

memory = Memory(activated=True, signature_name_format='{name}')

@memory
def example_function():
    return [i for i in range(1000000)]

bigdata = example_function()

