import math
from typing import Any, List, Tuple
import pygame

from simulation.camera import Camera


class RobotRenderer:
    """Handles forward kinematics calculations and rendering for a robotic arm."""

    def draw(
        self,
        screen: pygame.Surface,
        camera: Camera,
        robot: Any,  # Replace with your Robot domain model type once defined
        width: int,
        height: int
    ) -> None:
        """Calculates joint positions via forward kinematics and renders links and joints."""
        base_x: float = robot.base_x
        base_y: float = robot.base_y

        joint_positions: List[Tuple[float, float]] = [(base_x, base_y)]

        current_x: float = base_x
        current_y: float = base_y
        accumulated_angle: float = 0.0

        # --- Forward Kinematics Pass ---
        for link in robot.links:
            accumulated_angle += link.angle
            current_x += math.cos(accumulated_angle) * link.length
            current_y += math.sin(accumulated_angle) * link.length
            joint_positions.append((current_x, current_y))

        # --- Render Pass: Links ---
        for i in range(len(joint_positions) - 1):
            x1, y1 = joint_positions[i]
            x2, y2 = joint_positions[i + 1]

            sx1, sy1 = camera.world_to_screen(x1, y1, width, height)
            sx2, sy2 = camera.world_to_screen(x2, y2, width, height)

            pygame.draw.line(
                screen,
                (200, 200, 200),
                (int(sx1), int(sy1)),
                (int(sx2), int(sy2)),
                5
            )

        # --- Render Pass: Joints ---
        for x, y in joint_positions:
            sx, sy = camera.world_to_screen(x, y, width, height)
            pygame.draw.circle(
                screen,
                (255, 200, 0),
                (int(sx), int(sy)),
                radius=8
            )