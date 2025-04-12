#practice 1
def num_condition():
    num = int(input("enter a number:"))
    if num > 0:
        print("این یه عدد مثبته!")
    elif num == 0 :
        print("اینکه عدد صفره!")
    else:
        print("این یه عدد منفیه!")

num_condition()

#practice 2
def define_score():
    score = int(input("Enter your score:"))
    if score > 90:
        print("A")
    elif score >70:
        print("B")
    elif score > 50:
        print("C")
    else:
        print("F")

define_score()

#practice 3
sum_nums = 0
for x in range(1,101):
    if x % 2 == 0:
        sum_nums = sum_nums + x
print(f"The total number is {sum_nums}")

#practice 4
def multi_x():
    number = int(input("please give me a number:"))
    for i in range(1,11):
        multiply = i * number
        print(f"{number} * {i} = {multiply}")

multi_x()

#practice 5
password = "python123"
rand = 0
while rand == 0:
    entered_pass = input("please enter the password:")
    if entered_pass == password:
        print("رمز درست وارد شد!")
        rand = 1

#practice 6
def define_min(list):
    minimum = list[0]
    for i in list:
        if i < minimum:
            minimum = i
    print(f"The minimum number of the list is {minimum}")

define_min([43,5,2,8,534,23,63])