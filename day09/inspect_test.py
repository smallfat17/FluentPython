import functions
import inspect

funs = [func for func in inspect.getmembers(functions, inspect.isfunction)]
# print(funs[0](1, 2))
print(funs)