import pygame
from simulation.renderer import Renderer
import models.constants
from simulation.camera import Camera
from simulation.grid import GridRenderer

def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (models.constants.WINDOW_WIDTH,
        models.constants.WINDOW_HEIGHT)
    )

    pygame.display.set_caption(
        models.constants.TITLE
    )

    clock = pygame.time.Clock()
    renderer = Renderer(screen)
    camera = Camera()
    grid = GridRenderer()
    running = True

    while running:

        dt = clock.tick(models.constants.FPS) / models.constants.MS_TO_SEC
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        renderer.clear(models.constants.BACKGROUND)
        grid.draw(screen, camera, models.constants.WINDOW_WIDTH, models.constants.WINDOW_HEIGHT)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()