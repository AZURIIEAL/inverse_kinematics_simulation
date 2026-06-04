import pygame
from models.color import Color

class Renderer:
    """Handles all rendering operations using domain models."""

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen: pygame.Surface = screen

    def clear(self, color: Color) -> None:
        """Fills the screen surface using our structured Color model."""
        self.screen.fill(color.to_tuple())