from words import all_words
import random
from termcolor import colored
import pygame
import copy

# Pygame Config
white = (230, 230, 230)
black = (0,0,0)
red = (200, 0, 0)
green = (0, 150, 0)

pygame.init()
window = pygame.display.set_mode((600, 750))
window.fill(white)

pygame.font.init()
FONT = pygame.font.SysFont("Times New Roman", 16)
FONT_BIG = pygame.font.SysFont("Times New Roman", 24)

run = True
clock = pygame.time.Clock()

words = []
# Returns "number" randomly chosen words from the list in words.py
def get_words(number):
    i = 0

    while i < number:
        rand_index = random.randint(0, len(all_words) - 1)
        word = all_words[rand_index]
        words.append(word) if word not in words else words.append(all_words[rand_index + 1])
        i += 1

    return words

'''Creates the boards of given dimension. Ex 15 x 15 or 10 x 10'''
def create_board(dimension):
    board = []

    for _ in range(dimension):
        board.append(['0'] * dimension)

    return board

# Prints the board prettily
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
    '''Calls function to add randomly chosen words to board'''

    # rollover allowed

    words = get_words(10)

    for i in range(10):
        direction = 'h' if random.randint(1,100) % 2 == 0 else 'v'
        new_board = add(words[i].upper(), board, direction)

    # print(words)
    return new_board


def is_space_occupied(word, direction, rand_row, rand_col):
    count = 0
    if direction == 'h':
        for _ in range(len(word)):
            if board[rand_row][rand_col + count].isdigit():
                # print_board(board)
                if rand_col + count == len(board) - 1:
                    rand_col , count = 0, 0
                else: count += 1

            elif board[rand_row][rand_col + count] == word[count]:
                # print_board(board)
                if rand_col + count == len(board) - 1:
                    rand_col , count = 0, 0
                else: count += 1
            
            else:
                return True

    else:
        for _ in range(len(word)):
            if board[rand_row + count][rand_col].isdigit():
                # print_board(board)
                if rand_row + count == len(board) - 1:
                    rand_row , count = 0, 0
                else: count += 1

            elif board[rand_row + count][rand_col] == word[count]:
                # print_board(board)
                if rand_row + count == len(board) - 1:
                    rand_row , count = 0, 0
                else: count += 1
            
            else:
                return True

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
        
    # print_board(board)
    
    return board

'''fill the crossword'''
def fill_crossword(crossword):
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    filled_crossword = copy.deepcopy(crossword)
    for row in range(len(crossword)):
        for col in range(len(crossword)):
            if filled_crossword[row][col] in letters:
                continue
            else:
                filled_crossword[row][col] = letters[random.randrange(0, 26)]
    return filled_crossword
    
   


def main():
    crossword = add_words_to_board(board)
    return crossword

def create_grid():
    w = 600 // 15
    width = 600
    x, y = 0,0

    for _ in range(15):
        pygame.draw.line(window, black, (x,0), (x,width))
        pygame.draw.line(window, black, (0, y), (width, y))

        y += w 
        x += w   
    
    pygame.draw.line(window, black, (620, 0), (620, width))
    

def put_letters_on_grid(crossword):
    x = 15
    y = 15
    # print(crossword)
    for row in range(len(crossword)):
        y = 15 + 40 * (row)
        x = 15
        for col in range(len(crossword)):
            x = 15 + 40 * (col)
            if crossword[row][col] == '0':
                text = FONT.render(crossword[row][col], 1, black)
            else:
                text = FONT.render(crossword[row][col], 1, green)

            window.blit(text, (x,y))

    words_x = 0
    words_y = 620

    for i in range(len(words)):
        wrd = " ".join(words[i])
        text = FONT.render(wrd, 1, red)
        window.blit(text, (words_x, words_y))
        if words_x + text.get_width() + 10 < 600:
            words_x += text.get_width() + 10

        else:
            words_x = 0
            words_y += text.get_height() + 10

    answer_text = FONT_BIG.render("Click here to see the solution", 1, red)
    window.blit(answer_text, (150, 710))


board = create_board(15)

crossword = main()

create_grid()

filled_crossword = fill_crossword(crossword)
put_letters_on_grid(filled_crossword)

print_board(crossword)

show_answer = False

while run:
    clock.tick(30)

    #gets x and y position of mouse as (x, y)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 <= mouse[0] <= 150+283 and 710 <= mouse[1] <= 738:
                window.fill(white)
                create_grid()
                put_letters_on_grid(crossword)

  
    pygame.display.update()




