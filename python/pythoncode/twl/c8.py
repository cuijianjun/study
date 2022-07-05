import time

def decorator(func):
    def wrapper(*args, **kwargs):
        print(time.time())
        func(*args, **kwargs)
    return wrapper


@decorator
def f1():
    print('This is a function')
@decorator
def f3(func_name1, function2, **kw):
    print('This is a function')
    print(kw)
f1()
f3('test func1', 'test func2', a = 1,b = 2, c = '333')
f = decorator(f1)
f()
