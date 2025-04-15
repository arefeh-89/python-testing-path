#practice 1
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"The client name is {self.name.title()} and the age is {self.age}")

class Employee(Person):
    def __init__(self,job_title,name,age):
        super().__init__(name,age)
        self.job_title = job_title

    def job(self):
        super().introduce()
        print(f"{self.name.title()}'s job is {self.job_title}")

e = Employee("engineer","azadeh", 30)
e.job()