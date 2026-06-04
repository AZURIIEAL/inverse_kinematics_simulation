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

### 2. Focal Zoom Logic
To keep the point under the mouse stable while zooming, the camera position $C$ is shifted based on the zoom change:
$$C_{new} = C_{old} + (S_{mouse} - \text{Center}_{screen}) \cdot \left(\frac{1}{Z_{old}} - \frac{1}{Z_{new}}\right)$$
*This ensures that the world coordinate relative to the mouse cursor remains invariant during scaling.*

### 3. Infinite Grid Rendering
The `GridRenderer` ensures that the grid appears infinite by snapping the rendering window to the nearest grid lines:
*   **Snap Logic:** `first_x = floor(world_left / spacing) * spacing`
*   **Performance:** Lines are only drawn within the visible screen bounds (plus a small buffer).

## Camera Controls

| Action | Control |
| :--- | :--- |
| **Pan View** | Middle Mouse Button (Hold & Drag) |
| **Focal Zoom** | Mouse Wheel (Scroll Up/Down) |
| **Reset View** | (Coming soon) |

## Project Structure

The project follows a decoupled architecture, separating rendering logic from coordinate systems:

- **[`models/`](models/):** Contains domain models like [`Color`](models/color.py) and global [`constants`](models/constants.py).
- **[`simulation/`](simulation/):**
    - [`camera.py`](simulation/camera.py): Manages the viewport and coordinate math.
    - [`grid.py`](simulation/grid.py): Handles the mathematical layout of the background grid.
    - [`axes.py`](simulation/axes.py): Renders the primary Basis vectors and origin.
    - [`renderer.py`](simulation/renderer.py): Low-level Pygame drawing abstraction.

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
