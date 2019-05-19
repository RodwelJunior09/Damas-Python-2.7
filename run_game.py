import pygame
from Objects.Ficha import Ficha
from Objects.Tablero import Tablero
from Objects.Pieces import player1_army, player2_army

# Create the Structure for the Checkers Board(only the board, not the pieces). (See Image at the top) Done!!
# Create a Function that creates all the pieces located in the starting position on the board of question 1. Done!!
# Create a function that takes as a parameter a piece on the board, and prints out all the possible moves.
# Create a Function that takes as a parameter a piece on the board, and prints out all the possible jumps.
# Create a Function that takes as a parameter a color of the pieces, and prints out the position of all the pieces that are valid moves for that color.

turn_message = "Damas.... Player 1 Turn"
puntero = pygame.image.load("./Imagenes/Ficha_amarilla.png")
fill_square = pygame.image.load("./Imagenes/Cuadro.png")
game_display = pygame.display.set_mode((600, 600))
pygame.display.set_caption(turn_message)

white_color = (255, 255, 255)
game_display.fill(white_color)

tablero = Tablero()
tablero.movement_squares()
game_display.blit(tablero.board, (0,0))
pygame.display.update()

number_click = 1
turn_player = 1
game_on = False
print("Player 1 Turn")

def starting_positions():
    for piece in range(len(player1_army)):
        player1_army[piece].position = tablero.move_squares[piece]
        game_display.blit(player1_army[piece].sprite, player1_army[piece].position)
        pygame.display.update()
    pos2player = tablero.move_squares
    pos2player.reverse()
    for piece in range(len(player2_army)):
        player2_army[piece].position = pos2player[piece]
        game_display.blit(player2_army[piece].sprite, player2_army[piece].position)
        pygame.display.update()

def true_pos(pos):
    if pos in tablero.move_squares:
        return pos
    for squares in tablero.move_squares:
        for pos_x in range(pos[0] - 75, pos[0]):
            if pos_x == squares[0]:
                for pos_y in range(pos[1] - 75, pos[1]):
                    if pos_y == squares[1]:
                        return squares

def touch_another_piece(pos, player_turn):
    piece_pos = true_pos(pos)
    if player_turn == 1:
        for players in player2_army:
            if players.position == piece_pos:
                pygame.display.set_caption("Checkers...Movement Invalid")
                return True
        return False
    elif player_turn == 2:
        for players in player1_army:
            if players.position == piece_pos:
                pygame.display.set_caption("Checkers...Movement Invalid")
                return True
        return False

def find_player(pos):
    square_pos = true_pos(pos)
    if turn_player == 1:
        for piece in player1_army:
            if piece.position == square_pos:
                piece.selected_piece()
                game_display.blit(fill_square, piece.position)
                game_display.blit(piece.sprite, piece.position)
                return piece
    elif turn_player == 2:
        for piece in player2_army:
            if piece.position == square_pos:
                piece.selected_piece()
                game_display.blit(fill_square, piece.position)
                game_display.blit(piece.sprite, piece.position)
                return piece

def end_game():
    print("Finishing the game....")
    return True

starting_positions()
pygame.display.update()

while not game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = end_game()
            
        if pygame.mouse.get_pressed()[0] == 1:
            if number_click == 1:
                pos = pygame.mouse.get_pos()
                if touch_another_piece(pos, turn_player):
                    number_click = 1
                else:
                    piece_selected = find_player(pos)
                    pygame.display.update()
                    paths = piece_selected.path_piece()
                    print(paths)
                    # game_display.blit(puntero, paths[0])
                    # game_display.blit(puntero, paths[1])

                    



