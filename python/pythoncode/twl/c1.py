#map 

list_x = [1,2,3,4,5,6]
list_y = [1,4,9,16,25,36]

r = map(lambda x: x*x, list_x)
print(list(r))


#map 多参数
list_x = [1,2,3,4,5,6]
list_y = [1,4,9,16,25,36]

r = map(lambda x,y: x*x + y, list_x, list_y)
print(list(r))

