#practice 1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def describ_person(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

p = Person("Arefeh","35")
p.describ_person()

#practice 2

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(f"This book is {self.title.title()} written by {self.author.title()}.")

b = Book("dollor","arefeh rastegarnejad")
b.describe_book()

#practice 3

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def info(self):
        if self.brand[0].lower() in ['a','e','y','i','o']:
            print(f"This car is an {self.brand.title()} made in {self.year}.")
        else:
            print(f"This car is a {self.brand.title()} made in {self.year}.") 

c1 = Car("Audi","2025")
c1.info()
c2 = Car("benz","1990")
c2.info()

#practice 4

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area(self):
        print(f"Area:{(self.width+self.length)*2}")
    def Perimeter(self):
        print(f"Perimeter:{self.width*self.length}")

r = Rectangle(3,5)
r.area()
r.Perimeter()

#practice 5

class Movie:
    def __init__(self,title,director,year):
        self.title = title
        self.director = director
        self.year = year

    def describe(self):
        print(f"\"{self.title.title()}\", directed by {self.director.title()}, was released in {self.year}.")

m = Movie("inception","christopher nolan","2010")
m.describe()

class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average(self):
        sum_grade = 0
        for i in self.grades:
            sum_grade = sum_grade + i
        avrg = sum_grade / len(self.grades)
        return avrg
    
    def status(self):
        avrg = Student.average(self)
        if avrg > 17:
            print("Excellent")
        elif avrg > 14:
            print("Good")
        else:
            print("Needs Improvement")

s = Student("arefeh",[12,15,20,15,13,16,18,20])
s.average()
s.status()