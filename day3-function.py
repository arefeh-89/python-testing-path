#practice 1
def sum_num(a,b):
    return a+b
print(sum_num(4,7))

#practice 2
def even_odd(n):
    if n%2 == 0:
        print("The number is an even number")
    else:
        print("It's an odd number")

even_odd(253)

#practice 3
def avg(my_list):
    sum_num = 0
    for i in my_list:
        sum_num = sum_num + i
    return sum_num/len(my_list)

print(avg([43,23,645,34,53,967]))

#practice 4
def is_palindrome(my_string):
    string = my_string.lower().replace(' ','')
    reverse_string = string[::-1]
    if string == reverse_string:
        print("The provided string is palindrome")

is_palindrome("dad")