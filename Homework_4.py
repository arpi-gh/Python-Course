'''Իրականացնել ծրագիր, որում պետք է ստեղծել ցուցակ(list),
բաղկացած 100-ից 1000-ի միջև ընկած բոլոր պալինդրոմային թվերից՝
օգատգործելով list-ի comprehension։'''

#
# num_list = [num for num in range(100, 1001) if (num == (num % 10 * 100) + (num // 10 % 10 * 10) + (num // 100 % 10))]
# print(num_list)

'''Իրականացնել ծրագիր, որը շրջում է մատրիցը 180 աստիճանով։ '''


def input_matrix(n, m):
    matrix = []
    for i in range(n):
        l = [int(v) for v in input('Enter matrix row. {} numbers only:  '.format(m)).split(' ')]
        if len(l) != m:
            print('ERROR')
            return None
        matrix.append(l)
    return matrix


def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()


# columns = int(input("Number of columns: "))
# rows = int(input("Number of rows:"))
# mat = input_matrix(rows, columns)
# print_matrix(mat)
# print("Here's the result!")
# for ls in range(len(mat)):
#     mat[ls] = mat[ls][-1::-1]
# mat = mat[-1::-1]
# print_matrix(mat)

'''Ունենք ամբողջ թվերից բաղկացած մատրից, որի վրա պետք է իրականացնել transpose։ 
Transpose կատարել նշանակում է մատրիցի տողերը փոխադրել սյուներով։'''

# columns = int(input("Number of columns: "))
# rows = int(input("Number of rows: "))
# mat = input_matrix(rows, columns)
# print_matrix(mat)
# res_mat = []
# mat_row = []
# for j in range(len(mat[0])):
#     for i in range(len(mat)):
#         mat_row.append(mat[i][j])
#     res_mat.append(mat_row)
#     mat_row = []
#
# print("Here's the resulting matrix!")
# print_matrix(res_mat)

'''Գրել ծրագիր, որը կստուգի մուտքային թիվը երկուսի աստիճան է, թե՝ ոչ։'''

# num = int(input("Enter a number: "))
# n = num
# while n > 1:
#     n /= 2
# if n == 1:
#     print("{} is a power of 2".format(num))
# else:
#     print("{} is not a power of 2".format(num))

'''Գրել ծրագիր, որը որպես մուտքային արժեք կստանա ամբողջ թիվ և կարտածի նրանում պարունակվող ‘1’ բիթերի քանակը։'''

num = int(input("Enter a number: "))
n = num
bin_ls = []
while num > 0:
    n = num % 2
    num //= 2
    bin_ls.append(n)
counter = 0
for b in bin_ls:
    if b == 1:
        counter += 1
bin_ls.reverse()
print(bin_ls)
print(counter)
