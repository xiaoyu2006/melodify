"""
Main module for the Melodify application.
"""

import sys
import random
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Slot, Qt


class MainWidget(QWidget):
    """Main widget of the application."""

    def __init__(self):
        """TODO"""
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        """self.button"""
        self.text.setText(random.choice(self.hello))


def main():
    """Main entry point for the application."""
    app = QApplication(sys.argv)

    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
