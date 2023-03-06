def factorial(n):
    if n == 0:
        return 1
    if isinstance(n, int):
        return n * factorial(n-1)
    else:
        raise ValueError


'''while True:
    try:
        num = int(input('Enter a number: '))
    except ValueError:
        print('That wasn\'t a number. Try again.')
    else:
        print(factorial(num))
        break'''


def enum_func(it, start = 0):
    counter = [start]
    items = [it[0]]
    if hasattr(it, '__iter__'):
        for i in range(1, len(it)):
            counter.append(i)
            items.append(it[i])
        return list(zip(counter, items))
    else:
        raise TypeError


'''ls = [i for i in input().split()]
for index, item in enum_func(ls):
    print(item, 'is at index', index) '''


def isdigit(n):
    try:
        int(n)
    except:
        return False
    else:
        return True


def filter_func(func, item):
    if hasattr(item, '__iter__'):
        _type = type(item)
        ret_val = []
        if func is None:
            for i in item:
                if i:
                    ret_val.append(i)
        else:
            for i in item:
                if func(i):
                    ret_val.append(i)
        return _type(ret_val)


'''test_it = [1, 2, '', 34, 'h', (1, 2, 3)]
print(filter_func(isdigit, test_it))'''


def pow_of_four(n):
    if type(n) != int:
        return
    if n / 4 == 1:
        return True
    if n % 4 == 0:
        return pow_of_four(n / 4)
    return False


'''num = int(input())
print(pow_of_four(num))'''

