from GameClass import *
from MainGameFunctions import *

engine = pygame
engine.init()
Board = Board()
# All the variables Inicialize
EndGame = False
Board.displayBoard()
setDiferentCaption('Damas... Players 1 Turn', engine)

while not EndGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EndGame = endGame(EndGame)