from dataclass import dataclass

@dataclass
class Student():
    name: str
    age: int
    school_name: str
    # def __init__(self,name,age,school_name):
    #     self.name = name
    def test(self):
        print(self.name)
student = Student('7yue', 18, 'Tsinghua')
print(student.__reduce_ex__())
    