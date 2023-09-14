#!/usr/local/bin/python3

# Creates A Simple Python Tic Tac Toe Game

# Imports Some Useful APIs
import pygame
import math

# Initialize Pygame And Sets Up The Game Clock
pygame.init()
clock = pygame.time.Clock()

# ----- GLOBAL VARIABLES ----- #

# Defines How Often The Screen Will Update
FPS = 60

# Sets Up The Screen Dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Sets Up The Title Screen Image Dimensions
TITLE_SCREEN_WIDTH = 1200
TITLE_SCREEN_HEIGHT = 800
TITLE_SCREEN_SIZE = (TITLE_SCREEN_WIDTH, TITLE_SCREEN_HEIGHT)

# Sets Up The Play Button Image Dimensions
PLAY_BUTTON_WIDTH = 200
PLAY_BUTTON_HEIGHT = 200
PLAY_BUTTON_SIZE = (PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)

# Sets Up The Board Image Dimensions
BOARD_WIDTH = 800
BOARD_HEIGHT = 800
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)

# Sets Up The Player Image Dimensions
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)

# Sets Up The Dimensions For The Screen That Will Display Who Won
WINNER_WIDTH = 600
WINNER_HEIGHT = 400
WINNER_SIZE = (WINNER_WIDTH, WINNER_HEIGHT)

# Defines A Blank Space
BLANK = "-"

# Define Some Colors: R G B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ----- Tracking Variables ----- #
board = [BLANK, BLANK, BLANK, 
         BLANK, BLANK, BLANK, 
         BLANK, BLANK, BLANK]

player = "X"
winner = None
stage = "title"

# Creates The Game Window
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Tic Tac Toe")

# Sets Up The Images
TITLE_IMAGE = pygame.transform.scale(pygame.image.load("assets/title.png"), TITLE_SCREEN_SIZE)
PLAY_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load("assets/play_button.png"), PLAY_BUTTON_SIZE)
BOARD_IMAGE = pygame.transform.scale(pygame.image.load("assets/board.png"), BOARD_SIZE)
PLAYER_X_IMAGE = pygame.transform.scale(pygame.image.load("assets/x.png"), PLAYER_SIZE)
PLAYER_O_IMAGE = pygame.transform.scale(pygame.image.load("assets/o.png"), PLAYER_SIZE)
WINNER_X_IMAGE = pygame.transform.scale(pygame.image.load("assets/x_win.png"), WINNER_SIZE)
WINNER_O_IMAGE = pygame.transform.scale(pygame.image.load("assets/o_win.png"), WINNER_SIZE)
WINNER_TIE_IMAGE = pygame.transform.scale(pygame.image.load("assets/tie.png"), WINNER_SIZE)

# ----- HELPER FUNCTIONS ----- #
def draw_title_screen():
    # Draws The Title Screen
    SCREEN.blit(TITLE_IMAGE, (0, 0))
    
    # Adds The Play Button
    PLAY_BUTTON_X = (SCREEN_WIDTH / 2) - (PLAY_BUTTON_WIDTH / 2)
    PLAY_BUTTON_Y = ((SCREEN_HEIGHT / 4) * 3) - (PLAY_BUTTON_HEIGHT / 2)
    SCREEN.blit(PLAY_BUTTON_IMAGE, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
    
def draw_board():
    # Sets The Background To Black
    SCREEN.fill(BLACK)
    
    # Draws The Tic Tac Toe Board On The Screen
    SCREEN.blit(BOARD_IMAGE, ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2), (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2)))
    
def get_square(x, y):
    global tile
    OFF_SET = 75
    # Finds What Section Of The Board The User Clicks
    if x < (SCREEN_WIDTH / 3) + OFF_SET and y < (SCREEN_HEIGHT / 3):
        # Top Left Square
        tile = 1
    elif (SCREEN_WIDTH / 3)  - OFF_SET < x < ((SCREEN_WIDTH / 3) * 2) - OFF_SET and y < (SCREEN_HEIGHT / 3):
        # Top Middle Square
        tile = 2
    elif ((SCREEN_WIDTH / 3) * 2) - OFF_SET < x and y < (SCREEN_HEIGHT / 3):
        # Top Right Square
        tile = 3
    elif x < (SCREEN_WIDTH / 3) + OFF_SET and (SCREEN_HEIGHT / 3) < y < ((SCREEN_HEIGHT / 3) * 2):
        # Middle Left Square
        tile = 4
    elif (SCREEN_WIDTH / 3) - OFF_SET < x < ((SCREEN_WIDTH / 3) * 2) - OFF_SET and (SCREEN_HEIGHT / 3) < y < ((SCREEN_HEIGHT / 3) * 2):
        # Center Square
        tile = 5
    elif ((SCREEN_WIDTH / 3) * 2) - OFF_SET < x and (SCREEN_HEIGHT / 3) < y < ((SCREEN_HEIGHT / 3) * 2):
        # Middle Right Square
        tile = 6
    elif x < (SCREEN_WIDTH / 3) + OFF_SET and ((SCREEN_HEIGHT / 3) * 2) < y:
        # Bottom Left Square
        tile = 7
    elif (SCREEN_WIDTH / 3) - OFF_SET < x < ((SCREEN_WIDTH / 3) * 2) - OFF_SET and ((SCREEN_HEIGHT / 3) * 2) < y:
        # Bottom Middle Square
        tile = 8
    elif ((SCREEN_WIDTH / 3) * 2) - OFF_SET < x and ((SCREEN_HEIGHT / 3) * 2) < y:
        # Bottom Right Square
        tile = 9
    return tile

def get_pixel(tile):
    global pixel
    TILE_SIZE = 250
    # Finds The Pixel In The Top Left Corner Of A Given Square
    if tile == 1:
        # Top Left Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + 50)
    elif tile == 2:
        # Top Middle Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + TILE_SIZE + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + 50)
    elif tile == 3:
        # Top Right Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + 2 * TILE_SIZE + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + 50)
    elif tile == 4:
        # Middle Left Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + TILE_SIZE + 50)
    elif tile == 5:
        # Center Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + TILE_SIZE + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + TILE_SIZE + 50)
    elif tile == 6:
        # Middle Right Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + 2 * TILE_SIZE + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + TILE_SIZE + 50)
    elif tile == 7:
        # Bottom Left Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + 2 * TILE_SIZE + 50)
    elif tile == 8:
        # Bottom Middle Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + TILE_SIZE + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + 2 * TILE_SIZE + 50)
    elif tile == 9:
        # Bottom Right Square
        pixel = ((SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2) + 2 * TILE_SIZE + 50, (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2) + 2 * TILE_SIZE + 50)
    return pixel
    
def draw_player(pixel):
    global player
    # Draws The Icon For The Current Player
    if player == "X":
        image = PLAYER_X_IMAGE
    elif player == "O":
        image = PLAYER_O_IMAGE
    
    # Checks If The Spot Clicked Is Already Occupied
    if board[tile - 1] == BLANK:
        board[tile - 1] = player
        SCREEN.blit(image, pixel)
        
        flip_player()

# Switches Between Player
def flip_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

# Checks Rows
def check_rows():
    global stage
    row_1 = board[0] == board[1] == board[2] != BLANK
    row_2 = board[3] == board[4] == board[5] != BLANK
    row_3 = board[6] == board[7] == board[8] != BLANK
    if row_1 or row_2 or row_3:
        stage = "win"
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

# Checks Columns
def check_columns():
    global stage
    column_1 = board[0] == board[3] == board[6] != BLANK
    column_2 = board[1] == board[4] == board[7] != BLANK
    column_3 = board[2] == board[5] == board[8] != BLANK
    if column_1 or column_2 or column_3:
        stage = "win"
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

# Check Diagonals
def check_diagonals():
    global stage
    diagonal_1 = board[0] == board[4] == board[8] != BLANK
    diagonal_2 = board[6] == board[4] == board[2] != BLANK
    if diagonal_1 or diagonal_2:
        stage = "win"
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

# Checks If A Player Won
def check_win():
    global winner
    global stage
    row_winner = check_rows()
    columns_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
        stage = "win"
    elif columns_winner:
        winner = columns_winner
        stage = "win"
    elif diagonal_winner:
        winner = diagonal_winner
        stage = "win"
    else:
        winner = None

# Checks If The Game Was A Tie
def check_tie():
    global stage
    if BLANK not in board and winner == None:
        stage = "win"

# Checks If The Game Is Over
def check_over():
    # Does This By Checking If A Player Won Or The Game Is A Tie
    check_win()
    check_tie()

# Draws The Win Screen For Whoever Won
def draw_winner(winner):
    if winner == "X":
        # Set The Background Black
        SCREEN.fill(BLACK)
        
        # Displays The X Win Screen
        SCREEN.blit(WINNER_X_IMAGE, (SCREEN_WIDTH / 2 - WINNER_WIDTH / 2, SCREEN_HEIGHT / 2 - WINNER_HEIGHT / 2))
        
    elif winner == "O":
        # Sets The Background Black
        SCREEN.fill(BLACK)
        
        # Displays The O Win Screen
        SCREEN.blit(WINNER_O_IMAGE, (SCREEN_WIDTH / 2 - WINNER_WIDTH / 2, SCREEN_HEIGHT / 2 - WINNER_HEIGHT / 2))
        
    elif winner == None:
        # Sets The Background Black
        SCREEN.fill(BLACK)
        
        # Displays The Tie Screen
        SCREEN.blit(WINNER_TIE_IMAGE, (SCREEN_WIDTH / 2 - WINNER_WIDTH / 2, SCREEN_HEIGHT / 2 - WINNER_HEIGHT / 2))
        
# ----- MAIN FUNCTION ----- #
def main():
    global player
    global winner
    global stage
    global board

    # Displays The Title Screen
    draw_title_screen()

    # Main Game Loop
    while True:
        # Handles Events
        for event in pygame.event.get():
            # The Red X In The Top Left-Hand Of The Window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Title Screen --> Board
            elif event.type == pygame.MOUSEBUTTONDOWN and (500 < mouse_x < 700) and (500 < mouse_y < 700) and stage == "title":
                draw_board()
                stage = "board"
            # Puts The Player's Character On The Board
            elif event.type == pygame.MOUSEBUTTONDOWN and stage == "board":
                draw_player(get_pixel(get_square(mouse_x, mouse_y)))
                # Checks If The Game Is Over
                check_over()
            # Player Wins
            elif stage == "win":
                draw_winner(winner)
                # Resets The Board
                board = [BLANK, BLANK, BLANK, 
                         BLANK, BLANK, BLANK, 
                         BLANK, BLANK, BLANK]
                # Sets The Stage Back To Title So The User Can Play Again      
                stage = "title"

        # Gets The Mouse Position At All Times
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Updates The Screen
        pygame.display.flip()
        clock.tick(FPS)

# Runs The Code
if __name__ == "__main__":
    main()
