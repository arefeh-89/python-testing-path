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