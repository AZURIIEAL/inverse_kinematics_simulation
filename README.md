...existing code...
# Inverse Kinematics Simulator

A minimal inverse kinematics simulation built with Pygame.

## Overview

This project displays an interactive inverse kinematics demo using a renderer and simple application configuration constants. The application entry point is [main.py](main.py). Core configuration values (window size, title, FPS, background color) are defined in [`models.constants`](models/constants.py), for example [`models.constants.TITLE`](models/constants.py), [`models.constants.WINDOW_WIDTH`](models/constants.py), [`models.constants.WINDOW_HEIGHT`](models/constants.py), and [`models.constants.FPS`](models/constants.py). The rendering logic is implemented in [simulation/renderer.py](simulation/renderer.py).

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
