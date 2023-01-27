# # Write a program that asks the user to enter a number,
# # checks, and prints whether the number is even or odd.
# num = int(input('Enter number:'))
# if num % 2 == 0:
#     print("The number you entered is even.")
# else:
#     print("The number you entered is odd.")
#
# # Write a program that asks the user to enter a character,
# # checks, and prints whether the character is a consonant or a vowel.
#
# char = str(input('Enter a character:'))
# if char == 'a'or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#     print("You have entered a vowel")
# else:
#     print("You have entered a consonant")
#
#
# # Write a program that asks the user to enter n number
# # and prints the n-th Fibonacci number.
# num = int(input('Enter number:'))
# n = 2
# first = 0
# second = 1
# fib_n = 1
# if num == 0:
#     print(first)
# elif num == 1:
#     print(second)
# else:
#     while n != num + 1:
#         fib_n = first + second
#         first = second
#         second = fib_n
#         n += 1
#     print(fib_n)
#
# # Write a program that asks the user to enter a number
# # and prints the sum of its digits on the screen.
#
# num = int(input("Enter number: "))
# digit_sum = 0
# digit = 0
# while num != 0:
#     digit = num % 10
#     digit_sum += digit
#     num //= 10
# print(digit_sum)
#
# # Write program that prints the following image on the screen. Use cycles.
# height = int(input("Enter height:"))
# width = int(input("Enter width:"))
# border = '* ' * width
# print(border)
# for i in range(0, height + 1):
#     print('* ','  ' * (width-3), '* ')
# print(border)
