def greatest_sum_array(array) -> int:
    greatest_sum = sum(array)
    step = 1
    while step != len(array):
        for i in range(0, len(array)):
            if step <= len(array):
                group = array[i:(i+step+1)]
                _sum = sum(group)
                if _sum > greatest_sum:
                    greatest_sum = _sum
        step += 1
    return greatest_sum


#     0  1   2  3  4  5   6  7
# sum(1, 2), sum(2, 3), sum(3, 4), sum(4, 5), sum(5, 6)
# sum(1, 2, 3), sum(2, 3, 4). sum(3, 4, 5), sum(4, 5, 6)
# sum(1, 2, 3, 4), sum(2, 3, 4, 5), sum(3, 4, 5, 6)
# sum(1, 2, 3, 4, 5), sum(2, 3, 4, 5, 6)
# sum(1, 2, 3, 4, 5, 6)


# step   =1 0 1 2 3 4 5 6 7 8 9     step = 2, 2, 4, 6, 8
# groups = 0-1, 1-2, 2-3, 3-4     groups = 0-1-2, 1-2-3, 2-3-4, 3-4-5, 4-5-6, 5-6-7, 6-7-8


if __name__== '__main__':
    ls = [-2, 4, 3, 13, 6, -3, 8, 11, -9, 4]
    print(greatest_sum_array(ls))









