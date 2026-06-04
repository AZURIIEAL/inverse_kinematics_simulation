import math
import pygame

# Assuming Camera class is in models.camera
from simulation.camera import Camera 
from models.constants import GRID_MINOR, GRID_MAJOR


class GridRenderer:
    """Handles rendering an infinite background grid with major and minor axes."""

    def __init__(self) -> None:
        self.minor_spacing: int = 25
        self.major_every: int = 4

    def draw(
        self,
        screen: pygame.Surface,
        camera: Camera,
        width: int,
        height: int
    ) -> None:
        """Draws major and minor grid lines based on the camera position and zoom."""
        spacing: float = self.minor_spacing * camera.zoom

        # Skip drawing if zoomed out too far to prevent layout clutter/crashes
        if spacing < 8:
            return

        start_x: float = -spacing
        end_x: float = width + spacing

        start_y: float = -spacing
        end_y: float = height + spacing

        world_left: float = camera.x - width / (2 * camera.zoom)
        world_top: float = camera.y - height / (2 * camera.zoom)

        first_x: float = math.floor(world_left / self.minor_spacing) * self.minor_spacing
        first_y: float = math.floor(world_top / self.minor_spacing) * self.minor_spacing

        # Draw Vertical Grid Lines
        x: float = first_x
        while True:
            screen_x, _ = camera.world_to_screen(x, 0.0, width, height)

            if screen_x > end_x:
                break

            index: int = int(round(x / self.minor_spacing))
            color: tuple[int, int, int] = (
                GRID_MAJOR if index % self.major_every == 0 else GRID_MINOR
            )

            pygame.draw.line(
                screen,
                color,
                (int(screen_x), int(start_y)),
                (int(screen_x), int(end_y))
            )
            x += self.minor_spacing

        # Draw Horizontal Grid Lines
        y: float = first_y
        while True:
            _, screen_y = camera.world_to_screen(0.0, y, width, height)

            if screen_y > end_y:
                break

            index = int(round(y / self.minor_spacing))
            color = GRID_MAJOR if index % self.major_every == 0 else GRID_MINOR

            pygame.draw.line(
                screen,
                color,
                (int(start_x), int(screen_y)),
                (int(end_x), int(screen_y))
            )
            y += self.minor_spacing