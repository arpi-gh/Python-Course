'''Write a program that allows the user to enter five numbers (read as strings).
Create a string that consists of the user’s numbers separated by plus signs.
For instance, if the user enters 2, 5, 11, 33, and 55,
then the string should be ‘2+5+11+33+55’.'''

# res_str = ''
# for i in range(5):
#     inp = str(input('Enter number:'))
#     res_str += inp
#     if i != 4:
#         res_str += '+'
# print(res_str)

'''Write a program that gets a string from the user containing a potential telephone number. 
The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. 
A phone number is considered valid as long as it is written in the form abc-def-hijk
or 1-abc-def-hijk. The dashes must be included, the phone number should contain only numbers and dashes, 
and the number of digits in each group must be correct.'''

# phone_num = str(input("Enter your phone number: "))
# if phone_num[0:3].isdigit() and phone_num[4:7].isdigit() and phone_num[8:].isdigit():
#     if phone_num[3] == '-' and phone_num[7] == '-':
#         print('valid')
#     else:
#         print('invalid')
# elif phone_num[0] == '1' and phone_num[2:5].isdigit() and phone_num[6:9].isdigit() and phone_num[10:].isdigit():
#     if phone_num[1] == '-' and phone_num[5] == '-' and phone_num[9] == '-':
#         print('valid')
#     else:
#         print('invalid')
# else:
#     print('invalid')


'''Write a program that implements the Caesar cipher, 
a simple encryption technique where each letter in the plaintext is shifted 
a certain number of places down the alphabet'''

# txt = str(input("Enter  text: "))
# shift = int(input('Enter shift: '))
# encoded = txt.encode()
# encoded_txt = bytearray(encoded)
# for char in range(len(encoded_txt)):
#     encoded_txt[char] += shift
# decoded = encoded_txt.decode()
# decoded_txt = str(decoded)
# print(decoded_txt)

'''Write a program that calculates the Fibonacci sequence. '''
# num1 = 0
# num2 = 1
# limit = int(input('Enter limit: '))
# print(num1, num2, end=' ')
# Flag = True
# while Flag:
#     next_num = num1 + num2
#     if next_num <= limit:
#         print(next_num, end=' ')
#     else:
#         Flag = False
#     num1 = num2
#     num2 = next_num

'''Write a program that accepts a string from the user and removes all duplicates. 
The resulting string should contain only unique characters.'''
# doesn't work for characters that are far from each other
# line = str(input("Enter a string: "))
# for l in range(len(line) - 2):
#     if line[l+1] == line[l]:
#         line = line[0:l+1] + line[l+2:]
#         l += 1
# print(line)
line = str(input("Enter a string: "))
ls = []
for l in line:
    if l not in ls:
        ls.append(l)
print(''.join(ls))


