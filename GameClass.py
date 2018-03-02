import pygame
class Board:
    def __init__(self):
        self.image = pygame.image.load('./Imagenes/Cuadro.png')
        self.board = pygame.transform.scale(self.image, (600, 600))
        self.display = pygame.display.set_mode((600, 600))
    
    def displayBoard(self):
        return self.display.blit(self.board, (0, 0))


class Piece:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.fposition = None
        self.isQueen = False

    def definePos(self, Xpos, Ypos):
        self.fposition = (Xpos, Ypos)

    def crownPiece(self):
        self.isQueen = True

    def eatFunction(self):
        self.fposition = None


