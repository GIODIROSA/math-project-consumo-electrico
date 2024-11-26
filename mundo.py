import pygame
import constantes
from elemento import Refrigerador, Televisor, Lavadora, Calefactor, AireAcondicionado
import random
import os

class Mundo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

      
        self.elementos = []

        # Método para agregar elementos sin colisiones
        self.agregar_elemento(Refrigerador)
        self.agregar_elemento(Televisor)
        self.agregar_elemento(Lavadora)
        self.agregar_elemento(Calefactor)
        self.agregar_elemento(AireAcondicionado)


        grass_piso = os.path.join('imagenes', 'floor.png')
        self.grass_image = pygame.image.load(grass_piso).convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (constantes.GRASS, constantes.GRASS))



    def agregar_elemento(self, clase_elemento):
        intentos = 0
        max_intentos = 100 # Limitar el número de intentos para evitar un bucle infinito
        while intentos < max_intentos:
            x = random.randint(0, self.ancho - 40)
            y = random.randint(0, self.alto - 40)
            nuevo_elemento = clase_elemento(x, y)
            
            if not any(self.check_collision(nuevo_elemento, elemento) for elemento in self.elementos):
                self.elementos.append(nuevo_elemento)
                break
            
            intentos += 1
            
    def check_collision(self, elem1, elem2):
        return (elem1.x < elem2.x + elem2.size and
                elem1.x + elem1.size > elem2.x and
                elem1.y < elem2.y + elem2.size and
                elem1.y + elem1.size > elem2.y)


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
        