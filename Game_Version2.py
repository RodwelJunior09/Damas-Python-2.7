from Game_Class2 import *

# Create the Structure for the Checkers Board(only the board, not the pieces). (See Image at the top)
# Create a Function that creates all the pieces located in the starting position on the board of question 1.
# Create a function that takes as a parameter a piece on the board, and prints out all the possible moves.
# Create a Function that takes as a parameter a piece on the board, and prints out all the possible jumps.
# Create a Function that takes as a parameter a color of the pieces, and prints out the position of all the pieces that are valid moves for that color.


Cuadro = pygame.image.load("./Imagenes/Cuadro.png")
Puntero = pygame.image.load("./Imagenes/Ficha_amarilla.png")
Display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Damas... Players 1 Turn")
white = (255, 255, 255)
Display.fill(white)
Board = Tablero(Display)
pygame.display.update()
EndGame = False

Turn_Player = 1
print "Player 1 Turn"

User_Ficha1, User_Ficha2, User_Ficha3, User_Ficha4, User_Ficha5, User_Ficha6, User_Ficha7, User_Ficha8, User_Ficha9, User_Ficha10, User_Ficha11, User_Ficha12 = Ficha(
    0, 525, Display), Ficha(150, 525, Display), Ficha(300, 525, Display), Ficha(450, 525, Display), Ficha(75, 450,
                                                                                                          Display), Ficha(
    225, 450, Display), Ficha(375, 450, Display), Ficha(525, 450, Display), Ficha(0, 375, Display), Ficha(150, 375,
                                                                                                          Display), Ficha(
    300, 375, Display), Ficha(450, 375, Display)

Player1_pieces = [User_Ficha1, User_Ficha2, User_Ficha3, User_Ficha4, User_Ficha5, User_Ficha6, User_Ficha7,
                  User_Ficha8, User_Ficha9, User_Ficha10, User_Ficha11, User_Ficha12]

Ficha_op1, Ficha_op2, Ficha_op3, Ficha_op4, Ficha_op5, Ficha_op6, Ficha_op7, Ficha_op8, Ficha_op9, Ficha_op10, Ficha_op11, Ficha_op12 = Op_Ficha(
    75, 0, Display), Op_Ficha(225, 0, Display), Op_Ficha(375, 0, Display), Op_Ficha(525, 0, Display), Op_Ficha(0, 75,
                                                                                                               Display), Op_Ficha(
    150, 75, Display), Op_Ficha(300, 75, Display), Op_Ficha(450, 75, Display), Op_Ficha(75, 150, Display), Op_Ficha(225,
                                                                                                                    150,
                                                                                                                    Display), Op_Ficha(
    375, 150, Display), Op_Ficha(525, 150, Display)

Player2_pieces = [Ficha_op1, Ficha_op2, Ficha_op3, Ficha_op4, Ficha_op5,
                  Ficha_op6, Ficha_op7, Ficha_op8, Ficha_op9, Ficha_op10,
                  Ficha_op11, Ficha_op12]

pygame.display.update()


def end_game():
    GameEnded = True
    return GameEnded


def No_pieces(Ending):
    if not Player1_pieces:
        print "*" * 30
        print "Player 2 Won!!"
        Ending = end_game()
        return Ending
    elif not Player2_pieces:
        print "*" * 30
        print "Player 1 Won!!"
        Ending = end_game()
        return Ending


def Wrong_Squares():  # Esta funcion recorre todos los cuadros que son Invalidos para el jugador moverse
    MovesInv = []
    Xposition = 75
    Yposition = 525
    for cicle in range(0, 34):
        MovesInv.append((Xposition, Yposition))
        Xposition += 150
        if cicle == 4 or cicle == 13 or cicle == 21 or cicle == 29:
            Xposition = 0
            Yposition -= 75
        if cicle == 9 or cicle == 17 or cicle == 25:
            Xposition = 75
            Yposition -= 75

    return MovesInv


def Invaible_Moves(click_position, Moves):  # Esta funcion se asegura de que la ficha no se mueva a donde no debe
    Real_position = True_position(click_position[0], click_position[1], Wrong_Squares())
    for every in Moves:
        if every == Real_position:
            return True


# Esta funcion retornara verdadero si el usuario da 2do click en una ficha que es de su mando
def piece_in_the_middle(click_pos):
    if Turn_Player == 1:
        Real_pos = True_position(click_pos[0], click_pos[1], memorize_board())
        for player in Player1_pieces:
            if player.position == Real_pos:
                return True
    else:
        Real_pos = True_position(click_pos[0], click_pos[1], memorize_board())
        for player2 in Player2_pieces:
            if player2.position == Real_pos:
                return True


def memorize_board():  # Recorre todos los cuadros que son validos para moverse
    AviableMoves = []
    Xposition = 0
    Yposition = 525
    for cicle in range(0, 34):
        AviableMoves.append((Xposition, Yposition))
        Xposition += 150
        if cicle == 4 or cicle == 13 or cicle == 21 or cicle == 29:
            Xposition = 75
            Yposition -= 75
        if cicle == 9 or cicle == 17 or cicle == 25:
            Xposition = 0
            Yposition -= 75

    return AviableMoves


def True_position(Xposition, Yposition, Squares):  # Aqui se da la posicion mas acertada en el cuadro
    position = (Xposition, Yposition)
    if position in Squares:
        return position
    for Square in Squares:
        for X in range(Xposition - 75, Xposition):
            if X == Square[0]:
                for Y in range(Yposition - 75, Yposition):
                    if Y == Square[1]:
                        Real_position = Square
                        return Real_position


# Aqui se imprime los caminos que recorrera el usuario
def print_path(First, Second, Path1, Path2):
    if First and Second is None:
        Display.blit(Puntero, Path2)
        pygame.display.flip()
    elif Second and First is None:
        Display.blit(Puntero, Path1)
        pygame.display.flip()
    elif First and Second:
        return
    elif First is None and Second is None:
        Display.blit(Puntero, Path1)
        Display.blit(Puntero, Path2)
        pygame.display.flip()


def Find_path(Position, Lista, Lista2):  # Aqui se imprime los caminos que puede recorrer la ficha
    First = None
    Second = None
    if Turn_Player == 2:
        Alternative1, Alternative2 = Adayacend_moves(Position)
        for player2 in Lista2:
            for player in Lista:
                if player.position == Alternative1 or player2.position == Alternative1:
                    First = True
                elif player.position == Alternative2 or player2.position == Alternative2:
                    Second = True

        print_path(First, Second, Alternative1, Alternative2)
    else:
        Alternative1, Alternative2 = Adayacend_moves(Position)
        for player in Lista:
            for player2 in Lista2:
                if player.position == Alternative1 or player2.position == Alternative1:
                    First = True
                elif player.position == Alternative2 or player2.position == Alternative2:
                    Second = True

        print_path(First, Second, Alternative1, Alternative2)


# Esta funcion hace desaparecer los caminos de la pantalla
def dissapear_path(Path1, Path2, First, Second):
    if First is None and Second is None:
        Display.blit(Cuadro, Path1)
        Display.blit(Cuadro, Path2)
        pygame.display.flip()
    if First and Second is None:
        Display.blit(Cuadro, Path2)
        pygame.display.flip()
    if Second and First is None:
        Display.blit(Cuadro, Path1)
        pygame.display.flip()


def select_piece(position, plataform, Player_List):  # Funcion para seleccionar pieza
    Squares = memorize_board()
    Real_position = True_position(position[0], position[1], Squares)
    for Player in Player_List:
        if Player.position == Real_position:
            plataform.blit(Cuadro, Real_position)
            Player.select_pieces(Real_position[0], Real_position[1], Display)
            pygame.display.flip()


def Adayacend_moves(pos):  # Aqui se retorna las adyacentes de la ficha
    True_pos = True_position(pos[0], pos[1], memorize_board())
    if True_pos is None:
        return None, None
    if Turn_Player == 1:
        Path1 = (True_pos[0] - 75, True_pos[1] - 75)
        Path2 = (True_pos[0] + 75, True_pos[1] - 75)
        return Path1, Path2
    else:
        Path2 = (True_pos[0] + 75, True_pos[1] + 75)
        Path1 = (True_pos[0] - 75, True_pos[1] + 75)
        return Path1, Path2


def Adayacend_of_Adayacend(pos1, pos2):  # Aqui retorna las adyacentes de las adyacentes de la ficha
    if pos1 is None or pos2 is None:
        return None, None
    if Turn_Player == 1:
        Path_to_Eat1 = (pos1[0] - 75, pos1[1] - 75)
        Path_to_Eat2 = (pos2[0] + 75, pos2[1] - 75)
        return Path_to_Eat1, Path_to_Eat2
    else:
        Path_to_Eat1 = (pos1[0] - 75, pos1[1] + 75)
        Path_to_Eat2 = (pos2[0] + 75, pos2[1] + 75)
        return Path_to_Eat1, Path_to_Eat2


def Error_Moves(pos):  # Esta funcion devuelve la ficha a su estado normal antes de ser seleccionada
    Real = True_position(pos[0], pos[1], memorize_board())
    if Turn_Player == 1:
        for player in Player1_pieces:
            if Real == player.position:
                player.after_selection()
                Display.blit(player.image, Real)
                pygame.display.flip()
    else:
        for player2 in Player2_pieces:
            if Real == player2.position:
                player2.after_selection()
                Display.blit(player2.imageop, Real)
                pygame.display.flip()


# Esta funcion hace que la ficha se vuelva Reina
def Transform_Queen():
    if Turn_Player == 1:
        for players in Player1_pieces:
            if players.position[1] == 0:
                players.transform_ficha()
                pygame.display.flip()
    else:
        for players2 in Player2_pieces:
            if players2.position[1] == 525:
                players2.transform_ficha()
                pygame.display.flip()


# Aqui se dibujaran los cuadros para desaparecer los caminos del jugador una vez que cometa un error
def Error_Path_Moves(pos):
    Adayacend1, Adayacend2 = Adayacend_moves(pos)
    First, Second = None, None
    for players in Player1_pieces:
        for players2 in Player2_pieces:
            if Adayacend1 == players2.position or Adayacend1 == players.position:
                First = True
            elif Adayacend2 == players2.position or Adayacend2 == players.position:
                Second = True

    dissapear_path(Adayacend1, Adayacend2, First, Second)


# Esta funcion toma una posicion y checkea si en la lista hay una reina retornara Verdadero
def checking_the_queens(Click_pos):
    if Turn_Player == 1:
        for players in Player1_pieces:
            if players.position == Click_pos:
                if players.queen_status:
                    return True
    else:
        for players2 in Player2_pieces:
            if players2.position == Click_pos:
                if players2.queen_status:
                    return True


# Aqui retornara True si la ficha se mueve hacia atras sin ser Reina
def move_backwards(zpos, zpos2):
    Tposition = True_position(zpos[0], zpos[1], memorize_board())
    Tposition2 = True_position(zpos2[0], zpos2[1], memorize_board())
    if Tposition is None or Tposition2 is None:
        return None, None
    if Turn_Player == 1:
        if checking_the_queens(Tposition):
            return None
        Next_position = (Tposition[0] - 75, Tposition[1] + 75)
        Next_position2 = (Tposition[0] + 75, Tposition[1] + 75)
        if Tposition2 == Next_position or Tposition2 == Next_position2:
            return True
    else:
        if checking_the_queens(Tposition):
            return None
        Next_position = (Tposition[0] - 75, Tposition[1] - 75)
        Next_position2 = (Tposition[0] + 75, Tposition[1] - 75)
        if Tposition2 == Next_position or Tposition2 == Next_position2:
            return True


# Aqui se imprime el camino para comer
def Print_Eating_Path(Empty_Space1, Empty_Space2, Path1, Path2):
    if Empty_Space1 is False and Empty_Space2 is False:
        return False
    if Empty_Space1 is None and Empty_Space2 is None:
        Display.blit(Puntero, Path1)
        Display.blit(Puntero, Path2)
        pygame.display.flip()
    elif Empty_Space1 is False and Empty_Space2 is None:
        Display.blit(Puntero, Path2)
        pygame.display.flip()
    elif Empty_Space1 is None and Empty_Space2 is False:
        Display.blit(Puntero, Path1)
        pygame.display.flip()


# Esta funcion devuelve los caminos traseros de la reina
def back_path(vpos):
    Tpos = True_position(vpos[0], vpos[1], memorize_board())
    if checking_the_queens(Tpos):
        if Turn_Player == 1:
            B_Path1, B_Path2 = (Tpos[0] - 75, Tpos[1] + 75), (Tpos[0] + 75, Tpos[1] + 75)
            return B_Path1, B_Path2
        else:
            B_Path1, B_Path2 = (Tpos[0] - 75, Tpos[1] - 75), (Tpos[0] + 75, Tpos[1] - 75)
            return B_Path1, B_Path2
    else:
        return


# Esta funcion sirve para cuando el usuario que va a comer tiene los espacios ocupados
def Two_paths_ocuped(Eat1, Eat2):
    V1, V2 = None, None
    for players in Player1_pieces:
        for players2 in Player2_pieces:
            if Eat1 == players.position or players2.position == Eat1:
                V1 = False
    for players in Player1_pieces:
        for players2 in Player2_pieces:
            if Eat2 == players2.position or players.position == Eat2:
                V2 = False

    Print_Eating_Path(V1, V2, Eat1, Eat2)


# Esta funcion sirve para cuando el usuario que va a comer tiene uno de los 2 espacios ocupados
def One_Path_Ocuped(Num, Eat1, Eat2):
    if Num == 1:
        for players in Player1_pieces:
            for players2 in Player2_pieces:
                if Eat1 == players.position or players2.position == Eat1:
                    return False

        Print_Eating_Path(None, False, Eat1, Eat2)
    else:
        for players in Player1_pieces:
            for players2 in Player2_pieces:
                if Eat2 == players2.position or players.position == Eat2:
                    return False

        Print_Eating_Path(False, None, Eat1, Eat2)


# Aqui se esta comprovando que los espacios para comer esten ocupados o desocupados
def Proving_Empty_Space(Path1, Path2, Eat1, Eat2):
    if Path1 and Path2:
        Two_paths_ocuped(Eat1, Eat2)
    elif Path1 and Path2 is None:
        One_Path_Ocuped(1, Eat1, Eat2)
    elif Path1 is None and Path2:
        One_Path_Ocuped(2, Eat1, Eat2)
    else:
        return False

def Find_Eating_Queen_Path(Position):
    Tpos = True_position(Position[0], Position[1], memorize_board())
    Path1, Path2 = Adayacend_moves(Position)
    V1, V2, V3, V4 = None, None, None, None
    Eat_Path1, Eat_Path2 = Adayacend_of_Adayacend(Path1, Path2)
    if checking_the_queens(Tpos):
        Path3, Path4 = back_path(Position)
        if Turn_Player == 1:
            Eat_Path3, Eat_Path4 = (Path3[0] - 75, Path3[1] + 75), (Path4[0] + 75, Path4[1] + 75)
            for players2 in Player2_pieces:
                if players2.position == Path1:
                    V1 = True
                if players2.position == Path2:
                    V2 = True
                if players2.position == Path3:
                    V3 = True
                if players2.position == Path4:
                    V4 = True

            if V1 is None and V2 is None and V3 is None and V4 is None:
                return None
            else:
                Proving_Empty_Space(V1, V2, Eat_Path1, Eat_Path2)
                Proving_Empty_Space(V3, V4, Eat_Path3, Eat_Path4)
                return True
        else:
            Path3, Path4 = back_path(Position)
            Eat_Path3, Eat_Path4 = (Path3[0] - 75, Path3[1] - 75), (Path4[0] + 75, Path4[1] - 75)
            for players in Player1_pieces:
                if players.position == Path1:
                    V1 = True
                if players.position == Path2:
                    V2 = True
                if players.position == Path3:
                    V3 = True
                if players.position == Path4:
                    V4 = True

            if V1 is None and V2 is None and V3 is None and V4 is None:
                return None
            else:
                Proving_Empty_Space(V1, V2, Eat_Path1, Eat_Path2)
                Proving_Empty_Space(V3, V4, Eat_Path3, Eat_Path4)
                return True


# Aqui se esta hallando el camino de comer
def Find_Eating_Path(Position):
    if Position is None:
        return None
    A_Path1, A_Path2 = Adayacend_moves(Position)
    E_Path1, E_Path2 = Adayacend_of_Adayacend(A_Path1, A_Path2)
    Ocup_Path1, Ocup_Path2 = None, None
    if Turn_Player == 1:
        for players2 in Player2_pieces:
            if players2.position == A_Path1:
                Ocup_Path1 = True
            elif players2.position == A_Path2:
                Ocup_Path2 = True
        if Ocup_Path1 is None and Ocup_Path2 is None:
            return None
        else:
            Proving_Empty_Space(Ocup_Path1, Ocup_Path2, E_Path1, E_Path2)
            return True
    else:
        for players in Player1_pieces:
            if players.position == A_Path1:
                Ocup_Path1 = True
            elif players.position == A_Path2:
                Ocup_Path2 = True
        if Ocup_Path1 is None and Ocup_Path2 is None:
            return None
        else:
            Proving_Empty_Space(Ocup_Path1, Ocup_Path2, E_Path1, E_Path2)
            return True



# Esta funcion elimina el puntero del comer
def Do_not_Eat(Path):
    for players in Player1_pieces:
        for players2 in Player2_pieces:
            if players.position == Path or players2.position == Path:
                return True

    Display.blit(Cuadro, Path)
    pygame.display.flip()


# Esta funcion recorre la accion que si el jugador decide comer o no
def Eating_Piece(click_pos, Path1, Path2, Path3, Path4, Eat_pos1, Eat_pos2, Eat_pos3, Eat_pos4):
    if Eat_pos1 == click_pos:
        Display.blit(Cuadro, Path1)
        eliminate_path(Path1)
        eliminate_piece(Path1)
        pygame.display.flip()
    elif Eat_pos2 == click_pos:
        Display.blit(Cuadro, Path2)
        eliminate_path(Path2)
        eliminate_piece(Path2)
        pygame.display.flip()
    elif Eat_pos3 == click_pos:
        Display.blit(Cuadro, Path3)
        eliminate_piece(Path3)
        eliminate_path(Path3)
        pygame.display.flip()
    elif Eat_pos4 == click_pos:
        Display.blit(Cuadro, Path4)
        eliminate_piece(Path4)
        eliminate_path(Path4)
        pygame.display.flip()
    elif Path1 == click_pos:
        if Do_not_Eat(Eat_pos2):
            return
    elif Path2 == click_pos:
        if Do_not_Eat(Eat_pos1):
            return
    elif Path3 == click_pos:
        if Do_not_Eat(Eat_pos4):
            return
    elif Path4 == click_pos:
        if Do_not_Eat(Eat_pos3):
            return


# Aqui se ejecuta el movimiento para comer de la ficha
def eat_function(zpos, zpos2):
    Tposition = True_position(zpos[0], zpos[1], memorize_board())
    Tposition2 = True_position(zpos2[0], zpos2[1], memorize_board())
    if Turn_Player == 1:
        Path1, Path2 = Adayacend_moves(zpos)
        Eat_pos1, Eat_pos2 = Adayacend_of_Adayacend(Path1, Path2)
        if checking_the_queens(Tposition):
            B_Path1, B_Path2 = back_path(zpos)
            for players2 in Player2_pieces:
                if players2.position == Path1 or players2.position == Path2 or players2.position == B_Path1 or players2.position == B_Path2:
                    Eat_pos3, Eat_pos4 = (B_Path1[0] - 75, B_Path1[1] + 75), (B_Path2[0] + 75, B_Path2[1] + 75)
                    Eating_Piece(Tposition2, Path1, Path2, B_Path1, B_Path2, Eat_pos1, Eat_pos2, Eat_pos3, Eat_pos4)
        else:
            for players2 in Player2_pieces:
                if Path1 == players2.position or Path2 == players2.position:
                    Eating_Piece(Tposition2, Path1, Path2, None, None, Eat_pos1, Eat_pos2, None, None)
    else:
        Path1, Path2 = Adayacend_moves(zpos)
        Eat_pos1, Eat_pos2 = Adayacend_of_Adayacend(Path1, Path2)
        if checking_the_queens(Tposition):
            B_Path1, B_Path2 = back_path(zpos)
            Eat_pos3, Eat_pos4 = (B_Path1[0] - 75, B_Path1[1] - 75), (B_Path2[0] + 75, B_Path2[1] - 75)
            Eating_Piece(Tposition2, Path1, Path2, B_Path1, B_Path2, Eat_pos1, Eat_pos2, Eat_pos3, Eat_pos4)
        else:
            Eating_Piece(Tposition2, Path1, Path2, None, None, Eat_pos1, Eat_pos2, None, None)


# Esta funcion establece los parametros para ver los caminos de la reina
def Queen_Path_Moves(qpos):
    Tpos = True_position(qpos[0], qpos[1], memorize_board())
    if Turn_Player == 1:
        if checking_the_queens(Tpos):
            B_Path1, B_Path2 = back_path(qpos)
            F_Path1, F_Path2 = Adayacend_moves(qpos)
            Queen_Ocuped_Path_Moves(F_Path1, F_Path2, B_Path1, B_Path2)
        else:
            return
    else:
        if checking_the_queens(Tpos):
            B_Path1, B_Path2 = back_path(qpos)
            F_Path1, F_Path2 = Adayacend_moves(qpos)
            Queen_Ocuped_Path_Moves(F_Path1, F_Path2, B_Path1, B_Path2)
        else:
            return


# Verifica si las piezas estan en el mismo camino de la reina
def Queen_Ocuped_Path_Moves(Path1, Path2, B_Path1, B_Path2):
    Punter1, Punter2, Punter3, Punter4 = None, None, None, None
    for players in Player1_pieces:
        for players2 in Player2_pieces:
            if players.position == Path1 or players2.position == Path1:
                Punter1 = True
            elif players.position == Path2 or players2.position == Path2:
                Punter2 = True
            elif players.position == B_Path1 or players2.position == B_Path1:
                Punter3 = True
            elif players.position == B_Path2 or players2.position == B_Path2:
                Punter4 = True

    print_path(Punter1, Punter2, Path1, Path2)
    print_path(Punter3, Punter4, B_Path1, B_Path2)


# Esta funcion disuelve el camino de la reina
def Queen_Dissapear_Path(qpos):
    Tpos = True_position(qpos[0], qpos[1], memorize_board())
    Path1, Path2 = Adayacend_moves(qpos)
    Empty1, Empty2, Empty3, Empty4 = None, None, None, None
    if checking_the_queens(Tpos):
        if Turn_Player == 1:
            B_Path1, B_Path2 = (Tpos[0] - 75, Tpos[1] + 75), (Tpos[0] + 75, Tpos[1] + 75)
            for players in Player1_pieces:
                for players2 in Player2_pieces:
                    if players.position == Path1 or players2.position == Path1:
                        Empty1 = True
                    elif players.position == Path2 or players2.position == Path2:
                        Empty2 = True
                    elif players.position == B_Path1 or players2.position == B_Path1:
                        Empty3 = True
                    elif players.position == B_Path2 or players2.position == B_Path2:
                        Empty4 = True

            dissapear_path(Path1, Path2, Empty1, Empty2)
            dissapear_path(B_Path1, B_Path2, Empty3, Empty4)
        else:
            B_Path1, B_Path2 = (Tpos[0] - 75, Tpos[1] - 75), (Tpos[0] + 75, Tpos[1] - 75)
            for players in Player1_pieces:
                for players2 in Player2_pieces:
                    if players.position == Path1 or players2.position == Path1:
                        Empty1 = True
                    elif players.position == Path2 or players2.position == Path2:
                        Empty2 = True
                    elif players.position == B_Path1 or players2.position == B_Path1:
                        Empty3 = True
                    elif players.position == B_Path2 or players2.position == B_Path2:
                        Empty4 = True

            dissapear_path(Path1, Path2, Empty1, Empty2)
            dissapear_path(B_Path1, B_Path2, Empty3, Empty4)
    else:
        return


# Esta funcion hace que se elimina la pieza que fue eliminada
def eliminate_path(position):
    Path1, Path2 = Adayacend_moves(position)
    Empty_First, Empty_Second = None, None
    for players in Player1_pieces:
        for players2 in Player2_pieces:
            if players.position == Path1 or players2.position == Path1:
                Empty_First = True
            elif players.position == Path2 or players2.position == Path2:
                Empty_Second = True

    dissapear_path(Path1, Path2, Empty_First, Empty_Second)


# Aqui se eliminara la ficha que sea comida
def eliminate_piece(Position_piece):
    for player in Player1_pieces:
        if player.position == Position_piece:
            player.eat_function()
        if player.position is None:
            Player1_pieces.remove(player)

    for player2 in Player2_pieces:
        if player2.position == Position_piece:
            player2.eat_function()
        if player2.position is None:
            Player2_pieces.remove(player2)


# Esta funcion da a conocer que si la ficha se esta moviendo mas de 1 cuadro
def More_than_1_Moves(position, position2, Moves):
    Real_position = True_position(position[0], position[1], Moves)
    Real_position2 = True_position(position2[0], position2[1], Moves)
    if Find_Eating_Path(position):
        return None
    elif checking_the_queens(Real_position):
        if Find_Eating_Queen_Path(position):
            return None
    if Real_position is None:
        Real_position = True_position(position[0], position[1], Wrong_Squares())
    elif Real_position2 is None:
        Real_position2 = True_position(position2[0], position2[1], Wrong_Squares())
    if Real_position[0] > Real_position2[0]:
        ResultX = Real_position[0] - Real_position2[0]
    else:
        ResultX = Real_position2[0] - Real_position[0]
    if Real_position[1] > Real_position2[1]:
        ResultY = Real_position[1] - Real_position2[1]
    else:
        ResultY = Real_position2[1] - Real_position[1]
    if ResultX >= 150 and ResultY >= 150:
        return True
    else:
        return False

# Esta funcion busca si la ficha puede dar el doble salto
def Find_Path(S_Position):
    if S_Position is None:
        return None
    A_Path1, A_Path2 = Adayacend_moves(S_Position)
    E_Path1, E_Path2 = Adayacend_of_Adayacend(A_Path1, A_Path2)
    Ocup_Path1, Ocup_Path2, Ocuped_Epath1, Ocuped_Epath2 = None, None, None, None
    if Turn_Player == 1:
        for players2 in Player2_pieces:
            if players2.position == A_Path1:
                Ocup_Path1 = True
            if players2.position == A_Path2:
                Ocup_Path2 = True
        if Ocup_Path1 is None and Ocup_Path2 is None:
            return None
        else:
            if Ocup_Path1 and Ocup_Path2 is None:
                for players in Player1_pieces:
                    for players2 in Player2_pieces:
                        if players.position == E_Path1 or players2.position == E_Path1:
                            Ocuped_Epath1 = True
                if Ocuped_Epath1:
                    return False
                else:
                    return True
            if Ocup_Path1 is None and Ocup_Path2:
                for players in Player1_pieces:
                    for players2 in Player2_pieces:
                        if players.position == E_Path2 or players2.position == E_Path2:
                            Ocuped_Epath2 = True
                if Ocuped_Epath2:
                    return False
                else:
                    return True
            if Ocup_Path1 and Ocup_Path2:
                for players in Player1_pieces:
                    for players2 in Player2_pieces:
                        if players.position == E_Path2 or players2.position == E_Path2:
                            Ocuped_Epath2 = True
                        if players.position == E_Path1 or players2.position == E_Path1:
                            Ocuped_Epath1 = True
                if Ocuped_Epath2 and Ocuped_Epath1:
                    return False
                elif Ocuped_Epath2 and Ocuped_Epath1 is None:
                    return True
                elif Ocuped_Epath1 and Ocuped_Epath2 is None:
                    return True
    else:
        for players in Player1_pieces:
            if players.position == A_Path1:
                Ocup_Path1 = True
            if players.position == A_Path2:
                Ocup_Path2 = True
        if Ocup_Path1 is None and Ocup_Path2 is None:
            return None
        elif Ocup_Path1 and Ocup_Path2 is None:
            for players in Player1_pieces:
                for players2 in Player2_pieces:
                    if players.position == E_Path1 or players2.position == E_Path1:
                        Ocuped_Epath1 = True
            if Ocuped_Epath1:
                return False
            else:
                return True
        elif Ocup_Path1 is None and Ocup_Path2:
            for players in Player1_pieces:
                for players2 in Player2_pieces:
                    if players.position == E_Path2 or players2.position == E_Path2:
                        Ocuped_Epath2 = True
            if Ocuped_Epath2:
                return False
            else:
                return True
        elif Ocup_Path1 and Ocup_Path2:
            for players in Player1_pieces:
                for players2 in Player2_pieces:
                    if players.position == E_Path2 or players2.position == E_Path2:
                        Ocuped_Epath2 = True
                    if players.position == E_Path1 or players2.position == E_Path1:
                        Ocuped_Epath1 = True
            if Ocuped_Epath1 and Ocuped_Epath2:
                return False
            elif Ocuped_Epath1 and Ocuped_Epath2 is None:
                return True
            elif Ocuped_Epath1 is None and Ocuped_Epath2:
                return True

# Funcion que autoriza el doble salto en la ficha
def Double_Jump(Player_Eat, Second_pos):
    if Player_Eat:
        if Find_Path(Second_pos):
            return True
        else:
            return False
    else:
        return False



# Esta funcion desaparece los caminos de las fichas si hay 2 caminos para comer
def Disapear_Path_of_Two_Eating_pieces(Position1):
    Path1, Path2 = Adayacend_moves(Position1)
    V1, V2, D1, D2 = None, None, None, None
    Pos_Eat1, Pos_Eat2 = Adayacend_of_Adayacend(Path1, Path2)
    if Turn_Player == 1:
        for players2 in Player2_pieces:
            if players2.position == Path1:
                V1 = True
            elif players2.position == Path2:
                V2 = True
    else:
        for players in Player1_pieces:
            if players.position == Path1:
                V1 = True
            elif players.position == Path2:
                V2 = True

    if V1 and V2:
        for players in Player1_pieces:
            for players2 in Player2_pieces:
                if players.position == Pos_Eat1 or players2.position == Pos_Eat1:
                    D1 = True
                elif players.position == Pos_Eat2 or players2.position == Pos_Eat2:
                    D2 = True

        if D1 and D2 is None:
            Display.blit(Cuadro, Pos_Eat2)
            pygame.display.flip()
        elif D1 is None and D2:
            Display.blit(Cuadro, Pos_Eat1)
            pygame.display.flip()
        else:
            Display.blit(Cuadro, Pos_Eat1)
            pygame.display.flip()
            Display.blit(Cuadro, Pos_Eat2)
            pygame.display.flip()


# Esta funcion switchea los turnos de los jugadores
def Next_Turn(Turn):
    if Turn == 1:
        Turn += 1
        print "*" * 30
        print "Player 2 Turn"
        pygame.display.set_caption("Damas... Players 2 Turn")
        return Turn
    else:
        Turn = 1
        print "*" * 30
        print "Player 1 Turn"
        pygame.display.set_caption("Damas... Players 1 Turn")
        return Turn


# Si el jugador clickea otra ficha que no sea la suyas
def Select_Another_piece(pos1, pos2):
    True_pos2 = True_position(pos2[0], pos2[1], memorize_board())
    if Turn_Player == 1:
        for Space2 in Player2_pieces:
            if Space2.position == True_pos2:
                pygame.display.set_caption("Damas...Movement Invalid...Play Again")
                Error_Moves(pos1)
                Error_Path_Moves(pos1)
                return True
    else:
        for Space in Player1_pieces:
            if Space.position == True_pos2:
                pygame.display.set_caption("Damas...Movement Invalid... Play Again")
                Error_Moves(pos1)
                Error_Path_Moves(pos1)
                return True


# Esta es la funcion que active el movimiento de la pieza
def Movement(tpos1, tpos2):
    Real_Position = True_position(tpos1[0], tpos1[1], memorize_board())
    Real_Position2 = True_position(tpos2[0], tpos2[1], memorize_board())
    if Turn_Player == 1:
        for Player in Player1_pieces:
            if Player.position == Real_Position:
                Display.blit(Cuadro, Real_Position)
                Display.blit(Cuadro, Real_Position2)
                Player.movement_pieces(Real_Position2[0], Real_Position2[1])
                pygame.display.flip()
    else:
        for Player2 in Player2_pieces:
            if Player2.position == Real_Position:
                Display.blit(Cuadro, Real_Position)
                Display.blit(Cuadro, Real_Position2)
                Player2.movement_pieces(Real_Position2[0], Real_Position2[1])
                pygame.display.flip()


# Esta retornara False si la ficha que clickeo el jugador es la de el
def touch_another_piece(Position):
    Tposition = True_position(Position[0], Position[1], memorize_board())
    if Turn_Player == 1:
        for players in Player1_pieces:
            if players.position == Tposition:
                return False

        pygame.display.set_caption("Damas...Movement Invalid..Play Again")
        Error_Path_Moves(Position)
        Error_Moves(Position)
        return True
    else:
        for players2 in Player2_pieces:
            if players2.position == Tposition:
                return False

        pygame.display.set_caption("Damas...Movement Invalid...Play Again")
        Error_Path_Moves(Position)
        Error_Moves(Position)
        return True


# Esta funcion es para seleccion de la fichas
def seleccion_of_pieces(tpos):
    num_Real = True_position(tpos[0], tpos[1], memorize_board())
    Display.blit(Cuadro, num_Real)
    if Turn_Player == 1:
        select_piece(tpos, Display, Player1_pieces)
        for player in Player1_pieces:
            if player.position == num_Real:
                Find_path(tpos, Player1_pieces, Player2_pieces)
    else:
        select_piece(tpos, Display, Player2_pieces)
        for player2 in Player2_pieces:
            if player2.position == num_Real:
                Find_path(tpos, Player1_pieces, Player2_pieces)


Array_of_Positions = []
Click_Numbers = 1

while not EndGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EndGame = end_game()

        if pygame.mouse.get_pressed()[0] == 1:
            if Click_Numbers == 1:
                pos = pygame.mouse.get_pos()
                if touch_another_piece(pos):
                    Array_of_Positions = []
                    Click_Numbers = 1
                else:
                    Queen_Path_Moves(pos)
                    Find_Eating_Queen_Path(pos)
                    Find_Eating_Path(pos)
                    Array_of_Positions.append(pos)
                    seleccion_of_pieces(pos)
                    Click_Numbers += 1
            else:
                pos2 = pygame.mouse.get_pos()
                if Select_Another_piece(Array_of_Positions[0], pos2):
                    Array_of_Positions = []
                    Click_Numbers = 1
                else:
                    Decision1 = Invaible_Moves(pos2, Wrong_Squares())
                    Decision2 = More_than_1_Moves(Array_of_Positions[0], pos2, memorize_board())
                    Decision3 = piece_in_the_middle(pos2)
                    Decision4 = move_backwards(Array_of_Positions[0], pos2)
                    if Decision1 or Decision2 or Decision3 or Decision4:
                        pygame.display.set_caption("Damas... Movement Invalid Play Again")
                        Error_Path_Moves(Array_of_Positions[0])
                        Error_Moves(Array_of_Positions[0])
                        Array_of_Positions = []
                        Click_Numbers = 1
                    else:
                        Queen_Dissapear_Path(Array_of_Positions[0])
                        Disapear_Path_of_Two_Eating_pieces(Array_of_Positions[0])
                        Player_Eat = Find_Path(Array_of_Positions[0])
                        eat_function(Array_of_Positions[0], pos2)
                        Movement(Array_of_Positions[0], pos2)
                        Transform_Queen()
                        eliminate_path(Array_of_Positions[0])
                        EndGame = No_pieces(EndGame)
                        Double = Double_Jump(Player_Eat, pos2)
                        Array_of_Positions = []
                        Click_Numbers = 1
                        if Double:
                            pygame.display.set_caption("Damas...Doble Salto Requerido")
                            pass
                        else:
                            Turn_Player = Next_Turn(Turn_Player)