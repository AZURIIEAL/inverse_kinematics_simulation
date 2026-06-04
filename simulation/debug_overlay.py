import pygame
from simulation.camera import Camera


class DebugOverlay:
    """Renders a real-time telemetry overlay on the screen for debugging."""

    def __init__(self) -> None:
        self.font: pygame.font.Font = pygame.font.SysFont("consolas", 18)

    def draw(
        self,
        screen: pygame.Surface,
        fps: float,
        camera: Camera,
        mouse_world: tuple[float, float]
    ) -> None:
        """Blits system performance and camera telemetry text onto the viewport."""
        lines: list[str] = [
            f"FPS: {fps:.1f}",
            f"Zoom: {camera.zoom:.2f}x",
            f"Camera X: {camera.x:.2f}",
            f"Camera Y: {camera.y:.2f}",
            f"Mouse World: ({mouse_world[0]:.2f}, {mouse_world[1]:.2f})"
        ]

        y_offset: int = 10

        for line in lines:
            surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(surface, (10, y_offset))
            y_offset += 22