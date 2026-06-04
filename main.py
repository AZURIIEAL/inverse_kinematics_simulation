import pygame

from models import constants
from simulation.robot.cd_solver import CCDSolver
from models.robot import RobotArm
from models.inverse_kinematics.target import Target
from simulation.axes import AxisRenderer
from simulation.camera import Camera
from simulation.debug_overlay import DebugOverlay
from simulation.grid import GridRenderer
from simulation.renderer import Renderer
from simulation.robot.robot_renderer import RobotRenderer
from simulation.inverse_kinematics import TargetRenderer 

def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption(constants.TITLE)
    clock = pygame.time.Clock()

    renderer = Renderer(screen)
    camera = Camera()
    grid = GridRenderer()
    debug_overlay = DebugOverlay()
    robot = RobotArm()
    robot_renderer = RobotRenderer()
    solver = CCDSolver()
    
    # Initialize Target and its designated Renderer
    target = Target(200.0, 100.0)
    target_renderer = TargetRenderer()

    font = pygame.font.SysFont(None, 24)
    axes = AxisRenderer(font)

    running = True
    is_panning = False
    last_mouse_pos = (0, 0)

    while running:
        # Calculate delta time in seconds
        dt = clock.tick(constants.FPS) / constants.MS_TO_SEC

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Place Target With Left Click (Button 1)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                world_x, world_y = camera.screen_to_world(
                    mouse_x,
                    mouse_y,
                    constants.WINDOW_WIDTH,
                    constants.WINDOW_HEIGHT
                )
                target.x = world_x
                target.y = world_y

            # Start Panning (Middle Mouse Button / Button 2)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                is_panning = True
                last_mouse_pos = pygame.mouse.get_pos()

            # Stop Panning
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                is_panning = False

            # Execute Camera Pan
            elif event.type == pygame.MOUSEMOTION and is_panning:
                current_mouse_pos = pygame.mouse.get_pos()
                dx = float(current_mouse_pos[0] - last_mouse_pos[0])
                dy = float(current_mouse_pos[1] - last_mouse_pos[1])

                camera.pan(dx, dy)
                last_mouse_pos = current_mouse_pos

            # Execute Focal Zoom (Mouse Wheel)
            elif event.type == pygame.MOUSEWHEEL:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                zoom_factor = 1.1 if event.y > 0 else 0.9

                camera.zoom_at(
                    zoom_factor,
                    mouse_x,
                    mouse_y,
                    constants.WINDOW_WIDTH,
                    constants.WINDOW_HEIGHT
                )

        # --- Keyboard Input Polling (Frame-Rate Independent) ---
        keys = pygame.key.get_pressed()
        rotation_step = constants.JOINT_ROTATION_SPEED * dt

        # Joint 1 Control (Q / A)
        if keys[pygame.K_q]:
            robot.rotate_joint(0, -rotation_step)
        if keys[pygame.K_a]:
            robot.rotate_joint(0, rotation_step)

        # Joint 2 Control (W / S)
        if keys[pygame.K_w]:
            robot.rotate_joint(1, -rotation_step)
        if keys[pygame.K_s]:
            robot.rotate_joint(1, rotation_step)

        # --- World Space Telemetry Tracking ---
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_world = camera.screen_to_world(
            mouse_x,
            mouse_y,
            constants.WINDOW_WIDTH,
            constants.WINDOW_HEIGHT
        )

        # --- Render Pipeline ---
        renderer.clear(constants.BACKGROUND)

        # 1. Background Grid & Primary Reference Axes
        grid.draw(screen, camera, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        axes.draw(screen, camera, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        
        # 2. Main Simulation Layer (Robot Arm Assembly & Crosshair Target)
        robot_renderer.draw(screen, camera, robot, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        target_renderer.draw(screen, camera, target, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        solver.solve(robot,target,iterations=10)
        
        # 3. Heads-Up Status Information Layer (Drawn over everything else)
        debug_overlay.draw(screen, clock.get_fps(), camera, mouse_world, robot)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()