from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("pick a number: 0, 1, or 2:")

    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == '0':
        print("correct")
    else:
        print("wrong guess")
        print(mylist)

mylist = [' ', '0', ' ']

mixedup_list = shuffle_list(mylist)

guess = player_guess()

check_guess = check_guess(mixedup_list, guess)

