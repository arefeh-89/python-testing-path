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

#practice 2
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print(f"The brand is {self.brand.title()} and it's model is {self.model}.")

class Car(Vehicle):
    def __init__(self,brand,model,num_doors):
        super().__init__(brand,model)
        self.num_doors = num_doors

    def info(self):
        super().info()
        print(f"This car has {self.num_doors} doors.")

c = Car("benz","2020",4).info()

#practice 3

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size

    def show_details(self):
        print(f"The employee name is {self.name.title()} and salary is {self.salary}.")
        print(f"her team is included {self.team_size} members!")

m = Manager("baran","3000 $",5)
m.show_details()

#practice 4
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"It's {self.name.title()} and she is {self.age} years old.")

class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.salary = salary

    def info(self):
        super().info()
        print(f"The employee id is {self.employee_id} and salary is {self.salary}.")

class Developer(Employee):
    def __init__(self,name,age,salary,employee_id,language):
        super().__init__(name,age,salary,employee_id)
        self.language = language

    def show_detail(self):
        super().info()
        print(f"She is a {self.language} developer!")

d = Developer("arefeh",35,"5000 $",4355,"Python")
d.show_detail()