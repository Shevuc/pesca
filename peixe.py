
import pygame
from settings import *


class Peixe:

    def __init__(self, y, velocidade):

        # Carregar imagem do peixe
        self.imagem = pygame.image.load(FICHEIRO_PEIXE).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, PEIXE_TAMANHO)

        # Criar posição do peixe
        self.rect = self.imagem.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = y

        self.velocidade = velocidade
        self.tipo = "peixe"

    def update(self):
        # Movimentar peixe para a direita
        self.rect.x += self.velocidade

    def desenhar(self, ecra):
        ecra.blit(self.imagem, self.rect)
