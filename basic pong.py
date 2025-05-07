import pygame
import sys

# Inicializa o pygame
pygame.init()

# Tamanho da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong Básico")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# raquetes
largura_paleta = 10
altura_paleta = 100
paleta_esquerda = pygame.Rect(50, altura//2 - altura_paleta//2, largura_paleta, altura_paleta)
paleta_direita = pygame.Rect(largura - 60, altura//2 - altura_paleta//2, largura_paleta, altura_paleta)
velocidade_paleta = 5

# Bola
bola = pygame.Rect(largura//2 - 15, altura//2 - 15, 30, 30)
vel_bola_x = 5
vel_bola_y = 5

# Loop do jogo
clock = pygame.time.Clock()
while True:
    clock.tick(60)  # 60 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento das paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta_esquerda.top > 0:
        paleta_esquerda.y -= velocidade_paleta
    if teclas[pygame.K_s] and paleta_esquerda.bottom < altura:
        paleta_esquerda.y += velocidade_paleta
    if teclas[pygame.K_UP] and paleta_direita.top > 0:
        paleta_direita.y -= velocidade_paleta
    if teclas[pygame.K_DOWN] and paleta_direita.bottom < altura:
        paleta_direita.y += velocidade_paleta

    # Movimento da bola
    bola.x += vel_bola_x
    bola.y += vel_bola_y

    # Colisão com topo e base
    if bola.top <= 0 or bola.bottom >= altura:
        vel_bola_y *= -1

    # Colisão com paletas
    if bola.colliderect(paleta_esquerda) or bola.colliderect(paleta_direita):
        vel_bola_x *= -1

    # Reinicia a bola se ela sair da tela
    if bola.left <= 0 or bola.right >= largura:
        bola.center = (largura//2, altura//2)
        vel_bola_x *= -1

    # Desenho na tela
    tela.fill(preto)
    pygame.draw.rect(tela, branco, paleta_esquerda)
    pygame.draw.rect(tela, branco, paleta_direita)
    pygame.draw.ellipse(tela, branco, bola)
    pygame.draw.aaline(tela, branco, (largura//2, 0), (largura//2, altura))  # linha do meio

    pygame.display.flip()
