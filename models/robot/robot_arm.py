from models.robot.link import Link


class RobotArm:

    def __init__(self):

        self.base_x = 0.0
        self.base_y = 0.0

        self.links = [
            Link(150.0, 0.0),
            Link(120.0, 0.0)
        ]