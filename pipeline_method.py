"""As part of a data processing pipeline, complete the implementation of the pipeline method:

    The pipeline method should accept a variable number of functions and
    return a new function that accepts one parameter (arg). The returned
    function should call the first function in pipeline with the parameter
    arg, then call the second function in pipeline with the result of the
    first function. The returned function should continue calling each
    function in pipeline in order, following the same pattern, and return
    the value from the last function.

    pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
    Then calling the returned function with 3:

    resuShould return: 5

"""

def pipeline(*func):
    def wrapper(arg):
        for f in func:
            arg = f(arg)
        return arg

    return wrapper


pipeline_func = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(pipeline_func(3))
