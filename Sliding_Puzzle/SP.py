import random

# Introduction of this game.
print('''Welcome to sliding puzzle game!
The board has an empty space where an adjacent tile can be slid to. \
The objective of the game is to rearrange \
the tiles into a sequential order by their numbers\
(left to right, top to bottom) by repeatedly \
making sliding moves (left, right, up or down).
You can choose dimension and control buttons by yourself!''')
# Prompt user for the desired dimension of the 
# puzzle, minimum 3, up to and including 10.
while True:
    n = input('Enter the desired dimension of the puzzle(it should between 3 and 10):')
    # Make sure the user enters a number between 3 and 10.
    # Ask the user to retype if there is an error.
    try:
        n = int(n)
        if 3 <= n <= 10:
            break
        else:
            print('Please enter a interger between 3 and 10!')
    except:
        print('Please enter a interger between 3 and 10!')

# Prompt user to enter the 4 letters 
# used for the left, right, up and down moves.
while True:
    # Make sure the user enters 4 different letters.
    # Ask the user to retype if there is an error.
    try:
        l, r, u, d = input(
            'Enter the four different letters used for left, right, up and down directions:')
        if (l.isalpha() and r.isalpha() and u.isalpha() and d.isalpha()
                and l != r and l != u and l != d and r != u and r != d and u != d):
            break
        else:
            print('Please enter the four different letters.')
    except:
        print('Please enter the four different letters linked together.')


# Define a function to generate a 
# randomized and solvable puzzle according to dimension.
def get_valid_list(li: list) -> list:
    global l, r, u, d  # Control letters
    # Randomly move 0 in the list 1000 times.
    b = 0
    while b < 1000:
        a = li.index(0)  # Get the index of 0.
        b += 1
        if a == 0:  # 0 is in the upper left corner.
            update_list(li, random.choice([l, u]))  # Only can move left or up.
        elif a == n - 1:  # 0 is in the upper right corner.
            update_list(li, random.choice([r, u]))  # Only can move right or up.
        elif a == n ** 2 - n:  # 0 is in the bottom left corner.
            update_list(li, random.choice([l, d]))  # Only can move left or down.
        elif a == n ** 2 - 1:  # 0 is in the bottom right corner.
            update_list(li, random.choice([r, d]))  # Only can move right or down.
        elif a in range(1, n - 1):  # 0 is in the upper except corner.
            update_list(li, random.choice([l, r, u]))  # Only can move left, right or up.
        elif a in range(n ** 2 - n + 1, n ** 2 - 1):  # 0 is in the bottom except corner.
            update_list(li, random.choice([l, r, d]))  # Only can move left, right or down.
        elif a in range(n, n ** 2 - 2 * n + 1, n):  # 0 is in the left-most except corner.
            update_list(li, random.choice([l, u, d]))  # Only can move left, up or down.
        elif a in range(2 * n - 1, n ** 2 - n, n):  # 0 is in the right-most except corner.
            update_list(li, random.choice([r, u, d]))  # Only can move right, up or down.
        else:  # 0 is not in the outermost shell.
            update_list(li, random.choice([l, r, u, d]))  # Can move left, right, up or down.
    return li


# Define a function to show the list.
def display_list(li: list):
    count = 0
    for i in li:
        if i == 0:  # Convert 0 to space to print.
            i = ' '
        count += 1
        print('%-5s' % i, end="")
        if count % n == 0:  # n times a line break.
            print('')


# Define a function to move.
def update_list(li: list, m: str) -> list:
    a = li.index(0)
    # The movement of user input is 
    # the opposite of the movement of 0's index.
    if m == l:
        li[a], li[a + 1] = li[a + 1], li[a]  # Enter l, 0 move right.
    if m == r:
        li[a], li[a - 1] = li[a - 1], li[a]  # Enter r, 0 move left.
    if m == u:
        li[a], li[a + n] = li[a + n], li[a]  # Enter u, 0 move down.
    if m == d:
        li[a], li[a - n] = li[a - n], li[a]  # Enter d, 0 move up.
    return li


# Define a function to prompt the 
# player the valid sliding direction and enter it.
def input_move(li: list) -> str:
    a = li.index(0)  # Get the index of 0.
    if a == 0:  # 0 is in the upper left corner.
        while True:
            x = input('Enter your move (left-%s, up-%s):' % (l, u))
            if x != l and x != u:
                print('Invalid inputs!')
            else:
                break
    elif a == n - 1:  # 0 is in the upper right corner.
        while True:
            x = input('Enter your move (right-%s, up-%s):' % (r, u))
            if x != r and x != u:
                print('Invalid inputs!')
            else:
                break
    elif a == n ** 2 - n:  # 0 is in the bottom left corner.
        while True:
            x = input('Enter your move (left-%s, down-%s):' % (l, d))
            if x != l and x != d:
                print('Invalid inputs!')
            else:
                break
    elif a == n ** 2 - 1:  # 0 is in the bottom right corner.
        while True:
            x = input('Enter your move (right-%s, down-%s):' % (r, d))
            if x != r and x != d:
                print('Invalid inputs!')
            else:
                break
    elif a in range(1, n - 1):  # 0 is in the upper except corner.
        while True:
            x = input('Enter your move (left-%s, right-%s, up-%s):' % (l, r, u))
            if x != l and x != r and x != u:
                print('Invalid inputs!')
            else:
                break
    elif a in range(n ** 2 - n + 1, n ** 2 - 1):  # 0 is in the bottom except corner.
        while True:
            x = input('Enter your move (left-%s, right-%s, down-%s):' % (l, r, d))
            if x != l and x != r and x != d:
                print('Invalid inputs!')
            else:
                break
    elif a in range(n, n ** 2 - 2 * n + 1, n):  # 0 is in the left-most except corner.
        while True:
            x = input('Enter your move (left-%s, up-%s, down-%s):' % (l, u, d))
            if x != l and x != u and x != d:
                print('Invalid inputs!')
            else:
                break
    elif a in range(2 * n - 1, n ** 2 - n, n):  # 0 is in the right-most except corner.
        while True:
            x = input('Enter your move (right-%s, up-%s, down-%s):' % (r, u, d))
            if x != r and x != u and x != d:
                print('Invalid inputs!')
            else:
                break
    else:  # 0 is not in the outermost shell.
        while True:
            x = input('Enter your move (left-%s, right-%s, up-%s, down-%s):' % (l, r, u, d))
            if x != l and x != r and x != u and x != d:
                print('Invalid inputs!')
            else:
                break
    return x


# Define a function to start game.
def start_game():
    list1 = [i for i in range(n ** 2)]  # Get the initial list.
    # Get the list for final verification.
    list2 = list1[1:]
    list2.append(0)
    get_valid_list(list1)
    display_list(list1)
    c = 0  # Count the number of moves.
    while True:
        list1 = update_list(list1, input_move(list1))
        c += 1
        display_list(list1)
        if list1 == list2:
            print('Congratulations! You solved the puzzle in %d moves!' % c)
            break


# Loops or exits the game.
flag = True
while flag:
    start_game()
    while True:
        new = input("Enter \"n\" to start a new game or enter \"q\" to end the game:")
        if new == 'q':
            flag = False
            break
        elif new == 'n':
            break
        else:  # Prompt user only can enter "q" or "n".
            print('Please enter \"q\" or \"n\".')
            continue
