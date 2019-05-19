import pygame

class Ficha: 
    def __init__(self, player):
        self.sprite = None
        self.position = None
        self.queen = False
        self.player = player
        if self.player == 1:
            self.sprite = pygame.image.load("./Imagenes/Ficha_Naranja.png")
        elif self.player == 2:
            self.sprite = pygame.image.load("./Imagenes/Ficha_Azul.png")
    
    def selected_piece(self):
        if self.player == 1:
            self.sprite = pygame.image.load("./Imagenes/Seleccion_Ficha_Naranja.png")
        elif self.player == 2:
            self.sprite = pygame.image.load("./Imagenes/Seleccion_de_ficha_Azul.png")
            
    def path_piece(self):
        if self.player == 1:
            path1 = (self.position[0] - 75, self.position[1] - 75)
            path2 = (self.position[0] + 75, self.position[1] - 75)
            return (path1, path2)
        elif self.player == 2:
            path1 = (self.position[0] + 75, self.position[1] + 75)
            path2 = (self.position[0] - 75, self.position[1] + 75)    
            return (path1, path2)
    
    def move_piece(self, xPos, yPos, available_moves):
        if (xPos, yPos) in available_moves:
            self.position = (xPos, yPos)
        else: 
            print("The new position is invalid")

    def eliminate(self):
        self.position = None

    

