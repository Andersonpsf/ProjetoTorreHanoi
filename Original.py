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
def printDiscos(hastes, tela, pecas_surf, pecas_rect):
    for haste, (x, _) in zip(hastes, [(300, 760), (700, 760), (1100, 760)]):
        for rect in haste:
            tela.blit(pecas_surf[pecas_rect.index(rect)], rect)

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

    mouse_pos = pygame.mouse.get_pos()

    printDiscos([haste1, haste2, haste3], tela, pecas_surf, pecas_rect)

    import pygame
    from pygame.locals import *
    from sys import exit
    from typing import List

    pygame.init()
    tela = pygame.display.set_mode((1400, 790))
    pygame.display.set_caption("Torre Hanoi")
    clock = pygame.time.Clock()
    # listas para cada haste (madeira)
    # O objetivo das listas é que quando um rectangle sair de uma haste para outra ele também saia de uma lista para a correspondente da haste. (Explicação parte1)

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
    lista = []
    haste1 = []
    haste2 = []
    haste3 = []

    # rect de rectangle que serve para saber os pontos de colisão e posicionar melhor as peças
    pecas_rect = [surf.get_rect(midbottom=(300, 607 + i * 17)) for i, surf in enumerate(pecas_surf)]


    for pecas in pecas_rect:
        haste1.append(pecas)
        lista.append(pecas)

    # superificie_torreHanoi1 = pygame.image.load(r"E:\TorreHanoiPCIF\TorreHanoi_Cenario1_page-0001.jpg").convert()

    posicao_y_torreHanoi = 20
    superficie_teste = pygame.Surface((1400, 800))
    superficie_teste.fill("Azure")

    operacao_valida = False
    # esse clicks foi feito para evitar que mais de um rect esteja na posição y (ele vai ir para essa posição ao ser clicado)
    clicks = c = 0
    while True:
        # tela.blit serve para posicionar as imagens na tela
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
                                print(lista.index(haste1[-1]))

                                if haste3==[] or lista.index(haste1[-1]) < lista.index(haste3[-1]) :
                                    print("Adicionada a haste 3")
                                    haste3.insert(-1,haste1.pop())
                                    print(lista)
                                    print(haste1)
                                    print(haste3)

                                elif lista.index(haste3[-1]) < lista.index(haste1[-1]):
                                    haste1.insert(-1,haste3.pop())
                                    print(lista)
                                    print(haste1)
                                    print(haste3)
                                      # Sair do loop após o movimento bem-sucedido
                                    
                                rect.midbottom = (madeira.midbottom[0], 760)
                                clicks = 0  # Defina clicks como 0 aqui, após o movimento bem-sucedido do retângulo
                                c += 1
                                while any(rect.colliderect(other_rect) for other_rect in pecas_rect if
                                          other_rect != rect):
                                    rect.y -= 1

                                else:
                                    print("Operação inválida")
                                    break




                            elif rect.collidepoint(mouse_pos) and clicks == 0:
                                rect.y = 20
                                clicks += 1
                                print(rect.right)
                                print(rect.midbottom)
                                print(f"Peça movida")

                                break

            elif event.type == pygame.KEYDOWN:
                if event.key == K_v:
                    print("Deu certo")

        pygame.display.update()
        clock.tick(60)

    pygame.display.update()
    clock.tick(60)
