from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def print_table():
    clear()
    sleep(0.1)
    print(a1," | ",a2," | ",a3,"\n--|---|--\n", b1," | ", b2," | ", b3,"\n--|---|--\n", c1, " | ", c2, " | ", c3, sep="")

def verify_win(p):
#    if table.count(p) < 3:
#        return None
    if table[0, 1, 2] == [p, p, p] or table[3, 4, 5] == [p, p, p] or table[6, 7, 8] == [p, p, p]:
        return True
    elif table[0, 3, 6] == [p, p, p] or table[1, 4, 7] == [p, p, p] or table[2, 5, 8] == [p, p, p]:
        return True
    elif table[0, 4, 8] == [p, p, p] or table[2, 4, 6] == [p, p, p]:
        return True
    else:
        return None

def choose_player():
    global human
    global computer
    p = input("choose 1 for X or 2 for O: ")
    if p == "1":
       human, computer = "X", "O"
    elif p == "2":
       human, computer = "O", "X"
    else:
        print(p, "is not 1 or 2, try again\n")
        choose_player()

def human_select_field():
    f = input("select a empty field: ")
    if int(f) < 0 or int(f) > 8:
        print("invalid option, try again\n")
        human_select_field()
    elif table[int(f)] == human or table[int(f)] == computer:
        print("this field is not empty, try again\n")
        human_select_field()
    else:
        table[int(f)] = human




a1, a2, a3, b1, b2, b3, c1, c2, c3 = 0, 1, 2, 3, 4, 5, 6, 7, 8
global table
table = [a1, a2, a3, b1, b2, b3, c1, c2, c3]


choose_player()
human_select_field()
print_table()