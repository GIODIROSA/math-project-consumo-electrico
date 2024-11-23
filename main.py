import pygame
import sys
import constantes
from personaje import Personaje
from mundo import Mundo

#inicializar pygame
pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))
pygame.display.set_caption("CRECE")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w * scale, h * scale))
    return nueva_imagen

animaciones = []
for i in range(9):
    img = pygame.image.load(f"assets/images/characters/player//player_{i}.png")
    img= escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)

def main():
    clock = pygame.time.Clock()
    mundo = Mundo(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
    personaje = Personaje(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2, animaciones)

    #bucle del juego
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    personaje.interact(mundo)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            personaje.move(-5,0 , mundo)
        if keys[pygame.K_RIGHT]:
            personaje.move(5,0, mundo)
        if keys[pygame.K_UP]:
            personaje.move(0,-5, mundo)
        if keys[pygame.K_DOWN]:
            personaje.move(0,5, mundo)

        mundo.draw(ventana)
        personaje.update()
        personaje.draw(ventana)
        mundo.draw_inventory(ventana, personaje)

        pygame.display.flip()
        clock.tick(60)

if __name__== "__main__":
    main()
        













