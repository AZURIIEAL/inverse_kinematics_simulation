class Camera:
    """Camera used to navigate the simulation world."""

    def __init__(self) -> None:
        self.x: float = 0.0
        self.y: float = 0.0
        self.zoom: float = 1.0

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

    def pan(self, dx: float, dy: float) -> None:
        """Move the camera in world space based on screen-space delta offsets."""
        self.x -= dx / self.zoom
        self.y -= dy / self.zoom

    def zoom_at(
        self,
        factor: float,
        mouse_x: float,
        mouse_y: float,
        screen_width: int,
        screen_height: int
    ) -> None:
        """Zooms the camera while keeping the point under the mouse stable."""
        # 1. Store world position before zoom
        world_x_before, world_y_before = self.screen_to_world(
            mouse_x, mouse_y, screen_width, screen_height
        )

        # 2. Apply zoom
        self.zoom *= factor

        # 3. Store world position after zoom (with same camera x/y)
        world_x_after, world_y_after = self.screen_to_world(
            mouse_x, mouse_y, screen_width, screen_height
        )

        # 4. Shift camera to compensate for the delta
        self.x -= (world_x_after - world_x_before)
        self.y -= (world_y_after - world_y_before)