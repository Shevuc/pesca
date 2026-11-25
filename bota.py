
import pygame
from settings import *


class Bota:

    def __init__(self, y, velocidade):

        self.imagem = pygame.image.load(FICHEIRO_BOTA).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, BOTA_TAMANHO)

        self.rect = self.imagem.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = y

        self.velocidade = velocidade
        self.tipo = "bota"

    def update(self):
        self.rect.x += self.velocidade

    def desenhar(self, ecra):
        ecra.blit(self.imagem, self.rect)
