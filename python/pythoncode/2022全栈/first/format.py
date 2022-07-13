info= 'my name is %s, my age is %s'

name='frank'
age=22

print(info % (name, age))

info= 'my name is {0}, my age is {1}'
print(info.format(name, age))

print(f'this is {name}')
