import math
from typing import List, Tuple

from models.robot.link import Link


class RobotArm:
    """Domain model tracking base position, links, and rotation kinematics of the arm assembly."""

    def __init__(self) -> None:
        self.base_x: float = 0.0
        self.base_y: float = 0.0

        # Initializing a standard two-link arm setup with default lengths
        self.links: List[Link] = [
            Link(150.0, 0.0),
            Link(120.0, 0.0)
        ]

    def rotate_joint(self, joint_index: int, delta_angle: float) -> None:
        """Modifies a specific link's relative angle over time."""
        if 0 <= joint_index < len(self.links):
            self.links[joint_index].angle += delta_angle

    def get_joint_positions(self) -> List[Tuple[float, float]]:
        """Calculates world-space coordinates for all joints using Forward Kinematics."""
        positions: List[Tuple[float, float]] = [(self.base_x, self.base_y)]

        current_x: float = self.base_x
        current_y: float = self.base_y  # Cleaned up chained assignment typo
        accumulated_angle: float = 0.0

        for link in self.links:
            accumulated_angle += link.angle
            current_x += math.cos(accumulated_angle) * link.length
            current_y += math.sin(accumulated_angle) * link.length
            
            positions.append((current_x, current_y))

        return positions