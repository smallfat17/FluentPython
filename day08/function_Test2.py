
#类和方法的属性
class Stu: pass
def fun1():pass

print(set(dir(fun1)) - set(dir(Stu))) #{'__call__', '__code__', '__globals__', '__annotations__', '__get__', '__qualname__', '__defaults__', '__name__', '__closure__', '__kwdefaults__'}

from inspect import signature

def fn(a, b='bb', *args, c='cc', **kwargs): pass

sig = signature(fn)
print(sig) #(a, b='bb', *args, c='cc', **kwargs)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

#POSITIONAL_OR_KEYWORD : a = <class 'inspect._empty'>   #形参
#POSITIONAL_OR_KEYWORD : b = bb
#VAR_POSITIONAL : args = <class 'inspect._empty'>       #定位参数元组
#KEYWORD_ONLY : c = cc                                  #关键字参数
#VAR_KEYWORD : kwargs = <class 'inspect._empty'>        #关键字参数字典

def fn2(s1: str, c: str, a: 'int >0'=80) -> int:pass
fn2(1, 2, -1)

print(fn2.__annotations__)  #{'s1': <class 'str'>, 'c': <class 'str'>, 'a': 'int >0', 'return': <class 'int'>}
