from Classes import *
import sys

pygame.init()

WINWIDTH, WINHEIGHT = 700, 700
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Test')

FPSCLOCK = pygame.time.Clock()
FPS = 60

Entities = pygame.sprite.Group()
player = Player(0, WINHEIGHT - 200, Entities)
Entities.add(player)


def camera(obj):
    global Entities

    for entity in Entities:
        if obj.rect.x >= 700/2:
            obj.rect.x = 700/2
        if entity == obj:
            continue
        if obj.pos[0] >= 350 and obj.x_vel < 0:
            obj.rect.x = 350

        entity.pos[0] = entity.pos[0] - obj.x_vel
        # entity.pos[1] = entity.pos[1] + obj.pos[1]
        entity.rect.left = entity.pos[0]
        # entity.rect.top = entity.pos[1]


def init_surface():
    x = 0
    while x <= 1400:
        f = FloorTile(x, WINHEIGHT - 70)
        Entities.add(f)
        DISPLAYSURF.blit(f.image, f.rect)
        x += 70
    box = Box(350, WINHEIGHT - 140)
    Entities.add(box)
    DISPLAYSURF.blit(box.image, box.rect)

    DISPLAYSURF.blit(player.image, player.rect)


def draw():
    bg = pygame.Surface((70, 70))
    for x in range(0, 1400, 70):
        for y in range(0, 1400, 70):
            DISPLAYSURF.blit(bg, (x, y))

    player.update()
    player.apply_gravity()
    camera(player)


    for E in Entities:
        DISPLAYSURF.blit(E.image, E.rect)


def keydown(event):
    global player

    if event.key == K_d:
        player.move_right()
    elif event.key == K_a:
        player.move_left()
    if event.key == K_w:
        if player.OnGround:
            player.jump()


def keyup(event):
    global player

    if event.key == K_d:
        player.x_vel = 0
    elif event.key == K_a:
        player.x_vel = 0


init_surface()
pygame.display.update()

while True:

    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        if e.type == KEYDOWN:
            keydown(e)
        elif e.type == KEYUP:
            keyup(e)

    draw()

    pygame.display.update()

    FPSCLOCK.tick(FPS)
