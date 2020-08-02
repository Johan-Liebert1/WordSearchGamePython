from words import all_words
import random
from termcolor import colored

def get_words(number):
    words = []
    i = 0

    while i < number:
        rand_index = random.randint(0, len(all_words) - 1)
        word = all_words[rand_index]
        words.append(word) if word not in words else words.append(all_words[rand_index + 1])
        i += 1

    return words

def create_board(dimension):
    board = []

    for _ in range(dimension):
        board.append(['0'] * dimension)

    return board

def print_board(board):
    # board = dimension * dimension
    string = ''
    for i in range(len(board)):
        string += '\n\n'
        for j in range(len(board)):
            if (board[i][j].isdigit()):
                string +=  board[i][j] + "    "
            else:
                string += colored(board[i][j] , 'green') + "    "

    print(string)


def add_words_to_board(board):
    # rollover allowed

    words = get_words(10)

    for i in range(10):
        direction = 'h' if random.randint(1,100) % 2 == 0 else 'v'
        new_board = add(words[i].upper(), board, direction)

    print(words)
    return new_board


def is_space_occupied(word, direction, rand_row, rand_col):
    # count = 0
    if direction == 'h':
        for count in range(len(word)):
            if board[rand_row][rand_col + count] != '0' and board[rand_row][rand_col + count] != word[count]:
                return True

            else:
                if rand_col + count == len(board) - 1:
                    rand_col , count = 0, 0
                else:
                    continue

    else:
        for count in range(len(word)):
            if board[rand_row + count][rand_col] != '0' and board[rand_row + count][rand_col] != word[count]:
                return True

            else:
                if rand_row + count == len(board) - 1:
                    rand_row , count = 0, 0
                else:
                    continue
    return False

def get_random_values():
    return random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
    
        

# need to check whether some space is occupied or not by another letter
# avg word length = 7.409
def add(word, board, direction):
    count = 0
    # for horizontal
    if direction == 'h':
        while True:
            row, rand_col = get_random_values()
            if is_space_occupied(word, 'h', row, rand_col) == True:
                continue
            else:
                break
    
    # for vertical
    if direction == 'v':
        while True:
            rand_row, col = get_random_values()
            if is_space_occupied(word, 'v', rand_row, col) == True:
                continue
            else:
                break


    for char in word:

        if direction == 'h':
            board[row][rand_col + count] = char

            if count + rand_col == len(board) - 1: 
                count, rand_col = 0, 0

            else:
                count += 1

        elif direction == 'v':
            board[rand_row + count][col] = char

            if count + rand_row == len(board) - 1: 
                count, rand_row = 0, 0

            else:
                count += 1
        
    print_board(board)
    
    return board


def main():
    crossword = add_words_to_board(board)
    print_board(crossword)

board = create_board(15)

if __name__ == "__main__":
    main()



