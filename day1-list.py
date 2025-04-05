#practice 1:
random_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = [num for num in random_numbers if num % 2 == 0]
print(even_numbers)

#practice 2:
names = ["Arefeh","Ashkan","Sara","Reza","Ali"]
print([name for name in names if name[0]=="A"])
print(len([name for name in names if len(name) > 5]))

#practice 3:
a = [1,2,3]
b = [4,5,6]
c = a.copy()
for x in b:
    c.append(x)
c.reverse()
print(c)

#practice 4:
nums = [1,2,2,3,4,4,5,1]
new_nums = []
[new_nums.append(num) for num in nums if num not in new_nums]    
print(new_nums)

#practice 5:
scores = [
    [10, 15, 20],
    [5, 8, 12],
    [7, 14, 21]
]
averages = []
i = 0
while i < len(scores):
    sum = 0
    for x in scores[i]:
        sum = sum + x
    average = sum/len(scores[i])
    averages.append(average)
    i += 1
print(averages)
total_ave = 0
for ave in averages:
    total_ave = total_ave + ave
total_ave = total_ave / len(averages)
print(total_ave)

