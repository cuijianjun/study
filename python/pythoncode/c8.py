# 主要用来遍历/循环 序列或者集合、字典

a = [['apple', 'orange', 'banana', 'grape'], (1,2,3)]

for X in a:
    for y in X:
        print(y)
else: 
    print('fruit is gone')

A= [1,2,3]

for x in a:
    if x== 2:
        break
    print(x)


for x in a:
    if x== 2:
        continue
    print(x)