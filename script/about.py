from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QPushButton, QApplication)
from PyQt6.QtCore import Qt
from script.version import get_version

class About(QDialog):
    @staticmethod
    def show_about(parent=None):
        dialog = About(parent)
        dialog.exec()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('About')
        self.setFixedSize(400, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel('CDE550 Simulator')
        title.setStyleSheet('font-size: 16px; font-weight: bold;')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Version
        version = QLabel("Versione: " + get_version())
        layout.addWidget(version, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Description
        description = QLabel('Simulatore del Nidec Commander CDE550')
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description)
        
        # Copyright
        copyright = QLabel('© 2025 Nsfr750')
        layout.addWidget(copyright, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Close button
        close_btn = QPushButton('Chiudi')
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
