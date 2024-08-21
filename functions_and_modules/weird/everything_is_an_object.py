import my_math
from inspect import getmembers, isfunction

for member in dir(my_math):
    if isfunction(getattr(my_math, member)):
        my_math_function = getattr(my_math, member)
        print("name is {}".format(my_math_function.__name__))
        print("documentation is {}".format(my_math_function.__doc__))
        print("code is {}".format(my_math_function.__code__))
        print("number of local variables of {} are {}".format(my_math_function.__name__, my_math_function.__code__.co_nlocals))
        print("names of arguments and local variables of {} are {}\n".format(my_math_function.__name__, my_math_function.__code__.co_varnames))
