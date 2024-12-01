import pygame
import constantes

def pantalla_inicio(ventana):
    letras_titulo = pygame.font.Font(None, 74)
    letras_botones = pygame.font.Font(None, 36)
    letras_instrucciones = pygame.font.Font(None, 24) # Fuente para las instrucciones

    titulo = letras_titulo.render("Bienvenido a CRECE", True, constantes.COLOR_BLANCO)
    texto_jugar = letras_botones.render("Iniciar", True, constantes.COLOR_NEGRO)
    texto_salir = letras_botones.render("Salir", True, constantes.COLOR_NEGRO)


    # Instrucciones
    instrucciones_movimiento = letras_instrucciones.render("Usa las flechas para moverte", True, constantes.COLOR_BLANCO)
    instrucciones_interaccion = letras_instrucciones.render("Presiona 'E' para sumar un dia de consumo", True, constantes.COLOR_BLANCO)
    instrucciones_mensaje = letras_instrucciones.render("¡Aprendamos a reducir el consumo eléctrico en casa!", True, constantes.COLOR_VERDE)

    boton_jugar = pygame.Rect(constantes.ANCHO_VENTANA / 2 - 100, 
                            constantes.ALTO_VENTANA / 2 - 50, 200, 50)

    boton_salir = pygame.Rect(constantes.ANCHO_VENTANA / 2 - 100,
                            constantes.ALTO_VENTANA / 2 + 50, 200, 50)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    return "Jugar"
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    exit()

        # Rellenar fondo
        ventana.fill(constantes.COLOR_BG)  # Asegúrate que COLOR_BG no sea negro

        # Dibujar el título
        ventana.blit(titulo, (constantes.ANCHO_VENTANA / 2 - titulo.get_width() / 2, 100))

        # Dibujar los botones
        pygame.draw.rect(ventana, constantes.COLOR_VERDE, boton_jugar)
        pygame.draw.rect(ventana, constantes.COLOR_GRAFITO, boton_salir)

        # Dibujar texto en los botones
        ventana.blit(texto_jugar, (boton_jugar.x + boton_jugar.width / 2 - texto_jugar.get_width() / 2,
                                boton_jugar.y + boton_jugar.height / 2 - texto_jugar.get_height() / 2))
        ventana.blit(texto_salir, (boton_salir.x + boton_salir.width / 2 - texto_salir.get_width() / 2,
                                boton_salir.y + boton_salir.height / 2 - texto_salir.get_height() / 2))
        
        # Dibujar las instrucciones
        ventana.blit(instrucciones_movimiento, (constantes.ANCHO_VENTANA / 2 - instrucciones_movimiento.get_width() / 2, 
                                                constantes.ALTO_VENTANA / 2 + 150))
        ventana.blit(instrucciones_interaccion, (constantes.ANCHO_VENTANA / 2 - instrucciones_interaccion.get_width() / 2, 
                                                 constantes.ALTO_VENTANA / 2 + 180))
        ventana.blit(instrucciones_mensaje, (constantes.ANCHO_VENTANA / 2 - instrucciones_mensaje.get_width() / 2, 
                                             constantes.ALTO_VENTANA / 2 + 210))

        pygame.display.flip()
