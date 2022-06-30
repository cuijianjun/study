import re

a = 'C|C++|Ja23va|Python333232'

r = re.findall('\d', a)
print(r)