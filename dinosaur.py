import pygame
import sys
import random
import os

pygame.init()

cielo = (10, 10, 10)
red = (220, 60, 60)
white = (255, 255, 255)

x = 800
y = 500
window = pygame.display.set_mode((x, y))
pygame.display.set_caption("dino run")
fuente = pygame.font.SysFont("arial", 24)
fps = pygame.time.Clock()

sy = 300          # suelo
fs = -15          # fuerza de salto
g = 0.8           # gravedad
vo_inicial = 5    # velocidad inicial
vo_max = 15       # velocidad máxima
vo_paso = 0.5     # cuánto sube por obstáculo esquivado

dino_img = pygame.image.load(os.path.join("img", "dino.png")).convert_alpha()
dinodunk_img = pygame.image.load(os.path.join("img", "dino dunk.png")).convert_alpha()
cactus_img = pygame.image.load(os.path.join("img", "cactus.png")).convert_alpha()
roca_img = pygame.image.load(os.path.join("img", "roca.png")).convert_alpha()
flappy_img = pygame.image.load(os.path.join("img", "flappy.png")).convert_alpha()

dino_img = pygame.transform.scale(dino_img, (60, 60))
dinodunk_img = pygame.transform.scale(dinodunk_img, (40, 30))
roca_img = pygame.transform.scale(roca_img, (50, 50))
flappy_img = pygame.transform.scale(flappy_img, (20, 20))
cactus_img = pygame.transform.scale(cactus_img, (20, 60))


def reiniciar():
    global dino_rect, dino_actual, vy, vo, tem, teo, score
    global obstaculos, jugando, inicio, tiempo
    dino_actual = dino_img
    dino_rect = dino_img.get_rect(bottomleft=(50, sy))
    vy = 0
    vo = vo_inicial
    tem = 0
    teo = random.randint(45, 90)
    score = 0
    obstaculos = []   # cada elemento: [imagen, rect, posicion_x]
    jugando = True
    inicio = pygame.time.get_ticks()
    tiempo = 0


def crear_obstaculo():
    tipo = random.choice(["cactus", "roca", "pajaro"])
    if tipo == "cactus":
        img = cactus_img
        rect = img.get_rect(bottomleft=(x, sy))
    elif tipo == "roca":
        img = roca_img
        rect = img.get_rect(bottomleft=(x, sy))
    else:
        img = flappy_img
        altura = random.choice([15, 35, 120])   # distancia sobre el suelo
        rect = img.get_rect(bottomleft=(x, sy - altura))
    obstaculos.append([img, rect, float(rect.x)])


reiniciar()

while True:
    fps.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if jugando:
        tiempo = (pygame.time.get_ticks() - inicio) // 1000

        agachado = keys[pygame.K_DOWN] or keys[pygame.K_s]
        en_suelo = dino_rect.bottom >= sy

        # salto
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and en_suelo and not agachado:
            vy = fs
        if agachado and not en_suelo:
            vy += 2   # caída rápida en el aire
        vy += g
        dino_rect.y += vy
        if dino_rect.bottom > sy:
            dino_rect.bottom = sy
            vy = 0

        # imagen y hitbox según si está agachado
        dino_actual = dinodunk_img if agachado else dino_img
        dino_rect = dino_actual.get_rect(bottomleft=dino_rect.bottomleft)

        # crear obstáculos con separación aleatoria
        tem += 1
        if tem >= teo:
            tem = 0
            teo = random.randint(45, 90)
            crear_obstaculo()

        # mover obstáculos
        for obs in obstaculos[:]:
            obs[2] -= vo
            obs[1].x = int(obs[2])
            if obs[1].colliderect(dino_rect):
                jugando = False
            elif obs[1].right < 0:
                obstaculos.remove(obs)
                score += 1
                vo = min(vo + vo_paso, vo_max)
    else:
        if keys[pygame.K_r]:
            reiniciar()

    # dibujar
    window.fill(cielo)
    pygame.draw.line(window, white, (0, sy), (x, sy), 2)
    window.blit(dino_actual, dino_rect)
    for obs in obstaculos:
        window.blit(obs[0], obs[1])

    window.blit(fuente.render(f"Puntaje: {score}", True, white), (10, 10))
    window.blit(fuente.render(f"Tiempo: {tiempo}s", True, white), (10, 40))

    if not jugando:
        txt1 = fuente.render("game over", True, red)
        txt2 = fuente.render(f"Puntaje final: {score}  |  Tiempo: {tiempo} segundos", True, white)
        txt3 = fuente.render("Presiona R para reiniciar", True, white)
        window.blit(txt1, txt1.get_rect(center=(x // 2, y // 2 - 40)))
        window.blit(txt2, txt2.get_rect(center=(x // 2, y // 2)))
        window.blit(txt3, txt3.get_rect(center=(x // 2, y // 2 + 40)))

    pygame.display.flip()
