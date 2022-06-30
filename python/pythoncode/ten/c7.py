
import re
language = 'PythonC#\nJavaPHP'

#4~8

r = re.findall('c#.{1}', language, re.I|re.S)
print(r)