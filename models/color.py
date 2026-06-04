from dataclasses import dataclass

@dataclass(frozen=True)
class Color:
    """Domain model representing an RGBA color."""
    r: int
    g: int
    b: int
    a: int = 255  # Default alpha to fully opaque

    def to_tuple(self) -> tuple[int, int, int, int]:
        """Convert the color model to a standard Pygame-compatible tuple."""
        return (self.r, self.g, self.b, self.a)