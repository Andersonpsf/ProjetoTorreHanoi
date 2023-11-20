import pygame
from pygame.locals import *
from sys import exit
from typing import List


pygame.init()
tela = pygame.display.set_mode((1400, 790))
pygame.display.set_caption("Torre Hanoi")
clock = pygame.time.Clock()
#listas para cada haste (madeira)
#O objetivo das listas é que quando um rectangle sair de uma haste para outra ele também saia de uma lista para a correspondente da haste. (Explicação parte1)
pilha_haste1: List[pygame.Rect] = []
pilha_haste2: List[pygame.Rect] = []
pilha_haste3: List[pygame.Rect] = []
superficie_base = pygame.image.load(r"../../images/base.jpg").convert()
superficie_base = pygame.transform.scale(superficie_base, (1380, 30))

madeira_surf = pygame.image.load(r"../../images/madeira.jpg").convert()
madeira_rect = madeira_surf.get_rect(midbottom=(300, 760))
madeira_rect2 = madeira_surf.get_rect(midbottom=(700, 760))
madeira_rect3 = madeira_surf.get_rect(midbottom=(1100, 760))
madeiras = [madeira_rect, madeira_rect2, madeira_rect3]


pecas_surf = [
    pygame.image.load(r"../../images/retanguloAzul.jpg").convert(),
    pygame.image.load(r"../../images/retanguloAzulCiano.jpg").convert(),
    pygame.image.load(r"../../images/retanguloAmarelo.jpg").convert(),
    pygame.image.load(r"../../images/retanguloVermelho.jpg").convert(),
    pygame.image.load(r"../../images/retanguloVerde.jpg").convert(),
    pygame.image.load(r"../../images/retanguloRosa.jpg").convert(),
    pygame.image.load(r"../../images/retanguloRoxo.jpg").convert(),
    pygame.image.load(r"../../images/retanguloCinza.jpg").convert(),
    pygame.image.load(r"../../images/retanguloLaranja.jpg").convert(),
    pygame.image.load(r"../../images/retanguloBege.jpg").convert(),
]

haste1 = []
haste2 = []
haste3 = []

#rect de rectangle que serve para saber os pontos de colisão e posicionar melhor as peças
pecas_rect = [surf.get_rect(midbottom=(300, 607 + i * 17)) for i, surf in enumerate(pecas_surf)]

for pecas in pecas_rect:
    pilha_haste1.append(pecas)
    haste1.append(pecas)

# superificie_torreHanoi1 = pygame.image.load(r"E:\TorreHanoiPCIF\TorreHanoi_Cenario1_page-0001.jpg").convert()

posicao_y_torreHanoi = 20
superficie_teste = pygame.Surface((1400, 800))
superficie_teste.fill("Azure")

#esse clicks foi feito para evitar que mais de um rect esteja na posição y (ele vai ir para essa posição ao ser clicado)
clicks = c = 0
while True:
    #tela.blit serve para posicionar as imagens na tela
    tela.blit(superficie_teste, (0, 5))
    tela.blit(superficie_base, (10, 760))
    tela.blit(madeira_surf, madeira_rect)
    tela.blit(madeira_surf, madeira_rect2)
    tela.blit(madeira_surf, madeira_rect3)
    for i, (surf, rect) in enumerate(zip(pecas_surf, pecas_rect)):
        tela.blit(surf, rect)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            for madeira in madeiras:
                if madeira.collidepoint(mouse_pos):
                    for rect in pecas_rect:
                        if clicks == 1 and rect.y == 20:
                            print("Peça em movimento e mouse em cima da madeira")
                            rect.midbottom = (madeira.midbottom[0], 760 )

                            if rect.midbottom[0]==300:
                                #código para não dar erro caso a lista esteja vazia pois não vai ter nenhum rect para ele comparar
                                if not haste1:
                                    haste1.append(rect)
                                    print("rect adicionado em lista vazia")
                                    break
                                    #(Explicação parte2) Isso é para que toda vez que for mover um rect para uma outra haste ele compare com a última haste da lista, impossibilitando assim que tenha uma haste maior por cima de uma menor
                                    if rect.width > haste1[-1]:
                                        print("não da")
                                        break
                                    else:
                                        haste1.append(rect)
                                        print("rect adicionado")

                            elif rect.midbottom[0]==700:
                                if not haste2:
                                    haste2.append(rect)
                                    print("rect adicionado em lista vazia")
                                    break
                                    if rect.width > haste2[-1]:
                                        print("não da")
                                        break
                                    else:
                                        haste2.append(rect)
                                        print("rect adicionado")

                            elif rect.midbottom[0]==1100:
                                if not haste3:
                                    haste3.append(rect)
                                    print("rect adicionado em lista vazia")
                                    break
                                if rect.width > haste3[-1]:
                                    print("não da")
                                    break
                                else:
                                    haste3.append(rect)
                                    print("rect adicionado")
                            while any(rect.colliderect(other_rect) for other_rect in pecas_rect if other_rect != rect):
                                rect.y = rect.y - 5
                            clicks = 0
                            c += 1
                            eixoY = midbottom = (300, 750 - i * 18)
                            break


                        elif rect.collidepoint(mouse_pos) and clicks == 0:
                            rect.y = 20
                            clicks += 1
                            print(rect.right)
                            print(rect.midbottom)
                            print(f"Peça movida")
                            if rect.midbottom[0]==300:
                                index = haste1.index(rect)
                                haste1.pop(index)
                                print("Retangulo removido")
                            elif rect.midbottom[0]==700:
                                index = haste2.index(rect)
                                haste2.pop(index)
                                print("Retangulo removido")
                            elif rect.midbottom[0]==1100:
                                index = haste3.index(rect)
                                haste3.pop(index)
                                print("Retangulo removido")
                            break

        elif event.type == pygame.KEYDOWN:
            if event.key == K_v:
                print("Deu certo")

    pygame.display.update()
    clock.tick(60)
