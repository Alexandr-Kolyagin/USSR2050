import pygame
from render import Render
from player import Playerg
from data.player import Player
from data import db_session

def main():
    db_session.global_init("db/ussr.db")
    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    running = True
    id = 1
    player = Playerg(id=id)
    render = Render(screen, player)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        player.move()
        render.map()
        render.render_player()

        pygame.display.flip()

if __name__ == "__main__":
    main()