'''Իրականացնել պարզագույն բառարան, որը ֆայլից կկարդա բառերի համախումբ՝
անգերեն-հայերեն բառերի թարգմանությամբ։ Բառերը կարող են լինել Python keyword-ներ,
statement-ներ և այլ համակարգչային գիտությանը վերաբերվող բառեր։ Օբյեկտը,
որի մեջ պետք է պահեք բառերը, կարող է լինել dictionary։'''


fs = open('dict.txt', encoding='UTF8')

lines = fs.readlines()
kvs = []
for line in lines:
    kv = line.strip()
    kvs.append(kv.split(' - '))
my_dictionary = dict([(key, value) for key, value in kvs])
print(my_dictionary)
# print(my_dictionary.keys())
# print(my_dictionary.values())
print(my_dictionary['array'])


'''Տրված է հետևյալ ֆունկցիան def myfunc(alist): . . . . 
return len(alist)։ dis module-ի օգնությամբ դուրս բերել բայթ կոդի ներկայացումը 
և նկարագրել բոլոր դաշտերը (Python byte-code)։'''


import dis
def myfunc(alist):
    return len(alist)


dis.dis(myfunc)

