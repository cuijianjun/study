from datetime import datetime

now = datetime.now()
print(now, type(now))
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str, type(now_str))

