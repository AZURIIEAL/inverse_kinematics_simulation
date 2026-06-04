...existing code...
# Inverse Kinematics Simulator

A minimal inverse kinematics simulation built with Pygame.

## Core Concepts & Math Logic

The simulation uses a custom coordinate transformation system to handle an infinite, zoomable world space.

### 1. Coordinate Transformations
The `Camera` class manages the translation and scaling between **World Space** (arbitrary units) and **Screen Space** (pixels).

*   **World to Screen:**
    $$S_x = (W_x - C_x) \cdot Z + \frac{W_{screen}}{2}$$
    $$S_y = (W_y - C_y) \cdot Z + \frac{H_{screen}}{2}$$
    *Where $C$ is the camera position, $Z$ is the zoom level, and $S$ is the resulting screen coordinate.*

*   **Screen to World:**
    $$W_x = \frac{S_x - \frac{W_{screen}}{2}}{Z} + C_x$$
    $$W_y = \frac{S_y - \frac{H_{screen}}{2}}{Z} + C_y$$

### 3. Forward Kinematics (FK)
The `RobotRenderer` calculates the posture of the arm by accumulating joint angles and applying planar trigonometry:
*   **Angle Accumulation:** $\Phi_i = \sum_{j=1}^{i} \theta_j$
*   **Joint Positions:**
    $$x_i = x_{i-1} + L_i \cos(\Phi_i)$$
    $$y_i = y_{i-1} + L_i \sin(\Phi_i)$$
    *Where $L_i$ is the length of link $i$, and $\theta_i$ is its relative angle.*

### 4. Infinite Grid Rendering
The `GridRenderer` ensures that the grid appears infinite by snapping the rendering window to the nearest grid lines using `math.floor` snap logic.

## Controls

| Category | Action | Key/Control |
| :--- | :--- | :--- |
| **Camera** | Pan View | Middle Mouse (Drag) |
| | Focal Zoom | Mouse Wheel |
| **Robot** | Joint 1 Rotate | `Q` / `A` |
| | Joint 2 Rotate | `W` / `S` |
| **Target** | Set Target | Left Mouse Click |

## Project Structure

The project is organized into modular packages for domain modeling and simulation logic:

- **[`models/`](models/):**
    - [`robot/`](models/robot/): Domain models for `RobotArm`, `Link`, and `Joint`.
    - [`inverse_kinematics/`](models/inverse_kinematics/): Logic for `Target` tracking.
    - [`color.py`](models/color.py), [`constants.py`](models/constants.py): Shared types.
- **[`simulation/`](simulation/):**
    - [`robot/`](simulation/robot/): Rendering logic for the robotic arm.
    - [`inverse_kinematics/`](simulation/inverse_kinematics/): Visual markers for IK targets.
    - [`camera.py`](simulation/camera.py), [`grid.py`](simulation/grid.py), [`axes.py`](simulation/axes.py): Viewport & environment rendering.
    - [`debug_overlay.py`](simulation/debug_overlay.py): Real-time telemetry (telemetry, FPS, coordinates).

## Setup

Follow these steps to set up the development environment:

1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   - **Command Prompt (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **PowerShell:**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the simulation using:
```bash
python main.py
```
