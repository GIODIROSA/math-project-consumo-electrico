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
        #if self.valor >= 0:
        self.valor += 1
        return True
        #return False

class Refrigerador(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri2.png')
        super().__init__(x, y, imagen, valor=0)

    def usar(self):
        self.valor += 256
        print(f"Refrigerador valor: {self.valor}")
        return True

class Televisor(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

    def usar(self):
        self.valor += 50
        print(f"Televisor valor: {self.valor}")
        return True

class Lavadora(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

    def usar(self):
        self.valor += 30
        print(f"Lavadora valor: {self.valor}")
        return True

class Calefactor(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

    def usar(self):
        self.valor += 2
        print(f"Calefactor valor: {self.valor}")
        return True

class AireAcondicionado(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

    def usar(self):
        self.valor += 2
        print(f"AireAcondicionado valor: {self.valor}")
        return True
