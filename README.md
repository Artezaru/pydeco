# pydeco

## Description
Python Decorators for functions and methods 

## Author
- Name: Artezaru
- Email: artezaru.github@proton.me
- GitHub: [Artezaru](https://github.com/Artezaru/pydeco.git)

## Installation

Install with pip

```
pip install git+https://github.com/Artezaru/pydeco.git
```

Clone with git

```
git clone https://github.com/Artezaru/pydeco.git
```

## Documentation

Generate the documentation with sphinx
1. Install the sphinx package and the pydata-sphinx-theme

```
pip install sphinx
pip install pydata-sphinx-theme
```

2. Generate the documentation

```
make html
```

3. Open the documentation in a web browser

```
open build/html/index.html
```

## Usage

More details in the documentation.

pydeco provides a number of decorators that can be used to modify the behavior of functions.
You can also create your own decorators.

To use a decorator of pydeco, first import the decorator you want to use and create an instance of it.

``` python
from pydeco.decorators import Logger
logger = Logger()
```

Next, you can use the decorator by adding it to the function you want to decorate.

``` python
@logger
def my_function():
    print('Hello, world!')
```

If you want to decorate a method of a class, you can use the decorator in the same way.
But a better way to decorate a method of a class is to use the ``class_propagate`` function of pydeco.

``` python
from pydeco import class_propagate

@class_propagate(logger, methods=['my_method'])
class MyClass:

    def my_method(self):
        print('Hello, world!')

    def my_other_method(self):
        print('Goodbye, world!')
```

For the logger, you can get the log of your script:
``` python
print(logger.details_repr)
```
```
Logger(
[{func_name}] number of calls : {Ncalls} - cumulative runtime : {hours}h {minutes}m {seconds}s
        [{date}] runtime : {hours}h {minutes}m {seconds}s
        [{date}] runtime : {hours}h {minutes}m {seconds}s
        [{date}] runtime : {hours}h {minutes}m {seconds}s
[{func_name}] number of calls : {Ncalls} - cumulative runtime : {hours}h {minutes}m {seconds}s
        [{date}] runtime : {hours}h {minutes}m {seconds}s
        [{date}] runtime : {hours}h {minutes}m {seconds}s
        [{date}] runtime : {hours}h {minutes}m {seconds}s
-----------
total number of calls : {total_runcall}
total runtime : {total_runtime_hours}h {total_runtime_minutes}m {total_runtime_seconds}s
)
```


## License
See LICENSE
