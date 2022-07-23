import pygame
from pygame.locals import *
from sys import exit
from t1 import Click

class Backend:
    def __init__(self):
        self.input_active = True
        self.total = 0
        self.num = 0
        self.ocult = ''
        self.text = ''
        self.sinal = '+'      
        self.tot = 0  
        
    def isthing(self, valor):
        if valor == '+' or valor == '-' or valor == '*' or valor == '/' or valor == '=' or valor == '^':
            return True
        else:
            return False

    def operacoes(self):
        if self.sinal == '+':
            self.num = int(self.ocult)
            self.total += self.num
            self.ocult = ''
        elif self.sinal == '-':
            self.num = int(self.ocult)
            self.total -= self.num
            self.ocult = ''
        elif self.sinal == '*':
            self.num = int(self.ocult)
            self.total *= self.num
            self.ocult = ''   
        elif self.sinal == '/':
            self.num = int(self.ocult)
            self.total /= self.num
            self.ocult = ''
        elif self.sinal == '^':
            self.num = int(self.ocult)
            self.total **= self.num
            self.ocult = ''    
        
    def running(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Click().clicks()

                self.input_active = True
                self.total = 0
                self.num = 0
                self.ocult = ''
                self.text = ''
                self.sinal = '+'      
                self.tot = 0  
            elif event.type == pygame.KEYDOWN and self.input_active:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    if self.isthing(self.text[-1]) == False:
                        self.text = self.text[:-1]
                        self.ocult = self.ocult[:-1]
                else:
                    if event.unicode.isnumeric() or self.isthing(event.unicode):
                        if self.text == '' and event.unicode == '+':  #nao pode comecar com sinal 
                            pass
                        elif len(self.text) > 0 and self.isthing(self.text[-1]) and self.isthing(event.unicode):  #digitar apenas um sinal 
                            pass
                        else:
                            if self.isthing(event.unicode) and len(self.text) > 0: #se for digitado um sinal
                                self.operacoes()
                                self.tot = self.total
                                self.sinal = event.unicode
                                if self.sinal == '=':
                                    self.input_active = False
                                    self.text += f' = {self.total}'
                            elif event.unicode.isnumeric():  #se for digitado numero
                                self.ocult += event.unicode
                            if event.unicode != '=':  #para não mostrar o sinal de '=' no terminal da calculadora
                                self.text += event.unicode

    def run(self):
        pass
