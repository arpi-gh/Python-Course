def case_change(word, i):
    if i == 0:
        word = word[i].upper() + word[i + 1:]
    elif i == len(word) - 1:
        word = word[0:i] + word[i].upper()
    else:
        word = word[0:i] + word[i].upper() + word[i + 1:]
    word.lower()
    return word


# W = str(input('Enter word: '))
# output = []
# for i in range(len(W)):
#     output.append(case_change(W, i))
# print(output)


def compare_str(s1, s2):
    if s1 == s2:
        return 0
    elif len(s1) != len(s2):
        return -1
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s2[i]


# str1 = input('Enter word 1: ')
# str2 = input('Enter word 2: ')
# output = compare_str(str1, str2)
# print(output)


def strStr(word1, word2):
    found = False
    index = None
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] != word2[j]:
                found = False
                break
            else:
                if not found:
                    index = i
                found = True
    return index


# str1 = input('Enter word 1: ')
# str2 = input('Enter word 2: ')
# output = (strStr(str1, str2))
# print(output)

'''4.Իրականացնել strMove(string, number, bool) ֆունկցիան, ստանում է տող, 
թիվ և բուլյան արժեք։ Եթե վերջինս True է, տողը տեղաշարժվում է աջ տրված թվի չափով, եթե False՝ ձախ։
Օրինակ՝ string = “Hello”, number = 2, bool = True, Output: loHel'''


def strMove(string, number, boolean):
    if boolean:
        if number < 0:
            number = abs(number)
        if number != 0:
            string = string[number:] + string[0:number + 1]
    return string


# st = input('Enter a string: ')
# move = bool(input('Do you want to shift the string? True/False: '))
# num = int(input('By how many bits?:  '))
# print(strMove(st, num, move))

'''5.Տրված է սորտավորված լիստ և մեկ կամայական թիվ։ Գրել ֆունկցիա, որը կվերադարձնի այդ թվի ինդեքսը լիստում, 
եթե այն առկա է, հակառակ դեպքում այն ինդեքսը, որտեղ որ կլիներ այդ թիվը, եթե պարունակվեր լիստում։'''


def where_is_num(ls, num):
    if num in ls:
        return ls.index(num)
    if num < ls[0]:
        return 0
    for i in range(len(ls)):
        if ls[i] < num < ls[i + 1]:
            return i + 1


# l = [int(N) for N in input('Enter a space-separated number list: ').split()]
# l.sort()
# target = int(input('Enter a number: '))
# print(l)
# print(where_is_num(l, target))

'''6.Գրել ծրագիր, որը կստանա երկու թիվ՝ m(rows) և n(columns), 
և կգեներացնի երկչափ զանգված(մատրից)։ i-րդ տողի j-րդ սյունակի էլեմենտը պետք է լինի i*j։ 
Փորձեք խնդիրը լուծել՝ օգտագործելով list comprehension:'''


def matrix_ij(m, n):
    # mat = []
    # for i in range(m):
    #     mat.append([])
    #     for j in range(n):
    #         mat[i].append(int(i*j))
    mat = [[int(i * j) for j in range(n)] for i in range(m)]
    return mat


'''rows = 4
columns = 5
print(matrix_ij(rows, columns))'''

'''7.Գրել ծրագիր, որը ստուգում է՝ տրված գաղտնաբառը վավեր է, թե ոչ։ Գաղտնաբառը վավեր է, եթե պարունակում է.
Առնվազն մեկ մեծատառ
Առնվազն մեկ թվանշան
Առնվազն մեկ նշան այս ցուցակից՝ [$#@]
Ամենաքիչը 6 նիշ
Ամենաշատը 16 նիշ
'''


def password_correct(password):
    if 6 <= len(password) <= 16:
        if '$' in password or '#' in password or '@' in password:
            if any(c.isupper() for c in password) and any(c.islower() for c in password):
                if any(c.isdigit() for c in password):
                    return True
                else:
                    print('Password must contain at least one digit!')
            else:
                print('Password must contain at least one uppercase and one lowercase letter!')
        else:
            print('Password must contain at least one of the following characters!: $ # @')
    else:
        print('Password must be between 6 and 16 characters long!')
    return False


'''user_pass = input('Enter a secure password: ')
correct = False
while not correct:
    if password_correct(user_pass):
        print('You\'re all set up!')
        correct = True
    else:
        user_pass = input('Try again!: ')'''

