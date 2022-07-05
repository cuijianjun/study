# 装饰器
import time

def f1():
    print(time.time())
    print('This is a funciton')
f1()

# 开闭原则

def f2():
    print('this is a function')

def print_current_time(func):
    print(time.time())
    func()