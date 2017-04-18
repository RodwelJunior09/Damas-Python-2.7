import pygame


class Ficha:
    def __init__(self, Xposition, Yposition, Display):
        self.image = pygame.image.load("./Imagenes/Ficha_Naranja.png")
        self.position = (Xposition, Yposition)
        self.Display = Display
        self.Display.blit(self.image, self.position)
        self.queen_status = False


    def transform_ficha(self, ubication="./Imagenes/Ficha_Naranja_Reina.png"):
        self.image = pygame.image.load(ubication)
        self.Display.blit(self.image, self.position)
        self.queen_status = True

    def select_pieces(self, Xposition, Yposition, Display):
        if self.queen_status:
            self.image = pygame.image.load("./Imagenes/Seleccion_Ficha_Naranja_Reina.png")
            Display.blit(self.image, (Xposition, Yposition))
            pygame.display.flip()
        else:
            self.image = pygame.image.load("./Imagenes/Seleccion_Ficha_Naranja.png")
            Display.blit(self.image, (Xposition, Yposition))
            pygame.display.flip()

    def movement_pieces(self, Xposition, Yposition):
        self.after_selection()
        self.position = (Xposition, Yposition)
        self.Display.blit(self.image, self.position)
        pygame.display.flip()

    def after_selection(self, ubication="./Imagenes/Ficha_Naranja.png"):
        if self.queen_status:
            self.image = pygame.image.load("./Imagenes/Ficha_Naranja_Reina.png")
            pygame.display.flip()
        else:
            self.image = pygame.image.load(ubication)
            pygame.display.flip()

    def eat_function(self):
        self.position = None


class Op_Ficha(Ficha):
    def __init__(self, Xposition, Yposition, Display):
        self.imageop = pygame.image.load("./Imagenes/Ficha_Azul.png")
        self.Display = Display
        self.position = (Xposition, Yposition)
        self.queen_status = False
        self.Display.blit(self.imageop, self.position)

    def select_pieces(self, Xposition, Yposition, Display):
        if self.queen_status:
            self.imageop = pygame.image.load("./Imagenes/Seleccion_Ficha_Azul_Reina.png")
            Display.blit(self.imageop, (Xposition,Yposition))
            pygame.display.flip()
        else:
            self.imageop = pygame.image.load("./Imagenes/Seleccion_de_Ficha_Azul.png")
            Display.blit(self.imageop, (Xposition, Yposition))
            pygame.display.flip()

    def movement_pieces(self, Xposition, Yposition):
        self.after_selection()
        self.position = (Xposition, Yposition)
        self.Display.blit(self.imageop, self.position)
        pygame.display.flip()

    def transform_ficha(self, ubication="./Imagenes/Ficha_Azul_Reina.png"):
        self.imageop = pygame.image.load(ubication)
        self.Display.blit(self.imageop, self.position)
        self.queen_status = True

    def after_selection(self, ubication="./Imagenes/Ficha_Azul.png"):
        if self.queen_status:
            self.imageop = pygame.image.load("./Imagenes/Ficha_Azul_Reina.png")
            pygame.display.flip()
        else:
            self.imageop = pygame.image.load(ubication)
            pygame.display.flip()

    def eat_function(self):
        self.position = None

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
