from os import system, name
from time import sleep
from random import sample
import random


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def print_table():
    clear()
    sleep(0.1)
    print(table[0]," | ",table[1]," | ",table[2],"\n--|---|--\n", table[3]," | ", table[4]," | ", table[5], \
          "\n--|---|--\n", table[6], " | ", table[7], " | ", table[8], sep="")

def restart_or_out():
    x = input("Press 1 for play again, 2 for finish the game")
    if x == "1":
        start()
    elif x == "2":
        exit()
    else:
        print("invalid option", x, "is not 1 or 2")
        restart_or_out()

def finish_game(p):
    if human == p:
        print("congrats human, you win")
        restart_or_out()
    else:
        print("you lose human")
        restart_or_out()

def verify_win(p):
    #verify line
    if table[0, 1, 2] == [p, p, p] or table[3, 4, 5] == [p, p, p] or table[6, 7, 8] == [p, p, p]:
        finish_game(p)
    # verify collum
    elif table[0, 3, 6] == [p, p, p] or table[1, 4, 7] == [p, p, p] or table[2, 5, 8] == [p, p, p]:
        finish_game(p)
    # verify diagonal
    elif table[0, 4, 8] == [p, p, p] or table[2, 4, 6] == [p, p, p]:
        finish_game(p)
    else:
        return None

def choose_player():
    global human
    global computer
    p = input('The "X" player will start the game\nChoose 1 for X or 2 for O: ')
    if p == "1":
        human, computer = "X", "O"
    elif p == "2":
        human, computer = "O", "X"
    else:
        print(p, "is not 1 or 2, try again\n")
        choose_player()

def human_select_field():
    f = input("select a empty field: ")
    if f not in table:
        print("invalid option, try again\n")
        human_select_field()
    else:
        table[int(f)] = human
        verify_win(human)

def computer_select_field():
    if level == "easy":
        f = sample(table, 1)
        f = f[0]
        if f == computer or f == human:
            computer_select_field()
        else:
            table[int(f)] = computer
            verify_win(computer)

def start():
    input("Tic Tac Toe\n\nPress ENTER to start")
    clear()
    choose_player()
    #choose_level()
    print_table()
    if human == "X":
        for i in range(len(table)):
            if i == 0 or i % 2 == 0:
                human_select_field()
            else:
                computer_select_field()
    if computer == "X":
        for i in len(table):
            if i == 0 or i % 2 == 0:
                computer_select_field()
            else:
                human_select_field()
    print("Human and Computer loses")
    restart_or_out()

global table, empty_table, human, computer, level
table = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
level = "easy"

start()