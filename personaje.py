import pygame
import constantes

class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.inventory = {"valor" : 0}

    def draw (self, ventana):
        pygame.draw.rect(ventana,constantes.COLOR_NEGRO, (self.x, self.y,self.size,self.size))

    def move(self, dx, dy, mundo):
        new_x = self.x + dx
        new_y = self.y + dy

        for elemento in mundo.elemento:
            if self.check_collision(new_x, new_y, elemento):
                return
            
        self.x = new_x
        self.y = new_y
        self.x = max(0, min(self.x, constantes.ANCHO_VENTANA - self.size))
        self.y = max(0, min(self.y, constantes.ALTO_VENTANA - self.size))

    def check_collision(self, x, y, obj):
        return (x < obj.x + obj.size and x + self.size > obj.x and y < obj.y + obj.size and
                y + self.size > obj.y)

    def is_near(self, obj):
        return (abs(self.x - obj.x)<= (self.size + obj.size) and
                abs(self.y - obj.y)<= (self.size + obj.size))
    
    
    def interact(self, mundo):
        for elemento in mundo.elemento:
            if self.is_near(elemento):
                if elemento.chop():
                    self.inventory["valor"] += 1
                    if elemento.valor == 0:
                        #elemento.imagen = pygame.image.load('imagenes', 'refri1.png')
                        mundo.elemento.remove(elemento)
                return