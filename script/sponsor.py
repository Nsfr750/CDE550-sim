from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                            QLabel, QWidget, QSizePolicy, QMessageBox)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices

# Sponsor Class
class Sponsor(QDialog):
    @staticmethod
    def show_sponsor(parent=None):
        dialog = Sponsor(parent)
        dialog.exec()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Sponsor')
        self.setMinimumSize(600, 200)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel('Support Development')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Button container
        btn_container = QWidget()
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.setSpacing(10)
        btn_layout.setContentsMargins(10, 0, 10, 0)
        
        # Sponsor buttons with their respective URLs
        buttons = [
            ('Sponsorizza su GitHub', "https://github.com/sponsors/Nsfr750"),
            ('Collegati su Discord', "https://discord.gg/BvvkUEP9"),
            ('Donazioni su PayPal', "https://paypal.me/3dmega"),
            ('Sponsorizza su Patreon', "https://www.patreon.com/Nsfr750")
        ]
        
        for text, url in buttons:
            btn = QPushButton(text, self)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            btn.setStyleSheet("""
                QPushButton {
                    padding: 8px;
                    background-color: #f0f0f0;
                    color: Black;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """)
            btn.clicked.connect(lambda checked, u=url: self.open_url(u))
            btn_layout.addWidget(btn)
        
        layout.addWidget(btn_container, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Close button
        close_btn = QPushButton('Chiudi', self)
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    
    def open_url(self, url):
        """Open the specified URL in the default web browser."""
        try:
            QDesktopServices.openUrl(QUrl(url))
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Could not open URL: {str(e)}')
