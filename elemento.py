import pygame
import os
import constantes

class Electrodomestico:
    def __init__(self, x, y, imagen, valor):
        self.x = x
        self.y = y
        self.valor = valor
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constantes.GRASS, constantes.ELEMENTOS))
        self.size = self.image.get_width()

    def draw(self, ventana):
        ventana.blit(self.image, (self.x, self.y))

    def usar(self):
        if self.valor >= 0:
            self.valor += 1
            return True
        return False

class Refrigerador(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

class Televisor(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

class Lavadora(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

class Calefactor(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

class AireAcondicionado(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)
