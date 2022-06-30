from c3 import Human
# 面向对象
class Student(Human):
    sum = 0
    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name,age)
        self.name = name
        self.age = age
        self.__score = age # 私有变量
        self.__class__.sum += 1
        print('student')
    def do_homework(self):
        print('english homework')

student1 = Student()
print(student1.sum)
print(Student.sum)
print(student1.name)
print(student1.age)


