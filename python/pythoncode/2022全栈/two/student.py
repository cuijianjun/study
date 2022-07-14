"""
    学生信息库
"""

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
print(max(student))

def check_user_info(**kwargs):
    if 'name' not in kwargs:
        return  '没有发现学生姓名'
    if 'age' not in kwargs:
        return '没有发现学生年龄'
    if 'sex' not in kwargs:
        return '没有发现学生性别'
    if 'class_number' not in kwargs:
        return  '没有发现学生学号'
    return True


def get_all_students():
    for id_,value in student.items():
        print('学号：{},姓名:{} ,年龄:{}, 性别:{}, 班级{}'.format(
            id_,value['name'],value['age'],value['sex'],value['class_number']
        ))
    return student

# get_all_students()

def add_student(**kwargs):
    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    
    id_ = max(student) + 1

    student[id_] = {
        'name': kwargs['name'],
        'age': kwargs['age'],
        'sex': kwargs['sex'],
        'class_name': kwargs['class_name']
    }

add_student(name='小白', age=19,class_number='A', sex='boy')

def delete_student(student_id):
    if student_id not in student:
        print('{}并不存在'.format(student_id))
    else:
        user_info = student.pop(student_id)
        print('学号是{},{}同学的信息已经删除'.format(student_id, user_info))

def update_student(student_id, **kwargs):
    if student_id in student:
        print('并不存在这个学号:{}'.format(student_id))
    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    student[student_id] = kwargs
    print('同学信息更新完毕')

update_student(1, name='dewei.zhang',age=33, class_number="A", sex='boy')


