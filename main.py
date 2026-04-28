"""
Main entry point for JARVIS-TonyStark-Edition
Starts the GUI and loads configuration
"""

import os
import sys
from src.ui_modern import JarvisUI
from src.jarvis_ai import JarvisAI
from PyQt5.QtWidgets import QApplication


def main():
    # Load configuration and initialize AI manager
    config_path = os.path.join(os.getcwd(), "config.json")
    ai_manager = JarvisAI(config_file=config_path)

    app = QApplication(sys.argv)
    window = JarvisUI()

    # Attach ai_manager to window for future integration
    window.ai_manager = ai_manager

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
