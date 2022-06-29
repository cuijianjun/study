# import sys
# 修改递归最大限制
# sys.setrecursionlimit(100000)

def add(x, y):
    result = x + y
    return result

def print_code(code):
    print(code)

a = add(1,2)

b = print_code('Python') 

print(a, b)