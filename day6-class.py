#practice 1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def describ_person(name,age):
        print(f"Hello, my name is {name} and I'm {age} years old.")

Person.describ_person("Arefeh","35")

#practice 2

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def describe_book(title,author):
        print(f"This book is {title.title()} written by {author.title()}")

Book.describe_book("dollor","arefeh rastegarnejad")