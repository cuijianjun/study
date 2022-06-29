# 面向对象
class Student():
    name = ''
    age = 0
    sum = 0
    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age
        print('student')
    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(name)
    @staticmethod
    def add(x,y):
        print(name)

student = Student('石敢当', 19)
print(student.name)
print(student.age) 
