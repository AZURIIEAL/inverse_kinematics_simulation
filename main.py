import pygame

from models import constants
from simulation.axes import AxisRenderer
from simulation.camera import Camera
from simulation.grid import GridRenderer
from simulation.renderer import Renderer


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    renderer = Renderer(screen)
    camera = Camera()
    grid = GridRenderer()
    
    font = pygame.font.SysFont(None, 24)
    axes = AxisRenderer(font)

    running = True
    is_panning = False
    last_mouse_pos = (0, 0)

    while running:
        dt = clock.tick(constants.FPS) / constants.MS_TO_SEC

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start Panning (Middle Mouse Button)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                is_panning = True
                last_mouse_pos = pygame.mouse.get_pos()

            # Stop Panning
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                is_panning = False

            # Execute Camera Pan
            elif event.type == pygame.MOUSEMOTION and is_panning:
                current_mouse_pos = pygame.mouse.get_pos()
                dx = float(current_mouse_pos[0] - last_mouse_pos[0])
                dy = float(current_mouse_pos[1] - last_mouse_pos[1])
                
                camera.pan(dx, dy)
                last_mouse_pos = current_mouse_pos

            # Execute Focal Zoom (Mouse Wheel)
            elif event.type == pygame.MOUSEWHEEL:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                zoom_factor = 1.1 if event.y > 0 else 0.9
                
                camera.zoom_at(
                    zoom_factor,
                    mouse_x,
                    mouse_y,
                    constants.WINDOW_WIDTH,
                    constants.WINDOW_HEIGHT
                )

        # --- Update Viewport Title (Telemetry info) ---
        pygame.display.set_caption(
            f"{constants.TITLE} | "
            f"Camera ({camera.x:.2f}, {camera.y:.2f}) | "
            f"Zoom {camera.zoom:.2f}x"
        )

        # --- Render Pipeline ---
        renderer.clear(constants.BACKGROUND)
        grid.draw(screen, camera, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        axes.draw(screen, camera, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()