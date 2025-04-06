#practice 1:
user = {"name" : "Arefeh" , "age" : 35 , "city" : "Tehran" , "job" : "Software tester"}
print(user["job"])

#practice 2:
user.update({"maried" : True})
user.pop("city")

#practice 3:
grades = {
    "Ali": 18,
    "Sara": 20,
    "Mehdi": 16
}
for x in grades:
    print(f'{x} : {grades[x]}')

#practice 4:
if "Ashkan" in x:
    print(f'Ashkan grade is {grades["Ashkan"]}')
else:
    print("Not Found")

#practice 5:
books = [
    {"title": "Book A", "author": "Author 1", "year": 2020},
    {"title": "Book B", "author": "Author 2", "year": 2018},
    {"title": "Book C", "author": "Author 3", "year": 2023}
]
for book in books:
    print(book["title"])