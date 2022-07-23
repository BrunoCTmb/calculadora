import pygame

class Layout:
    def __init__(self):
        pass

    def text(self, txt,size,color):
        font = pygame.font.SysFont('arial', size, False, False)
        texto = f'{txt}'
        final_text = font.render(texto, True, color)
        return final_text