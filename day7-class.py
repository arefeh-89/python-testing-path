#practice 1
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"The client name is {self.name.title()} and the age is {self.age}")

class Employee(Person):
    def __init__(self,job_title):
        self.job_title = job_title

    def job(self):
        print(f"{self.name.title()}'s job is {self.job_title}")

p = Person("azadeh", 30)
p.introduce()
e = Employee("engineer")
e.job()