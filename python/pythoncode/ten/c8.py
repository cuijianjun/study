import re

s = 'life is short, i use python'
#None
r = re.findall('life(.*)python', s)
print(r)