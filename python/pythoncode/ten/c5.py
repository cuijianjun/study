# 数量词
# *匹配0次或者无限次
# + 匹配1次或者无限次
# ？ 匹配0次或者1次 
import re
a= 'pytho0python1pythonn2'

# r = re.findall('python*', a)
r = re.findall('python+', a)

print(r)