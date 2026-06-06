q=[{"name":"zmy","age":18,"number":1},{"name":"zl","age":19,"number":2},
{"name":"sx","age":20,"number":2},{"name":"ls","age":21,"number":1},
   {"name":"ww","age":22,"number":2},{"name":"el","age":23,"number":1}]
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)


class BoyStudent(Student):
    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number=number

    def show(self):
        super().show()
        print(self.number,"男生")

class GirlStudent(Student):
    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number=number

    def show(self):
        super().show()
        print(self.number,"女生")
Student_map={1:BoyStudent,2:GirlStudent}
for i in q:
    sc=Student_map[i["number"]]
    b=sc(i["name"],i["age"],i["number"])
    b.show()


