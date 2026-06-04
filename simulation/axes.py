import pygame
from simulation.camera import Camera
from models.constants import AXIS_X, AXIS_Y


class AxisRenderer:
    """Handles rendering the primary X/Y basis axes, origin marker, and labels."""

    def __init__(self, font: pygame.font.Font) -> None:
        self.font: pygame.font.Font = font

    def draw(
        self,
        screen: pygame.Surface,
        camera: Camera,
        width: int,
        height: int
    ) -> None:
        """Draws the main axes, an origin marker circle, and axis labels."""
        
        # 1. Calculate and Draw Core Axes
        origin_x, origin_y = camera.world_to_screen(0.0, 0.0, width, height)
        int_origin_x = int(origin_x)
        int_origin_y = int(origin_y)

        # Y Axis
        if 0 <= int_origin_x <= width:
            pygame.draw.line(screen, AXIS_Y, (int_origin_x, 0), (int_origin_x, height), 2)

        # X Axis
        if 0 <= int_origin_y <= height:
            pygame.draw.line(screen, AXIS_X, (0, int_origin_y), (width, int_origin_y), 2)

        # 2. Origin Marker (Rendered as a small solid circle at world 0,0)
        if 0 <= int_origin_x <= width and 0 <= int_origin_y <= height:
            pygame.draw.circle(
                screen,
                (255, 255, 255),
                (int_origin_x, int_origin_y),
                radius=6
            )

        # 3. Text Labels (X and Y markers blitted near screen boundaries)
        x_label = self.font.render("X", True, AXIS_X)
        screen.blit(
            x_label, 
            (width - 30, int_origin_y + 10)
        )

        y_label = self.font.render("Y", True, AXIS_Y)
        screen.blit(
            y_label, 
            (int_origin_x + 10, 10)
        )