'''Tic-tac-toe տախտակը կարող է ներկայացվել որպես 3×3 երկչափ ցուցակ, որտեղ զրոները նշանակում են
դատարկ բջիջներ, մեկը՝ X, իսկ երկուսը նշանակում են O: Իրականացնել այդ խաղը օգտագործելով Python List։'''
def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()

def check_row(matrix, sym):
    for row in range(len(matrix)):
        if matrix[row][0] == sym and matrix[row][1] == sym and matrix[row][2] == sym:
            return True

def check_colum(matrix, sym):
    for col in range(len(matrix)):
        if matrix[0][col]  == sym and matrix[1][col]  == sym and matrix[2][col]  == sym:
            return True

def check_diag(matrix, sym):
    if matrix[0][0] == sym and matrix[1][1] == sym and matrix[2][2] == sym:
        return True
    elif matrix[0][2] == sym and matrix[1][1] == sym and matrix[2][0] == sym:
        return True

def is_vacant(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 0:
                return True


'''board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
print_matrix(board)
win = False
for turn in range(5):
    Flag = True
    while Flag:
        print('Player 1, input position: ')
        i1 = int(input('row: '))
        j1 = int(input('column: '))
        if board[i1][j1] == 0:
            board[i1][j1] = 'x'
            print_matrix(board)
            Flag = False
        else:
            if is_vacant(board):
                print('Already occupied, try again!')
            else:
                print("It's a tie!")
                Flag = False
    if check_row(board, 'x') or check_colum(board, 'x') or check_diag(board, 'x'):
        print('Player1 won!')
        win = True
        break
    Flag = True
    while Flag and is_vacant(board):
        print('Player 2, input position: ')
        i2 = int(input('row: '))
        j2 = int(input('column: '))
        if board[i2][j2] == 0:
            board[i2][j2] = 'O'
            print_matrix(board)
            Flag = False
        else:
            if is_vacant(board):
                print('Already occupied, try again!')
            else:
                print("It's a tie!")
                Flag = False
    if check_row(board, 'O') or check_colum(board, 'O') or check_diag(board, 'O'):
        print('Player2 won!')
        win = True
        break
if not is_vacant(board) and not win:
    print("It's a tie!")
print_matrix(board)'''


'''Իրականացնել պարզ վիկտորինա-խաղ, որը կպարունակի հարցերի և պատասխանների ցուցակներ(lists)։ 
Խաղը սկսելուց պատահական սկզբունքով հարց պետք է տրվի խաղացողին և պատասխանից կախված խաղի վերջում հայտնվի ճիշտ պատասխանների քանակը։ 
Հարցերը չպետք է կրկնվեն։ '''
import random

Q = ['How many legs does a spider have?', 'What is the name of the toy cowboy in Toy Story?',
     'What is the color of an emerald?', 'What is something you hit with a hammer?',
     'What\'s the name of a place you go to see lots of animals?',
     'Whose nose grew longer every time he lied?', 'What is the name of the fairy in Peter Pan?',
     'If you freeze water, what do you get?', 'How many planets are in our solar system?',
     'What do you use to write on a blackboard?']
A = ['8', 'Woody', 'Green', 'Nail', 'Zoo' , 'Pinocchio', 'Tinkerbell', 'Ice', '8', 'Chalk']

index_ls = list(range(0, 10))
random.shuffle(index_ls)
correct = 0
for i in index_ls:
    print(Q[i])
    answer = str(input())
    if answer.lower() == A[i].lower() or answer.lower() in A[i].lower():
        print('Correct!')
        correct += 1
print('Numer of correct answers: ', correct)