import pygame
class Ficha:
    def __init__(self, Color):
        self.color = Color
        if self.color == "Naranja":
            self.image = pygame.image.load("./Imagenes/Ficha_Naranja.png")
        else:
            self.image = pygame.image.load("./Imagenes/Ficha_Azul.png")
        self.position = None
        self.queen_status = False

    @staticmethod
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

    @staticmethod
    def Adayacend_moves(pos, Turn_Player):  # Aqui se retorna las adyacentes de la ficha
        True_pos = Ficha.True_position(pos[0], pos[1], Ficha.Moves_Squares())
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

    @staticmethod
    def Adayacend_of_Adayacend(pos1, pos2, Turn_Player):  # Aqui retorna las adyacentes de las adyacentes de la ficha
        if pos1 is None or pos2 is None:
            return None, None
        if Turn_Player == 1:
            Path_to_Eat1 = (pos1[0] - 75, pos1[1] - 75)
            Path_to_Eat2 = (pos2[0] + 75, pos2[1] - 75)
            if Path_to_Eat1[0] < 0:
                Path_to_Eat1 = 1
            elif Path_to_Eat2[0] > 600:
                Path_to_Eat2 = 1
            return Path_to_Eat1, Path_to_Eat2
        else:
            Path_to_Eat1 = (pos1[0] - 75, pos1[1] + 75)
            Path_to_Eat2 = (pos2[0] + 75, pos2[1] + 75)
            if Path_to_Eat1[0] < 0:
                Path_to_Eat1 = 1
            elif Path_to_Eat2[0] > 600:
                Path_to_Eat2 = 1
            return Path_to_Eat1, Path_to_Eat2

    @staticmethod
    def Moves_Squares():  # Recorre todos los cuadros que son validos para moverse
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


    @staticmethod
    def Wrong_Squares():
        List_W_Moves = []
        Xposition = 0
        Yposition = 525
        for cicle in range(0, 34):
            List_W_Moves.append((Xposition, Yposition))
            Xposition += 150
            if cicle == 4 or cicle == 13 or cicle == 21 or cicle == 29:
                Xposition = 0
                Yposition -= 75
            if cicle == 9 or cicle == 17 or cicle == 25:
                Xposition = 75
                Yposition -= 75
        return List_W_Moves


    def Transformando_Ficha_Reina(self, ubication="./Imagenes/Ficha_Naranja_Reina.png"):
        if self.color == "Naranja":
            self.image = pygame.image.load(ubication)
        else:
            self.image = pygame.image.load("./Imagenes/Ficha_Azul_Reina.png")
        self.Display.blit(self.image, self.position)
        self.queen_status = True

    def select_pieces(self, Xposition, Yposition, Display):
        if self.queen_status:
            if self.color == "Naranja":
                self.image = pygame.image.load("./Imagenes/Seleccion_Ficha_Naranja_Reina.png")
            else:
                self.image = pygame.image.load("./Imagenes/Seleccion_Ficha_Azul_Reina.png")
            Display.blit(self.image, (Xposition, Yposition))
            pygame.display.flip()
        else:
            if self.color == "Naranja":
                self.image = pygame.image.load("./Imagenes/Seleccion_Ficha_Naranja.png")
            else:
                self.image = pygame.image.load("./Imagenes/Seleccion_de_Ficha_Azul.png")
            Display.blit(self.image, (Xposition, Yposition))
            pygame.display.flip()

    def movement_pieces(self, Xposition, Yposition):
        self.after_selection()
        self.position = (Xposition, Yposition)
        self.Display.blit(self.image, self.position)
        pygame.display.flip()

    def after_selection(self, ubication="./Imagenes/Ficha_Naranja.png"):
        if self.queen_status:
            if self.color == "Naranja":
                self.image = pygame.image.load("./Imagenes/Ficha_Naranja_Reina.png")
                pygame.display.flip()
            else:
                self.image = pygame.image.load("./Imagenes/Ficha_Azul_Reina.png")
                pygame.display.flip()
        else:
            if self.color == "Naranja":
                self.image = pygame.image.load(ubication)
                pygame.display.flip()
            else:
                self.image = pygame.image.load("./Imagenes/Ficha_Azul.png")
                pygame.display.flip()

    def eat_function(self):
        self.position = None


# class Op_Ficha(Ficha):
#     def __init__(self, Xposition, Yposition, Display):
#         self.imageop = pygame.image.load("./Imagenes/Ficha_Azul.png")
#         self.Display = Display
#         self.position = (Xposition, Yposition)
#         self.queen_status = False
#         self.Display.blit(self.imageop, self.position)
#
#     def select_pieces(self, Xposition, Yposition, Display):
#         if self.queen_status:
#             self.imageop = pygame.image.load("./Imagenes/Seleccion_Ficha_Azul_Reina.png")
#             Display.blit(self.imageop, (Xposition,Yposition))
#             pygame.display.flip()
#         else:
#             self.imageop = pygame.image.load("./Imagenes/Seleccion_de_Ficha_Azul.png")
#             Display.blit(self.imageop, (Xposition, Yposition))
#             pygame.display.flip()
#
#     def movement_pieces(self, Xposition, Yposition):
#         self.after_selection()
#         self.position = (Xposition, Yposition)
#         self.Display.blit(self.imageop, self.position)
#         pygame.display.flip()
#
#     def transform_ficha(self, ubication="./Imagenes/Ficha_Azul_Reina.png"):
#         self.imageop = pygame.image.load(ubication)
#         self.Display.blit(self.imageop, self.position)
#         self.queen_status = True
#
#     def after_selection(self, ubication="./Imagenes/Ficha_Azul.png"):
#         if self.queen_status:
#             self.imageop = pygame.image.load("./Imagenes/Ficha_Azul_Reina.png")
#             pygame.display.flip()
#         else:
#             self.imageop = pygame.image.load(ubication)
#             pygame.display.flip()
#
#     def eat_function(self):
#         self.position = None

# class Op_Ficha:
#     def __init__(self, Xposition, Yposition, Display):
#         self.imageop = pygame.image.load("Ficha_Azul.png")
#         self.Display = Display
#         self.position = (Xposition, Yposition)
#         self.queen_status = False
#         self.Display.blit(self.imageop, self.position)
#
#     def select_pieces(self, Xposition, Yposition, Display):
#         self.imageop = pygame.image.load("Seleccion_de_Ficha_Azul.png")
#         Display.blit(self.imageop, (Xposition, Yposition))
#         pygame.display.flip()
#
#     def movement_pieces(self, Xposition, Yposition):
#         self.after_selection()
#         self.position = (Xposition, Yposition)
#         self.Display.blit(self.imageop, self.position)
#         pygame.display.flip()
#
#     def transform_ficha(self, ubication="Ficha_Azul_Reina.png"):
#         self.imageop = pygame.image.load(ubication)
#         self.Display.blit(self.imageop, self.position)
#         self.queen_status = True
#
#     def after_selection(self, ubication="Ficha_Azul.png"):
#         self.imageop = pygame.image.load(ubication)
#         pygame.display.flip()
#
#     def eat_function(self):
#         self.position = None


class Tablero:
    def __init__(self, Display):
        self.board_image = pygame.image.load("./Imagenes/tablero_original.png")
        self.board = pygame.transform.scale(self.board_image, (600, 600))
        Display.blit(self.board, (0, 0))
