def city_temp(**param):
    for key,value in param.items():
        print(key, ':', value)

city_temp(bj='32c', xm="23C", sh="31C")

a = {'bj': '32C', 'xm': '23C'}
city_temp(**a)