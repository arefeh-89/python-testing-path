#practice 1
with open("notes.txt","w") as file:
    file.write("Python is fun.\nLearning step by step.\nFiles are easy!")

#practice 2
with open("notes.txt","r") as file:
    for line in file.readlines():
        print(line.strip())

#practice 3
name = input("please tell me your name:")
with open("users.txt","a") as file:
    file.write(f"{name}\n")