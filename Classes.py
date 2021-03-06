import pygame
from pygame.locals import *


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Player(Entity):
    def __init__(self, x, y, group):
        Entity.__init__(self)
        self.pos = [x, y]
        self.x_vel = 0
        self.y_vel = 0
        self.OnGround = True
        self.Jumping = False
        self.image = pygame.image.load('p1_stand.png')
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))
        self.dt = 0
        self.gravity = 5
        self.group = group
        group.add(self)

    def collide_y(self, other):
        collidelist = pygame.sprite.spritecollide(self, other, False)
        for sprite in collidelist:
            if isinstance(sprite, FloorTile):
                self.rect.bottom = sprite.rect.top
                self.OnGround = True
                self.Jumping = False
                self.y_vel = 0
                self.dt = 0
            if isinstance(sprite, Box):
                if self.y_vel > 0 and self.rect.bottom + sprite.rect.height >= sprite.rect.top:
                    self.OnGround = True
                    self.Jumping = False
                    self.y_vel = 8
                    self.dt = 0
                    self.rect.bottom = sprite.rect.top
                elif self.y_vel > 0:
                    self.rect.bottom = sprite.rect.top
                    self.OnGround = True
                    self.Jumping = False
                    self.y_vel = 0
                elif self.y_vel < 0:
                    self.rect.top = sprite.rect.bottom

    def collide_x(self, other):
        collidelist = pygame.sprite.spritecollide(self, other, False)
        for sprite in collidelist:
            if isinstance(sprite, FloorTile):
                self.rect.bottom = sprite.rect.top
                self.OnGround = True
                self.Jumping = False
                self.y_vel = 0
                self.dt = 0
            if isinstance(sprite, Box):
                if self.x_vel > 0 and self.rect.right + sprite.rect.width >= sprite.rect.left:
                    self.rect.right = sprite.rect.left
                elif self.x_vel < 0 and self.rect.left - sprite.rect.width <= sprite.rect.right:
                    self.rect.left = sprite.rect.right
                if self.x_vel > 0:
                    self.rect.right = sprite.rect.left
                elif self.x_vel < 0:
                    self.rect.left = sprite.rect.right
                self.x_vel = 0

    def move_right(self):
        self.x_vel = 5

    def move_left(self):
        self.x_vel = -5

    def jump(self):
        self.y_vel = 0
        self.OnGround = False
        self.Jumping = True
        self.y_vel = -25

    def apply_gravity(self):
        self.dt += 1/60
        self.y_vel += (self.gravity * self.dt)
        self.y_vel = int(self.y_vel)

    def update(self):
        self.pos[0] = self.pos[0] + self.x_vel
        self.rect.x += self.x_vel
        self.collide_x(self.group)
        self.pos[1] = self.pos[1] + self.y_vel
        self.rect.y += self.y_vel
        self.collide_y(self.group)


class FloorTile(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.pos = [x, y]
        self.image = pygame.image.load('grass.png')
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))


class Box(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.pos = [x, y]
        self.image = pygame.image.load('box.png')
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))
