def _map(func, iterable):
    for item in iterable:
        yield func(item)


# ls = [1, 2, 3]
# new_ls = list(_map(lambda x: x ** 2, ls))
# print(new_ls)

def _reduce(func, iterable, initializer=None):
    while len(iterable) >= 2:
        i = 0
        initializer = func(iterable[i], iterable[i+1])
        iterable.insert(i+2, initializer)
        iterable = iterable[2:]
    return initializer


# scores = [75, 65, 80, 95, 50]
# total = _reduce(lambda a, b: a + b, scores)
# print(total)


def _range(start=0,stop=0, step=1):
    r = []
    if start < stop:
        while start < stop:
            r.append(start)
            start += step
    else:
        while start >= stop:
            r.append(start)
            start += step
    return r


'''failed attempt'''
# def implement_for(range_or_iter, func):
#     if hasattr(range_or_iter, '__iter__'):
#         range_or_iter = iter(range_or_iter)
#         def _for(iterat = range_or_iter):
#             while iterat:
#                 yield next(iterat)
#     elif type(range_or_iter) == int:
#         def _for(num = range_or_iter):
#             i = 0
#             while i != num:
#                 yield i
#                 i += 1
#     while range_or_iter:
#         return func(next(_for(range_or_iter)))


ls = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in _range(len(ls)-1, 0, -1):
#     print(ls[i], end=' ')


def itrtr(obj):
    if type(obj) == int:
        i = 0
        l = []
        while i != obj:
            l.append(i)
            i += 1
        obj = iter(l)
    elif hasattr(obj, '__iter__'):
        obj = iter(obj)
    else:
        return TypeError
    return obj

def my_for(obj, func):
    obj = itrtr(obj)
    while True:
        try:
            func(next(obj))
        except:
            break


new_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_for(new_ls, print)
print('__________________________________________________________')
my_for(5, print)   # for i in range(5)
print('__________________________________________________________')
my_for(range(1,7), print)
print('__________________________________________________________')
my_for(range(1, 5), lambda x: x ** 2)     # this one doesn't work for some reason

