class student():

    def  __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def show(self):
        print(f'student about: {self.name}\n surname: {self.surname}\n age {self.age}')

student1 = student('ali', 'aliyev', 12)
student1.show()

class teacher(student):
    
    def __init__(self, name, surname, age, position):
    
        self.position = position
        super().__init__(name, surname, age)
    
    def show(self):
        print(f'teacher about: {self.name}\n surname: {self.surname}\n age: {self.age}\n position: {self.position}')

teacher1 = teacher('cemil','huseynzade',22,'teacher')

teacher1.show()