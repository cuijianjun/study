import sys
import datetime
import io

print(sys.path)

import t
print(t.sys.path)
# 包和模块是不会被重复导入的
# 包不要循环引用
