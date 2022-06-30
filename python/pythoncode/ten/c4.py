#概括字符集

# \d \D
# \w 单次字符 \W 非单次字符
import re

s = 'pyhton2 3 &\n23\r4234php'

# r = re.findall('[0-9]', s)
r = re.findall('[a-z]{3,6}?', s)
print(r)