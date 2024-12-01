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
        imagen = os.path.join('imagenes', 'refri1.png')
        super().__init__(x, y, imagen, valor=0)

    def usar(self):
        self.valor += 40*192/30 #cantidad kwh * valor kwh / dias del mes
        print(f"Refrigerador valor: {self.valor}")
        return True


class Televisor(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'televisor.gif')
        super().__init__(x, y, imagen, valor=0)


    def usar(self):
        self.valor += 130*192/30 #cantidad kwh * valor kwh / dias del mes
        print(f"Televisor valor: {self.valor}")
        return True



class Lavadora(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'lavadora.png')
        super().__init__(x, y, imagen, valor=0)


    def usar(self):
        self.valor += 70*192/8 #cantidad kwh * valor kwh / dias posible uso mensual(2 veces a la semana)
        print(f"Lavadora valor: {self.valor}")
        return True


class Calefactor(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'calefactor.png')
        super().__init__(x, y, imagen, valor=0)


    def usar(self):
        self.valor += 350*192/30 #cantidad kwh * valor kwh / dias del mes
        print(f"Calefactor valor: {self.valor}")
        return True


class AireAcondicionado(Electrodomestico):
    def __init__(self, x, y):
        imagen = os.path.join('imagenes', 'airea.png')
        super().__init__(x, y, imagen, valor=0)


    def usar(self):
        self.valor += 320*192/30 #cantidad kwh * valor kwh / dias del mes
        print(f"AireAcondicionado valor: {self.valor}")
        return True

