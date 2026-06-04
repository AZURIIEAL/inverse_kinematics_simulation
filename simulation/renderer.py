import pygame


class Renderer:
    """
    Handles all rendering operations.
    """

    def __init__(self, screen):
        self.screen = screen

    def clear(self, color):
        self.screen.fill(color)