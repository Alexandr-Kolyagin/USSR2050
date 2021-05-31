import pygame

from data import db_session
from data.player import Player


class Playerg:
    def __init__(self, id=-1):
        db_sess = db_session.create_session()
        if id >= 0:
            player = db_sess.query(Player).filter(Player.id == id)[0]
            self.lvl = player.lvl
            self.name = "Владимир Михайлович Комаров"
            if player.name:
                self.nick = player.name
            self.x = player.x
            self.y = player.y
            self.pos = (self.x, self.y)
            self.speed = 2

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
