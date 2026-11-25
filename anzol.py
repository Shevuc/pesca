
import pygame
from settings import *


class Anzol:

    def __init__(self):
        self.x = 0
        self.y = ANZOL_Y_INICIAL
        self.estado = "parado"

    def lancar(self, barco):

        if self.estado == "parado":
            self.x = barco.rect.centerx
            self.estado = "descer"

    def update(self, barco):

        if self.estado == "parado":
            self.x = barco.rect.centerx
            self.y = ANZOL_Y_INICIAL

        elif self.estado == "descer":

            self.y += VELOCIDADE_ANZOL

            if self.y >= ANZOL_Y_LIMITE:
                self.estado = "subir"

        elif self.estado == "subir":

            self.y -= VELOCIDADE_ANZOL

            if self.y <= ANZOL_Y_INICIAL:
                self.estado = "parado"

    def subir(self):
        self.estado = "subir"

    def obter_rect(self):

        return pygame.Rect(
            self.x - 12,
            self.y - 8,
            24,
            28
        )

    def desenhar(self, ecra, barco):

        if self.estado != "parado":

            pygame.draw.line(
                ecra,
                COR_LINHA,
                (barco.rect.centerx, LINHA_Y_INICIO),
                (self.x, self.y),
                3
            )

            pygame.draw.arc(
                ecra,
                COR_ANZOL,
                (self.x - 9, self.y - 5, 20, 25),
                0,
                3.14,
                4
            )
