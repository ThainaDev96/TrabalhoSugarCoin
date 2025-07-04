import pygame
import random
from sys import exit

pygame.init()
pygame.mixer.init()
# === CARREGAR SONS ===

som_alerta = pygame.mixer.Sound('PNG/alerta/alerta.wav')
som_moeda = pygame.mixer.Sound('PNG/coin/coin.wav')
som_gameover = pygame.mixer.Sound('PNG/gameover/gameover.wav')
som_borbulho = pygame.mixer.Sound('PNG/efeitos/borbulho.wav')

som_dano = pygame.mixer.Sound('PNG/sons/dano.wav')
som_cura = pygame.mixer.Sound('PNG/sons/cura.wav')
som_descarregar = pygame.mixer.Sound('PNG/sons/descarregar.wav')

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Boat.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(LARGURA / 2, ALTURA))
        self.peso = 0
        self.alerta_tocado = False
        self.texto_valor = ''
        self.tempo_valor = 0
        self.texto_valor = ''

        self.tempo_valor = pygame.time.get_ticks()

    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 5 - self.peso
        if keys[pygame.K_RIGHT]:
            if self.rect.right <= casa_rect.left:
                if self.peso < 3:
                    self.rect.x += 5 - self.peso
                else:
                    if self.rect.right <= LARGURA:
                        self.rect.x += 5 - self.peso

    class Afundar:
        def __init__(self, sprite, velocidade=1, fade=3):
            self.sprite = sprite
            self.velocidade = velocidade
            self.fade = fade
            self.sprite.alpha = 255
            self.sprite.original_image = self.sprite.image.copy()

        def atualizar(self):
            self.sprite.rect.y += self.velocidade
            self.sprite.alpha -= self.fade
            if self.sprite.alpha < 0:
                self.sprite.alpha = 0
            self.sprite.image = self.sprite.original_image.copy()
            self.sprite.image.set_alpha(self.sprite.alpha)

        def terminou(self):
            return self.sprite.alpha <= 0

    def colisaoMoeda(self):
        global pontuacao_total
        if self.peso < 3:
            moedas_colididas = pygame.sprite.spritecollide(jogador.sprite, moedas_grupo, True)
            for moeda in moedas_colididas:
                pontuacao_total += moeda.valor
                self.peso += 0.5
                som_moeda.play()

                self.texto_valor = f'+{moeda.valor}'
                self.tempo_valor = pygame.time.get_ticks()

    def mostrarValorMoeda(self):
        tempo_atual = pygame.time.get_ticks()
        if self.texto_valor and tempo_atual - self.tempo_valor < 2000:
            texto = fonte.render(self.texto_valor, True, 'red')
            texto_rect = texto.get_rect(center=(self.rect.right, self.rect.top - 60))
            tela.blit(texto, texto_rect)
        elif tempo_atual - self.tempo_valor >= 2000:
            self.texto_valor = ''

    def colisaoPorto(self):
        global tempo_restante
        if self.rect.colliderect(casa_rect):
            if self.peso > 0:  # Se o barco tem peso (moedas)
                som_descarregar.play()
            self.peso = 0
            tempo_restante = None
            global piscar_vermelho
            piscar_vermelho = False
            self.alerta_tocado = False

    def update(self):
        self.playerInput()
        self.colisaoMoeda()
        self.colisaoPorto()
        self.mostrarValorMoeda()


class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 10
        moeda_maior_1 = pygame.image.load('png/gold/gold_21.png').convert_alpha()
        moeda_maior_2 = pygame.image.load('png/gold/gold_22.png').convert_alpha()
        moeda_maior_3 = pygame.image.load('png/gold/gold_23.png').convert_alpha()
        moeda_maior_4 = pygame.image.load('png/gold/gold_24.png').convert_alpha()
        moeda_maior_5 = pygame.image.load('png/gold/gold_25.png').convert_alpha()
        moeda_maior_6 = pygame.image.load('png/gold/gold_26.png').convert_alpha()
        moeda_maior_7 = pygame.image.load('png/gold/gold_27.png').convert_alpha()
        moeda_maior_8 = pygame.image.load('png/gold/gold_28.png').convert_alpha()
        moeda_maior_9 = pygame.image.load('png/gold/gold_29.png').convert_alpha()
        moeda_maior_10 = pygame.image.load('png/gold/gold_30.png').convert_alpha()
        self.frames = [moeda_maior_1, moeda_maior_2, moeda_maior_3, moeda_maior_4, moeda_maior_5, moeda_maior_6,
                       moeda_maior_7, moeda_maior_8, moeda_maior_9, moeda_maior_10]

        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (18, 18))

        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))

    def queda(self):
        self.rect.y += 2

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def animacao(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.queda()
        self.animacao()
        self.destruirMoeda()


class MoedaPrata(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 5
        moeda_maior_1 = pygame.image.load('png/silver/silver_20.png').convert_alpha()
        moeda_maior_2 = pygame.image.load('png/silver/silver_19.png').convert_alpha()
        moeda_maior_3 = pygame.image.load('png/silver/silver_18.png').convert_alpha()
        moeda_maior_4 = pygame.image.load('png/silver/silver_17.png').convert_alpha()
        moeda_maior_5 = pygame.image.load('png/silver/silver_16.png').convert_alpha()
        moeda_maior_6 = pygame.image.load('png/silver/silver_15.png').convert_alpha()
        moeda_maior_7 = pygame.image.load('png/silver/silver_14.png').convert_alpha()
        moeda_maior_8 = pygame.image.load('png/silver/silver_13.png').convert_alpha()
        moeda_maior_9 = pygame.image.load('png/silver/silver_12.png').convert_alpha()
        self.frames = [moeda_maior_1, moeda_maior_2, moeda_maior_3, moeda_maior_4, moeda_maior_5, moeda_maior_6,
                       moeda_maior_7]
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (18, 18))

            self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))

    def queda(self):
        self.rect.y += 3

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def animacao(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.queda()
        self.animacao()
        self.destruirMoeda()


class MoedaBronze(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 1
        moeda_maior_1 = pygame.image.load('png/bronze/bronze_10.png').convert_alpha()
        moeda_maior_2 = pygame.image.load('png/bronze/bronze_9.png').convert_alpha()
        moeda_maior_3 = pygame.image.load('png/bronze/bronze_8.png').convert_alpha()
        moeda_maior_4 = pygame.image.load('png/bronze/bronze_7.png').convert_alpha()
        moeda_maior_5 = pygame.image.load('png/bronze/bronze_6.png').convert_alpha()
        moeda_maior_6 = pygame.image.load('png/bronze/bronze_5.png').convert_alpha()
        moeda_maior_7 = pygame.image.load('png/bronze/bronze_4.png').convert_alpha()
        self.frames = [moeda_maior_1, moeda_maior_2, moeda_maior_3, moeda_maior_4, moeda_maior_5, moeda_maior_6,
                       moeda_maior_7]
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (18, 18))

            self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))

    def queda(self):
        self.rect.y += 5

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def animacao(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.queda()
        self.animacao()
        self.destruirMoeda()

class CupcakeEnvenenado(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('png/cupcake/cupcake.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))
        self.velocidade = 4

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y >= ALTURA + 50:
            self.kill()

        if self.rect.colliderect(jogador.sprite.rect):
            global vidas, game_over
            self.kill()
            som_dano.play()
            if vidas > 0:
                vidas -= 1
            else:
                vidas = -1  # força apagar a última maçã
                game_over = True


class Fase:
    def __init__(self):
        self.fase_atual = 1
        self.inicio_fase = pygame.time.get_ticks()
        self.tempo_fase = 30  # segundos para mudar de fase

    def atualizar(self):
        tempo_agora = pygame.time.get_ticks()
        tempo_decorrido = (tempo_agora - self.inicio_fase) // 1000

        if tempo_decorrido >= self.tempo_fase:
            self.fase_atual += 1
            self.inicio_fase = pygame.time.get_ticks()

    def exibir_info(self):
        texto = fonte.render(f'Fase: {self.fase_atual}', True, PRETO)
        dificuldade = "Fácil" if self.fase_atual == 1 else "Média" if self.fase_atual == 2 else "Difícil"
        dificuldade_texto = fonte.render(f'Dificuldade: {dificuldade}', True, PRETO)
        tela.blit(texto, (10, 70))
        tela.blit(dificuldade_texto, (10, 130))

class CupcakeBom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('png/cupcake_bom.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))
        self.velocidade = 3

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y >= ALTURA + 50:
            self.kill()

        if self.rect.colliderect(jogador.sprite.rect):
            global vidas
            if vidas < 2:
                vidas += 1
                som_cura.play()
            self.kill()


class Boneca(pygame.sprite.Sprite):
    def __init__(self, jogador):
        super().__init__()
        imagem_original = pygame.image.load("png/boneca/boneca.png").convert_alpha()
        largura_barco, altura_barco = jogador.image.get_size()

        escala_largura = int(largura_barco * 0.7)
        escala_altura = int(imagem_original.get_height() * (escala_largura / imagem_original.get_width()))

        self.image = pygame.transform.scale(imagem_original, (escala_largura, escala_altura))
        self.rect = self.image.get_rect()

        cintura_y = jogador.rect.top + int(altura_barco * 0.6)
        self.rect.midbottom = (jogador.rect.centerx, cintura_y)
        self.jogador = jogador

    def update(self):
        largura_barco, altura_barco = self.jogador.image.get_size()
        cintura_y = self.jogador.rect.top + int(altura_barco * 0.6)
        self.rect.midbottom = (self.jogador.rect.centerx, cintura_y)

    def afundar(self):
        self.rect.y += 0.01
class Remo(pygame.sprite.Sprite):
    def __init__(self, boneca):
        super().__init__()
        self.boneca = boneca
        self.original_image = pygame.image.load('png/remo/remo.png').convert_alpha()
        escala = 0.2
        largura = int(self.original_image.get_width() * escala)
        altura = int(self.original_image.get_height() * escala)
        self.original_image = pygame.transform.scale(self.original_image, (largura, altura))
        self.image = self.original_image
        self.rect = self.image.get_rect()

        # Angulo inicial e controle de direção (1 para aumentar, -1 para diminuir)
        self.angle = -30
        self.direction = 1
        self.rotation_speed = 1  # graus por frame

        # Offset do remo em relação ao centro da boneca (ajuste conforme a imagem)
        self.offset_x = 10
        self.offset_y = 15

    def update(self):
        # Atualiza o ângulo para rotacionar o remo
        self.angle += self.direction * self.rotation_speed
        if self.angle > 30:
            self.direction = -1
        elif self.angle < -30:
            self.direction = 1

        # Rotaciona a imagem do remo em torno do centro
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()

        # Posiciona o remo na mão da boneca (usando o centro da boneca + offset)
        boneca_pos = self.boneca.rect.center
        self.rect.center = (boneca_pos[0] + self.offset_x, boneca_pos[1] + self.offset_y)

    def tela_continuar():
        tempo_total = 10  # segundos para decidir
        tempo_inicial = pygame.time.get_ticks()

        fonte_maior = pygame.font.SysFont(None, 48)

        while True:
            tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) // 1000
            tempo_restante = max(0, tempo_total - tempo_decorrido)

            tela.fill((0, 0, 0))
            pergunta = fonte_maior.render("Deseja continuar?", True, (255, 255, 255))
            contagem = fonte_maior.render(f"{tempo_restante}", True, (255, 0, 0))
            instrucoes = fonte.render("Pressione S para SIM ou N para NÃO", True, (255, 255, 255))

            tela.blit(pergunta, pergunta.get_rect(center=(LARGURA / 2, ALTURA / 2 - 50)))
            tela.blit(contagem, contagem.get_rect(center=(LARGURA / 2, ALTURA / 2)))
            tela.blit(instrucoes, instrucoes.get_rect(center=(LARGURA / 2, ALTURA / 2 + 50)))

            pygame.display.update()

            if tempo_restante == 0:
                return False  # Não continuar

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        return True
                    elif event.key == pygame.K_n:
                        return False

    import pygame


import sys

class Button:
    def __init__(self, texto, pos, fonte, cor_normal, cor_hover):
        self.texto = texto
        self.pos = pos
        self.fonte = fonte
        self.cor_normal = cor_normal
        self.cor_hover = cor_hover
        self.pressionado = False
        self.render_text((0, 0, 0))  # cor do texto preto

    def render_text(self, cor_texto):
        self.text_surface = self.fonte.render(self.texto, True, cor_texto)
        self.rect = self.text_surface.get_rect(center=self.pos)
        self.total_width = self.rect.width + 60  # espaço para “ícone”
        self.total_height = self.rect.height + 20

    def draw(self, tela):
        mouse_pos = pygame.mouse.get_pos()
        clicando = pygame.mouse.get_pressed()[0]
        em_cima = self.rect.collidepoint(mouse_pos)
        cor_fundo = self.cor_hover if em_cima else self.cor_normal
        offset_y = 2 if em_cima and clicando else 0

        # Área do botão
        fundo_rect = pygame.Rect(
            self.rect.centerx - self.total_width // 2,
            self.rect.centery - self.total_height // 2 + offset_y,
            self.total_width,
            self.total_height
        )

        # Sombra
        sombra_rect = fundo_rect.copy()
        sombra_rect.y += 4
        pygame.draw.rect(tela, (50, 50, 50), sombra_rect, border_radius=12)

        # Botão
        pygame.draw.rect(tela, cor_fundo, fundo_rect, border_radius=12)
        pygame.draw.rect(tela, (255, 255, 255), fundo_rect, 2, border_radius=12)

        # “Ícone” desenhado (círculo azul decorativo)
        pygame.draw.circle(tela, (0, 120, 255), (fundo_rect.left + 25, fundo_rect.centery), 10)

        # Texto
        self.render_text((0, 0, 0))
        tela.blit(self.text_surface, (fundo_rect.left + 45, fundo_rect.centery - self.rect.height // 2 + offset_y))

    def clicado(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                return True
        return False


class Menu:
    def __init__(self, tela, fonte):
        self.tela = tela
        self.fonte = fonte
        self.rodando = True

        cinza_normal = (160, 160, 160)
        cinza_hover = (200, 200, 200)

        self.fonte_titulo = pygame.font.SysFont(None, 72)
        self.botao_comecar = Button("Começar", (LARGURA // 2, ALTURA // 2), fonte, cinza_normal, cinza_hover)
        self.botao_sair = Button("Sair", (LARGURA // 2, ALTURA // 2 + 60), fonte, cinza_normal, cinza_hover)
        self.botao_instrucoes = Button("Instruções", (LARGURA // 2, ALTURA // 2 + 120), fonte, cinza_normal,
                                       cinza_hover)

        self.logo = pygame.image.load("2.jpg").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (LARGURA, ALTURA))

    def exibir(self):
        while self.rodando:
            self.tela.fill((0, 0, 0))

            # Desenhar logo
            logo_rect = self.logo.get_rect(topleft=(0, 0))
            self.tela.blit(self.logo, logo_rect)

            titulo_texto = self.fonte_titulo.render("Sugar Coin", True, (0, 0, 139))
            titulo_rect = titulo_texto.get_rect(center=(LARGURA // 2, 100))  # Centralizado no topo
            self.tela.blit(titulo_texto, titulo_rect)

            # Desenhar botões
            self.botao_comecar.draw(self.tela)
            self.botao_sair.draw(self.tela)
            self.botao_instrucoes.draw(self.tela)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.botao_comecar.clicado(event):
                    self.rodando = False  # Sai do menu e começa o jogo

                if self.botao_sair.clicado(event):
                    pygame.quit()
                    sys.exit()

                if self.botao_instrucoes.clicado(event):
                    tela_instrucoes()
def tela_instrucoes(cupcake_bom=None):
    fonte_titulo = pygame.font.SysFont("Comic Sans MS", 40, bold=True)
    fonte_texto = pygame.font.SysFont("Comic Sans MS", 22)
    fonte_rodape = pygame.font.SysFont("Comic Sans MS", 20, italic=True)

    fundo = fundo_instrucoes

    # Lista com texto e imagens correspondentes
    instrucoes = [
        ("Objetivo: controle o barco e colete moedas que caem do céu.", None),
        ("", None),
        ("Moeda de bronze (vale 1 ponto)", img_bronze),
        ("Moeda de prata (vale 5 pontos)", img_prata),
        ("Moeda de ouro (vale 10 pontos)", img_ouro),
        ("", None),
        ("Barco suporta até 6 moedas (peso máximo: 3).", None),
        ("Depois, vá até o porto (direita) para descarregar.", None),
        ("", None),
        ("A partir da fase 2, caem cupcakes envenenados!", img_cupcake),
        ("Se for atingido ou demorar cheio, o barco afunda!", None),
        ("", None),
        ("Cupcakes bons restauram 1 vida (máximo: 3)", img_cupcake_bom ),
        ("", None),
        ("Você começa com 3 vidas (maçãs no topo direito).", img_maca),
        ("Se perder todas, é GAME OVER.", None),
        ("", None),
    ]

    scroll_offset = 0
    scroll_speed = 30
    espaco_linha = 36
    altura_conteudo = len(instrucoes) * espaco_linha + 20
    scroll_max = max(0, altura_conteudo - (ALTURA - 200))  # Espaço entre título e rodapé

    # Barra de rolagem
    barra_largura = 20
    barra_altura = 140  # Mais alto e grosso (altura do "tijolo")
    trilho_x = LARGURA - 30
    trilho_y = 100
    trilho_altura = ALTURA - 180
    segurando_barra = False
    mouse_y_inicio = 0
    scroll_inicio = 0

    rodando = True
    while rodando:
        tela.blit(fundo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                # Seta pra cima
                if event.key == pygame.K_UP:
                    scroll_offset = max(scroll_offset - scroll_speed, 0)
                # Seta pra baixo
                elif event.key == pygame.K_DOWN:
                    scroll_offset = min(scroll_offset + scroll_speed, scroll_max)
                else:
                    rodando = False  # Qualquer outra tecla sai da tela

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll para cima
                    scroll_offset = max(scroll_offset - scroll_speed, 0)
                elif event.button == 5:  # Scroll para baixo
                    scroll_offset = min(scroll_offset + scroll_speed, scroll_max)
                elif event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if trilho_x <= mx <= trilho_x + barra_largura:
                        if scroll_max > 0:
                            barra_y = trilho_y + int((scroll_offset / scroll_max) * (trilho_altura - barra_altura))
                            if barra_y <= my <= barra_y + barra_altura:
                                segurando_barra = True
                                mouse_y_inicio = my
                                scroll_inicio = scroll_offset

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    segurando_barra = False

            elif event.type == pygame.MOUSEMOTION:
                if segurando_barra:
                    my = pygame.mouse.get_pos()[1]
                    delta = my - mouse_y_inicio
                    proporcao = scroll_max / (trilho_altura - barra_altura)
                    scroll_offset = min(max(scroll_inicio + delta * proporcao, 0), scroll_max)

        # Desenhar título fixo no topo
        titulo = fonte_titulo.render("INSTRUÇÕES", True, (0, 70, 140))
        tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 50)))

        # Desenhar instruções roláveis
        base_y = 120 - scroll_offset
        x_texto = 100
        x_imagem = 40

        for i, (texto, imagem) in enumerate(instrucoes):
            y = base_y + i * espaco_linha
            # Só desenha se estiver dentro da área visível (entre título e rodapé)
            if 100 <= y <= ALTURA - 80:
                if imagem:
                    if texto == "Cupcakes bons restauram 1 vida (máximo: 3)":
                        imagem_redimensionada = pygame.transform.scale(imagem, (60, 60))
                        tela.blit(imagem_redimensionada, (x_imagem - 8, y - 10))
                    else:
                        tela.blit(imagem, (x_imagem, y))
                cor = (180, 0, 0) if "cupcake" in (texto or "").lower() else (30, 30, 30)
                render = fonte_texto.render(texto, True, cor)
                tela.blit(render, (x_texto, y))

        # Rodapé fixo
        rodape = fonte_rodape.render("Pressione qualquer tecla para voltar ao menu.", True, (0, 0, 0))
        tela.blit(rodape, rodape.get_rect(center=(LARGURA // 2, ALTURA - 40)))

        # Desenhar trilho e barra de rolagem (tijolo)
        pygame.draw.rect(tela, (200, 200, 200), (trilho_x, trilho_y, barra_largura, trilho_altura))
        if scroll_max > 0:
            barra_y = trilho_y + int((scroll_offset / scroll_max) * (trilho_altura - barra_altura))
        else:
            barra_y = trilho_y
        pygame.draw.rect(tela, (80, 80, 80), (trilho_x, barra_y, barra_largura, barra_altura))

        pygame.display.update()






def janela_continuar():
    tempo_total = 10
    tempo_inicial = pygame.time.get_ticks()

    fonte_grande = pygame.font.SysFont(None, 48)
    botao_sim = Button("SIM", (LARGURA // 2 - 100, ALTURA // 2 + 50), fonte, (160, 160, 160), (200, 200, 200))
    botao_nao = Button("NÃO", (LARGURA // 2 + 100, ALTURA // 2 + 50), fonte, (160, 160, 160), (200, 200, 200))

    fundo_janela = pygame.image.load("PNG/fim/fundo_janela.png").convert()  # ⬅️ imagem de fundo personalizada
    fundo_janela = pygame.transform.scale(fundo_janela, (LARGURA, ALTURA))

    while True:
        tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) // 1000
        tempo_restante = max(0, tempo_total - tempo_decorrido)

        tela.blit(fundo_janela, (0, 0))  # Aplica o fundo

        pergunta = fonte_grande.render("Deseja continuar?", True, (255, 255, 255))
        tela.blit(pergunta, pergunta.get_rect(center=(LARGURA // 2, ALTURA // 2 - 50)))

        contagem = fonte.render(f"Tempo restante: {tempo_restante}s", True, (255, 0, 0))
        tela.blit(contagem, contagem.get_rect(center=(LARGURA // 2, ALTURA // 2)))

        botao_sim.draw(tela)
        botao_nao.draw(tela)

        pygame.display.update()

        if tempo_restante == 0:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif botao_sim.clicado(event):
                return True
            elif botao_nao.clicado(event):
                return False

tempo_mostrar_texto = 2000
mostrar_texto = False

# === CONFIGURAÇÕES GLOBAIS ===
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Sugar Coin")

vidas = 2  # Começa com 2 vidas extras (total de 3)

img_maca = pygame.image.load('PNG/img_maca.png').convert_alpha()
img_maca = pygame.transform.scale(img_maca, (50, 50))


# === IMAGENS PARA TELA DE INSTRUÇÕES ===
img_bronze = pygame.transform.scale(pygame.image.load('png/bronze/bronze_6.png').convert_alpha(), (30, 30))
img_prata  = pygame.transform.scale(pygame.image.load('png/silver/silver_16.png').convert_alpha(), (30, 30))
img_ouro   = pygame.transform.scale(pygame.image.load('png/gold/gold_25.png').convert_alpha(), (30, 30))
img_cupcake = pygame.transform.scale(pygame.image.load('png/cupcake/cupcake.png').convert_alpha(), (50, 50))
img_cupcake_bom = pygame.image.load('png/cupcake_bom.png').convert_alpha()
img_cupcake_bom = pygame.transform.scale(img_cupcake_bom, (80, 80))


font = pygame.font.Font(None, 15)
AZUL = (137, 207, 240)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
fonte = pygame.font.SysFont(None, 36)

tempo_limite = 5
tempo_restante = None
game_over = False
pontuacao_total = 0
inicio_jogo = pygame.time.get_ticks()
piscar_vermelho = False
contador_piscar = 0
game_over_tocado = False

jogador = pygame.sprite.GroupSingle()
jogador.add(Jogador())

cupcakes_grupo = pygame.sprite.Group()
fase = Fase()

boneca_grupo = pygame.sprite.GroupSingle()
boneca_grupo.add(Boneca(jogador.sprite))

remo_grupo = pygame.sprite.GroupSingle()
remo = Remo(boneca_grupo.sprite)
remo_grupo.add(remo)

moedas_grupo = pygame.sprite.Group()
casa = pygame.image.load('porto.png')
casa_rect = casa.get_rect(bottomright=(LARGURA, ALTURA + 38))
fundo = pygame.image.load('png/fundo2.png').convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

# Fundo para a tela de instruções
fundo_instrucoes = pygame.image.load('2.jpg').convert_alpha()
fundo_instrucoes = pygame.transform.scale(fundo_instrucoes, (LARGURA, ALTURA))

moeda_timer_evento = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer_evento, 2000)

cupcake_timer = pygame.USEREVENT + 2
pygame.time.set_timer(cupcake_timer, 500)


clock = pygame.time.Clock()

menu = Menu(tela, fonte)
menu.exibir()

fase = Fase()  # Garante que o jogo sempre começará na fase 1
inicio_jogo = pygame.time.get_ticks()  # Reinicia o tempo total do jogo

cupcakes_bons_gerados = 0

afundando = False
afundar_iniciado = False
afundar_terminou = False
afundar_timer = 0

# --- LOOP PRINCIPAL ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == moeda_timer_evento:
            MAX_MOEDAS = 5
            if len(moedas_grupo) < MAX_MOEDAS:
                tipos_moeda = ['ouro', 'prata', 'bronze']
                quantidade = random.randint(1, min(3, MAX_MOEDAS - len(moedas_grupo)))
                moedas_selecionadas = random.sample(tipos_moeda, quantidade)
                for moeda in moedas_selecionadas:
                    if moeda == 'ouro':
                        moedas_grupo.add(Moeda())


                    elif moeda == 'prata':
                        moedas_grupo.add(MoedaPrata())
                    else:
                        moedas_grupo.add(MoedaBronze())

        if event.type == cupcake_timer:
            if fase.fase_atual >= 2:
                # === Cupcake Envenenado ===
                chance_envenenado = 0.4 if fase.fase_atual == 2 else min(0.2 * fase.fase_atual, 0.8)
                quantidade = 1 if fase.fase_atual == 2 else random.randint(1, fase.fase_atual)

                if random.random() < chance_envenenado:
                    for _ in range(quantidade):
                        cupcakes_grupo.add(CupcakeEnvenenado())

                # === Cupcake Bom (só 1 por vez na tela)
                if not any(isinstance(c, CupcakeBom) for c in cupcakes_grupo):
                    chance_bom = 0.2 if fase.fase_atual == 2 else 0.1
                    if random.random() < chance_bom:
                        cupcakes_grupo.add(CupcakeBom())

    fase.atualizar()

    # Gerar cupcakes envenenados nas fases 2 e 3

    if jogador.sprite.peso >= 3:
        piscar_vermelho = True
        if not jogador.sprite.alerta_tocado:
            som_alerta.play()
            jogador.sprite.alerta_tocado = True
        contador_piscar += 1
        if contador_piscar % 20 < 10:
            tela.fill(VERMELHO)
        else:
            tela.blit(fundo, (0, 0))
    else:
        piscar_vermelho = False
        contador_piscar = 0
        tela.blit(fundo, (0, 0))

    moedas_grupo.draw(tela)
    moedas_grupo.update()

    jogador.draw(tela)
    jogador.update()

    boneca_grupo.draw(tela)
    boneca_grupo.update()

    remo_grupo.update()
    remo_grupo.draw(tela)

    cupcakes_grupo.update()
    cupcakes_grupo.draw(tela)

    if jogador.sprite.peso >= 3:
        mensagem = fonte.render('Barco cheio', False, PRETO)
        mensagem_rect = mensagem.get_rect(midbottom=(jogador.sprite.rect.x, 550))
        tela.blit(mensagem, mensagem_rect)

    tela.blit(casa, casa_rect)

    if jogador.sprite.peso >= 3:
        if tempo_restante is None:
            tempo_restante = pygame.time.get_ticks()
        tempo_atual = pygame.time.get_ticks()
        segundos_passados = (tempo_atual - tempo_restante) / 1000
        if segundos_passados >= tempo_limite:
            game_over = True

        tempo_texto = fonte.render(f'Tempo: {max(0, int(tempo_limite - segundos_passados))}', True, PRETO)
        tela.blit(tempo_texto, (10, 100))

    tempo_total_segundos = (pygame.time.get_ticks() - inicio_jogo) // 1000
    tempo_total_texto = fonte.render(f'Tempo total: {tempo_total_segundos}s', True, PRETO)
    pontuacao_texto = fonte.render(f'Score: {pontuacao_total}', True, PRETO)
    tela.blit(tempo_total_texto, (10, 10))
    tela.blit(pontuacao_texto, (10, 40))

    # Exibir vidas (maçãs)
    for i in range(3):  # máximo de 3 vidas
        maca = img_maca.copy()
        if i > vidas:
            maca.set_alpha(60)  # vida perdida, maçã apagada
        tela.blit(maca, (LARGURA - 40 - i * 35, 10))

    fase.exibir_info()
    if game_over:
        if not afundar_iniciado:
            som_borbulho.play(-1)  # Toca o borbulho primeiro
            afundando = True
            afundar_iniciado = True

        if afundando and not afundar_terminou:
            jogador.sprite.rect.y += 0.5
            boneca_grupo.sprite.rect.y += 0.5
            remo_grupo.sprite.rect.y += 0.5

            if jogador.sprite.rect.top > ALTURA and boneca_grupo.sprite.rect.top > ALTURA and remo_grupo.sprite.rect.top > ALTURA:
                afundando = False
                afundar_terminou = True
                afundar_timer = pygame.time.get_ticks()
    if afundar_terminou:
        if pygame.time.get_ticks() - afundar_timer > 2000:
            som_borbulho.stop()
            som_gameover.play()  # Só agora toca o som de game over

            tela_preta = pygame.Surface((LARGURA, ALTURA))
            tela_preta.set_alpha(200)
            tela_preta.fill((0, 0, 0))
            tela.blit(tela_preta, (0, 0))

            mensagem_gameover = fonte.render('GAME OVER', True, VERMELHO)
            mensagem_gameover_rect = mensagem_gameover.get_rect(center=(LARGURA / 2, ALTURA / 2))
            tela.blit(mensagem_gameover, mensagem_gameover_rect)

            pygame.display.update()
            pygame.time.delay(3000)
            deseja_continuar = janela_continuar()

            if deseja_continuar:
                if deseja_continuar:
                    # Reinicializa tudo como no início
                    game_over = False

                    vidas = 2  # 2 vidas extras, total de 3 chances
                    img_maca = pygame.image.load('PNG/img_maca.png').convert_alpha()
                    img_maca = pygame.transform.scale(img_maca, (50, 50))

                    afundar_terminou = False
                    afundar_iniciado = False
                    piscar_vermelho = False
                    contador_piscar = 0
                    pontuacao_total = 0

                    tempo_restante = None
                    inicio_jogo = pygame.time.get_ticks()

                    # Resetar fase
                    fase = Fase()

                    # Esvaziar grupos
                    moedas_grupo.empty()
                    cupcakes_grupo.empty()
                    jogador.empty()
                    boneca_grupo.empty()
                    remo_grupo.empty()

                    jogador.add(Jogador())
                    boneca_grupo.add(Boneca(jogador.sprite))
                    remo = Remo(boneca_grupo.sprite)
                    remo_grupo.add(remo)



            else:
                pygame.quit()
                exit()

    pygame.display.update()
    clock.tick(60)