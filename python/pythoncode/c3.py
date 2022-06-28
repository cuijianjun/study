"""
    这是一段小程序
"""
ACCOUNT = 'qiyue'
PASSWORD = '123456'

print('please input account')

USER_ACCENT = input()

print('please input password')

USER_PASSWORD = input()

if ACCOUNT == USER_ACCENT and PASSWORD == USER_PASSWORD:
    print('success')
else:
    print('fail')
