"""
    学生信息库
"""

from re import A

class StudentInfo(object):
    def __init__(self, students):
        self.students = students
    def get_all_students(self):
        for id_,value in self.students.items():
            print('学号：{},姓名:{} ,年龄:{}, 性别:{}, 班级{}'.format(
                id_,value['name'],value['age'],value['sex'],value['class_number']
            ))
        return student
    
    def get_user_by_id(self, id):
        return self.students.get(id)
    def add_student(self, **kwargs):
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        
        id_ = max(self.students) + 1

        self.students[id_] = {
            'name': kwargs['name'],
            'age': kwargs['age'],
            'sex': kwargs['sex'],
            'class_name': kwargs['class_name']
        }
    
    def adds(self, new_students):
        for student in new_students:
            check = self.check_user_info(**student)
            if check != True:
                print(check, student.get('name'))
                continue
            self.__add(**student)
    def __add(self, **student):
        new_id = max(self.students) + 1
        self.students[new_id] = student
    
    def delete_student(self, student_id):
        if student_id not in self.students:
            print('{}并不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('学号是{},{}同学的信息已经删除'.format(student_id, user_info))

    def update_student(self, student_id, **kwargs):
        if student_id in self.students:
            print('并不存在这个学号:{}'.format(student_id))
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.students[student_id] = kwargs
        print('同学信息更新完毕')
    def check_user_info(self, **kwargs):
        if 'name' not in kwargs:
            return  '没有发现学生姓名'
        if 'age' not in kwargs:
            return '没有发现学生年龄'
        if 'sex' not in kwargs:
            return '没有发现学生性别'
        if 'class_number' not in kwargs:
            return  '没有发现学生学号'
        return True


student = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
    },
    2: {
        'name': 'xiaomu',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
    },
    3: {
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'gril'
    },
    4: {
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'boy'
    },
    5: {
        'name': '小云',
        'age': 18,
        'class_number': 'B',
        'sex': 'gril'
    },
}

student_info = StudentInfo(student)
user = student_info.get_user_by_id(1)
print(user)
