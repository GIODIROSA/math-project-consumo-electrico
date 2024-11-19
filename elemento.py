import pygame
import constantes
import os


class Refrigerador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.valor = 5

        refri1 = os.path.join('imagenes','refri1.png')
        self.image = pygame.image.load(refri1).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constantes.GRASS, constantes.ELEMENTOS))
        self.size = self.image.get_width()

    def draw(self, ventana):
        ventana.blit (self.image, (self.x, self.y))

    def chop(self):
        if self.valor > 0:
            self.valor -= 1
            return True
        return False
