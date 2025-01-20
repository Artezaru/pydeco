# HOW TO CREATE A DECORATOR and HOW TO USE A DECORATOR examples


#####
print("\n\nCreating a decorator")
from pydeco import Decorator

class PrintFunctionName(Decorator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def _wrapper(self, func, *args, **kwargs):
        print(f"Function name: {self.get_signature_name(func)}")
        outputs = func(*args, **kwargs)
        return outputs



#####
print("\n\nUsing the decorator")
print_deco = PrintFunctionName(activated=True, signature_name_format='{name}')

@print_deco
def my_function():
    print("Hello world!")

my_function()




#####
print("\n\nDeactivating the decorator")
@print_deco
def my_function():
    print("Hello world!")

my_function()  # The decorator is activated
print_deco.set_activated(False)
my_function()  # The decorator is deactivated
print_deco.set_activated(True)
my_function()  # The decorator is activated




#####
print("\n\nDecorating methods")
class MyClass:
    @print_deco
    def my_method(self):
        print("Hello world! (1)")

    @print_deco
    def my_second_method(self):
        print("Hello world! (2)")

    def my_third_method(self):
        print("Hello world! (3)")

my_class = MyClass()
my_class.my_method()
my_class.my_second_method()
my_class.my_third_method()




#####
print("\n\nClass propagate")
from pydeco import class_propagate

@class_propagate(print_deco, methods=['my_method', 'my_second_method'])
class MyClass:
    def my_method(self):
        print("Hello world! (1)")

    def my_second_method(self):
        print("Hello world! (2)")

    def my_third_method(self):
        print("Hello world! (3)")

my_class = MyClass()
my_class.my_method()
my_class.my_second_method()
my_class.my_third_method()






#####
print("\n\nName signature issue")
class MyClass:
    @print_deco
    def my_function(self):
        print("Hello world! (1)")

class MyOtherClass:
    @print_deco
    def my_function(self):
        print("Hello world! (2)")

my_class = MyClass()
my_class.my_function()
my_other_class = MyOtherClass()
my_other_class.my_function()










#####
print("\n\nSolving the name signature issue")
print_deco.set_signature_name_format('{qualname}')

class MyClass:
    @print_deco
    def my_function(self):
        print("Hello world! (1)")

class MyOtherClass:
    @print_deco
    def my_function(self):
        print("Hello world! (2)")

my_class = MyClass()
my_class.my_function()
my_other_class = MyOtherClass()
my_other_class.my_function()