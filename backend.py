import pygame as pg
import sys
from pygame.locals import *

class Back:
    def __init__(self):
        self.terminal_text = ''   #texto inicial do terminal da calculadora
        self.input_mode = True    #situacao do input: ativo ou desativado

    def running(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.input_mode = True
                self.terminal_text = ''
            elif event.type == pg.KEYDOWN and self.input_mode == True:
                if event.key == pg.K_RETURN:
                    self.input_mode = False
                elif event.key == pg.K_BACKSPACE:
                    terminal_text = terminal_text[:-1]
                else:
                    self.terminal_text += event.unicode

        return self.terminal_text

    def run(self):
        pass