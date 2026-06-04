class Camera:
    """Camera used to navigate the simulation world."""

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.zoom = 1.0

    def world_to_screen(
        self,
        world_x: float,
        world_y: float,
        screen_width: int,
        screen_height: int
    ) -> tuple[float, float]:
        """Convert world coordinates into screen coordinates."""
        screen_x = (world_x - self.x) * self.zoom + (screen_width / 2)
        screen_y = (world_y - self.y) * self.zoom + (screen_height / 2)
        return screen_x, screen_y

    def screen_to_world(
        self,
        screen_x: float,
        screen_y: float,
        screen_width: int,
        screen_height: int
    ) -> tuple[float, float]:
        """Convert screen coordinates into world coordinates."""
        world_x = (screen_x - (screen_width / 2)) / self.zoom + self.x
        world_y = (screen_y - (screen_height / 2)) / self.zoom + self.y
        return world_x, world_y