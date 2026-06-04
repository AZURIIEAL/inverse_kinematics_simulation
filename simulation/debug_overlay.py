import math
from typing import Any
import pygame

from simulation.camera import Camera


class DebugOverlay:
    """Renders a real-time telemetry overlay on the screen for debugging and metrics."""

    def __init__(self) -> None:
        self.font: pygame.font.Font = pygame.font.SysFont("consolas", 18)

    def draw(
        self,
        screen: pygame.Surface,
        fps: float,
        camera: Camera,
        mouse_world: tuple[float, float],
        robot: Any  # Explicitly passing the RobotArm instance to read link states
    ) -> None:
        """Blits system performance, camera metrics, and joint positions onto the viewport."""
        
        # Base telemetry lines
        lines: list[str] = [
            f"FPS: {fps:.1f}",
            f"Zoom: {camera.zoom:.2f}x",
            f"Camera X: {camera.x:.2f}",
            f"Camera Y: {camera.y:.2f}",
            f"Mouse World: ({mouse_world[0]:.2f}, {mouse_world[1]:.2f})"
        ]

        # Dynamically calculate and append the link angle metrics if links exist
        if hasattr(robot, "links") and len(robot.links) >= 2:
            joint_1_deg = math.degrees(robot.links[0].angle)
            joint_2_deg = math.degrees(robot.links[1].angle)
            
            lines.append(f"Joint 1: {joint_1_deg:.1f}°")
            lines.append(f"Joint 2: {joint_2_deg:.1f}°")

        y_offset: int = 10

        # Blit the unified instrumentation panel
        for line in lines:
            surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(surface, (10, y_offset))
            y_offset += 22