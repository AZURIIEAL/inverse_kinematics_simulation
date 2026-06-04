from typing import Any
import pygame

from simulation.camera import Camera


class TargetRenderer:
    """Handles rendering a stylized high-visibility crosshair target marker in screen-space."""

    def draw(
        self,
        screen: pygame.Surface,
        camera: Camera,
        target: Any,
        width: int,
        height: int
    ) -> None:
        """Draws a professional, high-visibility crosshair reticle at the target position."""
        sx, sy = camera.world_to_screen(target.x, target.y, width, height)
        
        int_sx: int = int(sx)
        int_sy: int = int(sy)

        inner_gap: int = 4      
        outer_ext: int = 15     
        radius: int = 10       
        
        # Color Palette
        color_accent: tuple[int, int, int] = (255, 80, 80)  
        color_shadow: tuple[int, int, int] = (20, 20, 20)    

        # ---------------------------------------------------------
        # PASS 1: Drop Shadow Outline (Drawn 1px wider & offset)
        # ---------------------------------------------------------
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ox, oy = int_sx + dx, int_sy + dy
            
            # Outer Ring Shadow
            pygame.draw.circle(screen, color_shadow, (ox, oy), radius, width=3)
            
            # Horizontal Line Shadows
            pygame.draw.line(screen, color_shadow, (ox - outer_ext, oy), (ox - inner_gap, oy), 3)
            pygame.draw.line(screen, color_shadow, (ox + inner_gap, oy), (ox + outer_ext, oy), 3)
            
            # Vertical Line Shadows
            pygame.draw.line(screen, color_shadow, (ox, oy - outer_ext), (ox, oy - inner_gap), 3)
            pygame.draw.line(screen, color_shadow, (ox, oy + inner_gap), (ox, oy + outer_ext), 3)

        # ---------------------------------------------------------
        # PASS 2: Primary Vector Layer (Core Red Reticle)
        # ---------------------------------------------------------
        # Main Tracking Ring
        pygame.draw.circle(screen, color_accent, (int_sx, int_sy), radius, width=2)

        # Left & Right horizontal crosshair lines with center gap
        pygame.draw.line(screen, color_accent, (int_sx - outer_ext, int_sy), (int_sx - inner_gap, int_sy), 2)
        pygame.draw.line(screen, color_accent, (int_sx + inner_gap, int_sy), (int_sx + outer_ext, int_sy), 2)

        # Top & Bottom vertical crosshair lines with center gap
        pygame.draw.line(screen, color_accent, (int_sx, int_sy - outer_ext), (int_sx, int_sy - inner_gap), 2)
        pygame.draw.line(screen, color_accent, (int_sx, int_sy + inner_gap), (int_sx, int_sy + outer_ext), 2)

        # Center Focal Precision Dot
        pygame.draw.circle(screen, color_accent, (int_sx, int_sy), radius=2)