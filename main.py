from words import all_words
import random


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
            string +=  board[i][j] + "    "

    print(string)


def add_words_to_board(board):
    # rollover allowed

    words = get_words(10)

    direction = 'horizonal' if random.randint(0,1) == 0 else 'vertical'

    new_board = add('CONSPICUOUS', board, 'vertical')
    return new_board


def add(word, board, direction):
    count = 0
    # for horizontal
    row = random.randint(0, len(board) - 1)
    rand_col = random.randint(0, len(board) - 1)
    
    # for vertical
    rand_row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)

    # add in rows

    for char in word:

        if direction == 'horizontal':
            board[row][rand_col + count] = char

            if count + rand_col == len(board) - 1: 
                count, rand_col, rand_row = 0, 0, 0

            else:
                count += 1

        else:
            board[rand_row + count][col] = char

            if count + rand_row == len(board) - 1: 
                count, rand_col, rand_row = 0, 0, 0

            else:
                count += 1
    
    return board


def main():
    crossword = add_words_to_board(board)
    print_board(crossword)

board = create_board(15)

if __name__ == "__main__":
    main()



