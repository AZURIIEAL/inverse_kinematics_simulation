import math
from typing import List, Tuple
from models.robot import RobotArm
from models.inverse_kinematics.target import Target


class CCDSolver:
    """Inverse Kinematics solver utilizing Cyclic Coordinate Descent."""

    def solve(
        self,
        robot: RobotArm,
        target: Target,
        iterations: int = 10
    ) -> None:
        """Iteratively updates robot link angles using CCD to minimize end-effector distance to target."""
        target_pos: Tuple[float, float] = (target.x, target.y)

        for _ in range(iterations):
            # Evaluate joint positions at the start of the iteration
            positions: List[Tuple[float, float]] = robot.get_joint_positions()
            
            # Check if the end-effector is within the acceptable threshold
            if math.dist(positions[-1], target_pos) < 1.0:
                return

            # Traverse the kinematic chain backwards from the end-effector to base
            for joint_index in reversed(range(len(robot.links))):
                # Recalculate positions to account for intermediate joint updates
                positions = robot.get_joint_positions()
                
                joint_x, joint_y = positions[joint_index]
                end_x, end_y = positions[-1]

                # Vector from current joint axis to the end-effector
                vx1: float = end_x - joint_x
                vy1: float = end_y - joint_y

                # Vector from current joint axis to target marker
                vx2: float = target.x - joint_x
                vy2: float = target.y - joint_y

                # Calculate relative angles using quadrant-aware arctangent
                angle1: float = math.atan2(vy1, vx1)
                angle2: float = math.atan2(vy2, vx2)

                # Find angular displacement
                delta: float = angle2 - angle1

                # Normalize delta angle to stay within [-pi, pi] for shortest path rotation
                delta = math.atan2(math.sin(delta), math.cos(delta))

                # Apply displacement modification to the link state
                robot.links[joint_index].angle += delta