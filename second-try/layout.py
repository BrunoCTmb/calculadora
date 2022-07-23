import pygame

class Layout:
    def __init__(self):
        pass

    def terminal(self, surf):
        borda = pygame.draw.rect(surf, ('black'), (50,10, 470, 120))
        t = pygame.draw.rect(surf, (100,100,100), (60,20, 450, 100))

    def buttons(self, surf):
        x = 50
        y = 160
        #bg = pygame.draw.rect(surf, ('black'), (10,150, 580, 400))

        for coluna in range(5):
            for linha in range(4):
                b1 = pygame.draw.rect(surf, ('blue'), (x,y,88,85))
                y += 88+10
            y = 160
            x += 85+10

    def text(self, txt,size,color):
        font = pygame.font.SysFont('cooper', size, False, False)
        texto = f'{txt}'
        final_text = font.render(texto, True, color)
        return final_text

    def run(self,s):
        self.terminal(s)
        self.buttons(s)