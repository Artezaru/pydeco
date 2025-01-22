pydeco.decorators
=================

``decorators`` is a sub-module of ``pydeco`` that provides a collection of decorators for use in Python programming.

This sub-module is composed of the following classes:

- ``pydeco.decorators.ProfilerUtils`` class is the base class for the utils decorators profiling functions and methods.
- ``pydeco.decorators.Timer`` and ``pydeco.decorators.Memory`` are utils decorators that measure the runtime and memory usage of a function or a method.
- ``pydeco.decorators.FunctionProfiler`` is a decorator using the utils decorators to profile functions and methods and reporting the results as logs.

.. toctree::
    :maxdepth: 1
    :caption: pydeco.decorators API:

    ./implemented_decorators/profiler_utils.rst
    ./implemented_decorators/timer.rst
    ./implemented_decorators/memory.rst
    ./implemented_decorators/function_profiler.rst

The user guide for the implemented decorators is available in the section :doc:`./implemented_decorators`.

