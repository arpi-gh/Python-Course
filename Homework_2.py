import math
import random

'''Write a program that generates and
prints 50 random integers, each between 3 and 6. '''
# for i  in range(50):
#     random.randint(3,6) #prints each one on a new line
#
# for i in range(50):
#     num = random.randint(3,6)
#     print(num, end=', ') #separates the numbers by a comma when printing

'''Write a program that asks the user to enter two numbers, x and y ,
and computes | x − y | /  x + y '''
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# dif = x - y
# print(abs(dif)  /  (x + y))

'''Write a program that checks if a string is a palindrome.'''
# user_str = str(input("Enter a string: "))
# if user_str[-1::-1] == user_str:
#     print("palindrome")
# else:
#     print("not a palindrome")

'''Write a program that takes a list of numbers
and calculates the sum of its elements.'''
# ls = [int(num) for num in input("Enter space-separated numbers: ").split()]
# sum = 0
# for num in ls:
#     sum += num
# print(sum)

'''Write a program that takes a list of numbers
and returns the largest number in the list.'''
# ls = [int(num) for num in input("Enter space-separated numbers: ").split()]
# print(max(ls)) #the easiest way
# #using a for loop
# largest_num = 0
# for i in range(len(ls)):
#     if ls[i] > largest_num:
#         largest_num = ls[i]
# print(largest_num)

'''Write a program that reverses a string. '''
# usr_str = str(input("Enter a string: "))
# print(str[::-1])
'''Write a program that calculates the area of a circle given its radius.'''
# radius = float(input("Radius: "))
# area = 2 * math.pi * radius
# print(area)
