import pygame
import constantes
from elemento import Refrigerador, Televisor, Lavadora, Calefactor, AireAcondicionado
import random
import os

class Mundo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

      
        self.elementos = [
            Refrigerador(random.randint(0, ancho - 40), random.randint(0, alto - 40)),
            Televisor(random.randint(0, ancho - 40), random.randint(0, alto - 40)),
            Lavadora(random.randint(0, ancho - 40), random.randint(0, alto - 40)),
            Calefactor(random.randint(0, ancho - 40), random.randint(0, alto - 40)),
            AireAcondicionado(random.randint(0, ancho - 40), random.randint(0, alto - 40)),
        ]

        grass_piso = os.path.join('imagenes', 'floor.png')
        self.grass_image = pygame.image.load(grass_piso).convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (constantes.GRASS, constantes.GRASS))

    def draw(self, ventana):
        # Dibujar el piso
        for y in range(0, self.alto, constantes.GRASS):
            for x in range(0, self.ancho, constantes.GRASS):
                ventana.blit(self.grass_image, (x, y))

        # Dibujar todos los elementos
        for elemento in self.elementos:
            elemento.draw(ventana)

    def draw_inventory(self, ventana, personaje):
        font = pygame.font.Font(None, 18)
        start_y = 10  
        spacing = 20  


        total_valor = 0

    
        for i, elem in enumerate(self.elementos):
            texto_inventario = f"{type(elem).__name__}: {elem.valor}"
            elemento_text = font.render(texto_inventario, True, constantes.COLOR_BLANCO)
            ventana.blit(elemento_text, (10, start_y + i * spacing))
           
            total_valor += elem.valor

        
        total_texto = f"Total Valor: {total_valor}"
        total_text = font.render(total_texto, True, constantes.COLOR_BLANCO)
        ventana.blit(total_text, (10, start_y + len(self.elementos) * spacing))
        