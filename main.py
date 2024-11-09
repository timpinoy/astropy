import pygame

from constants import *
from player import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()

    score = 0
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 32)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # draw score
        text = font.render(str(score), 1, "red")
        textpos = text.get_rect(center=(screen.get_width()/2, 40))

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if player.check_collision(a):
                print("Game over!")
                return

            for s in shots:
                if a.check_collision(s):
                    s.kill()
                    a.split()
                    score += 1

        screen.fill("black")

        screen.blit(text, textpos)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
