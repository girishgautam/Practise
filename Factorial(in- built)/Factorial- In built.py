
# In built
# import math
#
# num = int(input('Enter a number: '))
#
# result = math.factorial(num)
#
# print('Factorial of', num, 'is', result)

# Recurion
# def fact(num):
#     if num == 0:
#         return 1
#     else:
#        return num * fact(num-1)
#
# for i in range(6):
#     print('Factorial of', i, 'is', fact(i))

# For loop
def fact (num) :
    sum = 1
    for i in range(1, num + 1):
        if i == 0:
            sum = 1
        if i == 1:
            sum = 1
        else:
            sum = sum * i
    return sum



for i in range(7):
    print('Factorial of', i, 'is', fact(i))
