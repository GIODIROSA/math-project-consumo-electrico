import pygame
import constantes
from elemento import Refrigerador
import random
import os


class Mundo:
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        self.elemento = [Refrigerador(random.randint(0, ancho-40),random.randint(0, alto-40)) for _ in range(1)]

        grass_piso = os.path.join('imagenes','pisovf.png')
        self.grass_image = pygame.image.load(grass_piso).convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (constantes.GRASS, constantes.GRASS))


    def draw(self, ventana):
        for y in range(0,self.alto, constantes.GRASS):
            for x in range(0,self.ancho, constantes.GRASS):
                ventana.blit (self.grass_image, (x, y))

        
        for elemento in self.elemento:
            elemento.draw(ventana)

    def draw_inventory(self, ventana, personaje):
        font = pygame.font.Font(None, 36)
        elemento_text = font.render(f"Gasto Refrigerador: {personaje.inventory['valor']}",
                                True, constantes.COLOR_BLANCO)
        ventana.blit(elemento_text, (10, 10))          