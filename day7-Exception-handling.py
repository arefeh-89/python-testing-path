#practice 1
try:
    num1 = int(input("please enter first number:"))
    num2 = int(input("please enter second number:"))
    result = num1/num2
except ZeroDivisionError:
    print("The second number should not be zero!")
except ValueError:
    print("You should enter a number!")
except Exception as ex:
    print("Something is wrong!")
else:
    print(result)
finally:
    print("Finnished!")

