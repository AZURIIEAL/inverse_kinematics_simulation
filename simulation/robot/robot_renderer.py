from typing import List, Tuple
import pygame

from models.robot import RobotArm
from simulation.camera import Camera


class RobotRenderer:
    """Handles parsing world-space coordinates and rendering a robotic arm assembly."""

    def draw(
        self,
        screen: pygame.Surface,
        camera: Camera,
        robot: RobotArm,
        width: int,
        height: int
    ) -> None:
        """Pulls calculated joint positions from the domain model and draws the links and joints."""
        # Delegate forward kinematics processing to the domain model layer
        joint_positions: List[Tuple[float, float]] = robot.get_joint_positions()

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
                width=5
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