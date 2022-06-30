import re

a = 'C|C++|Java|Python'

r = re.findall('Python', a)
if len(r) > 0:
    print('字符串中包含Python')
print(r)

 