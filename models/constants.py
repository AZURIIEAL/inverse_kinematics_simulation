"""
Application configuration and color palette.
"""
from models.color import Color


TITLE = "Inverse Kinematics Simulator"
BACKGROUND = Color(r=20, g=20, b=20)
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
FPS = 60
MS_TO_SEC = 1000.0
GRID_MINOR = (35, 35, 35)
GRID_MAJOR = (50, 50, 50)
AXIS_X = (180, 60, 60)
AXIS_Y = (60, 180, 60)
TEXT = (220, 220, 220)  