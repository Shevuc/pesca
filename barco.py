
import pygame
from settings import *


class Barco:

    def __init__(self):
        # Carregar imagem do barco
        self.imagem = pygame.image.load(FICHEIRO_BARCO).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, BARCO_TAMANHO)

        # Criar posição do barco
        self.rect = self.imagem.get_rect()
        self.rect.x = BARCO_X_INICIAL
        self.rect.y = BARCO_Y

    def update(self, teclas):
        # Movimentar para a esquerda
        if teclas[pygame.K_LEFT]:
            self.rect.x -= VELOCIDADE_BARCO

        # Movimentar para a direita
        if teclas[pygame.K_RIGHT]:
            self.rect.x += VELOCIDADE_BARCO

        # Impedir que saia do ecrã
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > LARGURA:
            self.rect.right = LARGURA

    def desenhar(self, ecra):
        ecra.blit(self.imagem, self.rect)
