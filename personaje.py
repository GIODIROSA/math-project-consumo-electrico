import pygame
import constantes

class Personaje:
    def __init__(self, x, y, animaciones):
        self.x = x
        self.y = y
        self.size = 20
        self.inventory = {"valor" : 0}
        self.animaciones = animaciones
        # imagen de la animación que se está mostrando actualmente
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.flip = False

    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0
            
                

    def draw (self, ventana):
        # se construye el personaje y se reemplaza
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        ventana.blit(imagen_flip, (self.x, self.y,self.size,self.size))
        #pygame.draw.rect(ventana,constantes.COLOR_NEGRO, (self.x, self.y,self.size,self.size))

    def move(self, dx, dy, mundo):
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

        new_x = self.x + dx
        new_y = self.y + dy

        for elemento in mundo.elementos:
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
        for elemento in mundo.elementos:
            if self.is_near(elemento):
                if elemento.usar():
                    self.inventory["valor"] += 1
                    if elemento.valor == 0:
                        #elemento.imagen = pygame.image.load('imagenes', 'refri1.png')
                        mundo.elemento.remove(elemento)
                return