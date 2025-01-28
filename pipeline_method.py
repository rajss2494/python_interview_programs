def pipeline(*func):
    def wrapper(arg):
        for f in func:
            arg = f(arg)
        return arg

    return wrapper


pipeline_func = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(pipeline_func(3))
