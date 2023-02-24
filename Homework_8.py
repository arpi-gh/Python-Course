'''Տրված է list, որը պարունակում է 1-ից n ամբողջ թվերը(1-ը ներառյալ)։
Գրել ֆունկցիա, որը որպես պարամետր կստանա այդ list-ը և կգտնի բացակայող թիվը։
Բացակայող թիվ չգտնելու դեպքում վերադարձնել None։'''
def missing_number(list):
    for i in range(len(list)):
        if list[i+1] != list[i] + 1:
            return list[i] + 1


'''ls = [int(n) for n in input('Enter space-separated list of numbers:').split()]
missing = missing_number(ls)
if missing != None:
    print('The missing number is: ', missing)
else:
    print('The list is complete')'''


'''Իրականացնել ֆունկցիա (add_exictment), որը որպես պարամետր կստանա string-երից բաղկացած list և կավելացնի բացականչական նշան (!) 
յուրաքանչյուր string-ի վերջում։ Ծրագիրը պետք է փոփոխի սկզբնական list-ը և ոչինչ չվերադարձնի։ '''
def add_excitement(list):
    for i in range(len(list)):
        list[i] += '!'
'''
ls = [str(l) for l in input("Enter '/' - separated list of strings: ") .split('/')]
add_excitement(ls)
for l in ls:
    print(l)
'''

'''Գրել sum_digits անունով ֆունկցիա, որը վերադարձնում է իրեն փոխանցված ամբողջ թվի թվանշանների գումարը:'''
def sum_digits(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return sum

'''n = int(input('Enter number: '))
print('The sum of the digits is: ', sum_digits(n))'''

'''Գրել is_sorted անունով ֆունկցիա, որը որպես պարամետր կստանա list և կվերադարձնի True, 
եթե ցուցակը սորտավորված է և False, հակառակ դեպքում'''
def is_sorted(list):
    sample = list[:]
    if sorted(sample) == list:
        return True
    elif sorted(sample) == list[-1::-1]:
        print('reverse')
        return True
    else:
        return False

'''ls = [item for item in input('Enter list: ').split()]
print(is_sorted(ls))'''

'''Իրականացնել ֆունկցիա, որը որպես պարամետր կստանա երկու list և կմիավորի դրանք։ List-երը արդեն իսկ սորտավորված են։'''
def join_lists(list1, list2):
    list1.extend(list2)
    return list1

'''ls1 = [item for item in input('Enter list1: ').split()]
ls2 = [item for item in input('Enter list2: ').split()]
new_ls = join_lists(ls1, ls2)
print(new_ls)'''
