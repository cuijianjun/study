# 边界匹配
import re
qq = '1000000111'
# 4~8
r = re.findall("^\d{4,8}$", qq)
print(r)