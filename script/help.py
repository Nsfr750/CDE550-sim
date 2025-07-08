import os
import sys
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTextBrowser, 
                            QPushButton, QLabel, QApplication, QWidget, QScrollArea, QSizePolicy)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QFont

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Add script directory to Python path
script_dir = os.path.join(project_root, 'script')
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

class HelpWindow(QDialog):
    @staticmethod
    def show_help(parent=None):
        dialog = HelpWindow(parent)
        dialog.exec()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nidec CDE550 Simulator - Help")
        self.setMinimumSize(900, 700)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("Nidec CDE550 Simulator - Help")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(16)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)
        
        # Help content
        self.browser = QTextBrowser()
        self.browser.setOpenExternalLinks(True)
        self.browser.setHtml(self.get_help_content())
        main_layout.addWidget(self.browser)
        
        # Close button
        close_btn = QPushButton('Close')
        close_btn.clicked.connect(self.close)
        main_layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.setLayout(main_layout)
        
    def get_help_content(self):
        return """
        <html>
        <head>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    line-height: 1.6; 
                    margin: 20px;
                    color: #fafafa;
                }
                h1 { 
                    color: #1976D2; 
                    border-bottom: 2px solid #1976D2;
                    padding-bottom: 10px; 
                }
                h2 { 
                    color: #1976D2; 
                    margin-top: 25px;
                    border-bottom: 1px solid #e0e0e0;
                    padding-bottom: 5px;
                }
                h3 { 
                    color: #fbfbfb;
                    margin-top: 20px;
                }
                ul, ol { 
                    margin: 10px 0 10px 20px; 
                }
                li { 
                    margin: 8px 0; 
                }
                .note { 
                    color: #fafafa;
                    padding: 12px 16px;
                    border-radius: 4px;
                    margin: 15px 0;
                    border-left: 4px solid #1976D2;
                }
                .warning {  
                    padding: 12px 16px;
                    border-left: 4px solid #ff9800;
                    margin: 15px 0;
                    border-radius: 4px;
                    color: #fafafa;
                }
                .danger {
                    border-left: 4px solid #f44336;
                    padding: 12px 16px;
                    margin: 15px 0;
                    border-radius: 4px;
                    ccolor: #fafafa;
                }
                code { 
                    padding: 2px 6px; 
                    border-radius: 3px; 
                    font-family: 'Courier New', monospace;
                    font-size: 0.9em;
                    color: #fafafa;
                }
                a { 
                    color: #1976D2; 
                    text-decoration: none; 
                    font-weight: 500;
                }
                a:hover { 
                    text-decoration: underline;
                }
                .command {
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    padding: 8px 12px;
                    margin: 5px 0;
                    font-family: 'Courier New', monospace;
                    display: inline-block;
                }
                .key {
                    border: 1px solid #ddd;
                    border-radius: 3px;
                    padding: 1px 5px;
                    font-family: 'Courier New', monospace;
                    font-size: 0.9em;
                }
            </style>
        </head>
        <body>
            <h1>Nidec CDE550 Simulator - Help</h1>
            
            <div class="note">
                <p>Welcome to the Nidec CDE550 Simulator. This application allows you to simulate and test the Nidec CDE550 inverter functionality.</p>
            </div>
            
            <h2>Getting Started</h2>
            <p>The simulator provides a virtual interface to the Nidec CDE550 inverter with the following features:</p>
            <ul>
                <li>Start/Stop control of the inverter</li>
                <li>Frequency adjustment from 0 to 400 Hz</li>
                <li>Direction control (Forward/Reverse)</li>
                <li>Real-time monitoring of output parameters</li>
                <li>Alarm simulation and monitoring</li>
            </ul>
            
            <h2>User Interface</h2>
            
            <h3>Control Panel</h3>
            <p>The left panel contains all the control elements:</p>
            <ul>
                <li><strong>START</strong> - Starts the inverter</li>
                <li><strong>STOP</strong> - Stops the inverter</li>
                <li><strong>RESET</strong> - Resets the inverter state</li>
                <li><strong>Direction</strong> - Toggle between Forward and Reverse operation</li>
                <li><strong>Frequency</strong> - Set the output frequency (0.0-400.0 Hz)</li>
            </ul>
            
            <h3>Status Panel</h3>
            <p>The right panel displays the current status and parameters:</p>
            <ul>
                <li><strong>Status</strong> - Current state (READY, RUNNING, ALARM)</li>
                <li><strong>Alarms</strong> - Displays active alarms (if any)</li>
                <li><strong>Parameters</strong> - Shows real-time values for:
                    <ul>
                        <li>Output Voltage (V)</li>
                        <li>Output Current (A)</li>
                        <li>Motor Speed (RPM)</li>
                        <li>Temperature (°C)</li>
                    </ul>
                </li>
                <li><strong>Command Log</strong> - Shows the history of commands and state changes</li>
            </ul>
            
            <h2>Menu Options</h2>
            
            <h3>File Menu</h3>
            <ul>
                <li><strong>Exit</strong> - Close the application</li>
            </ul>
            
            <h3>Help Menu</h3>
            <ul>
                <li><strong>Help</strong> - Show this help documentation</li>
                <li><strong>About</strong> - Show application information</li>
                <li><strong>Sponsor</strong> - Information about sponsors</li>
                <li><strong>Check for Updates</strong> - Check for application updates</li>
            </ul>
            
            <div class="warning">
                <h3>Important Notes</h3>
                <ul>
                    <li>This is a simulation tool and does not connect to real hardware</li>
                    <li>All parameters shown are simulated values</li>
                    <li>Use this tool for testing and development purposes only</li>
                </ul>
            </div>
            
            <div class="danger">
                <h3>Safety Information</h3>
                <p>When working with real Nidec CDE550 inverters:</p>
                <ul>
                    <li>Always follow the manufacturer's safety guidelines</li>
                    <li>Ensure proper grounding and electrical connections</li>
                    <li>Disconnect power before performing any maintenance</li>
                    <li>Only qualified personnel should service the equipment</li>
                </ul>
            </div>
            
            <h2>Keyboard Shortcuts</h2>
            <ul>
                <li><span class="key">F1</span> - Show this help</li>
                <li><span class="key">Ctrl+Q</span> - Exit application</li>
            </ul>
            
            <div class="note" style="margin-top: 30px;">
                <p>For additional support or to report issues, please visit our <a href="https://github.com/Nsfr750/CDE550-sim">GitHub repository</a>.</p>
                <p>CDE550 Simulator &copy; 2025 by Nsfr750 - All rights reserved</p>
            </div>
        </body>
        </html>
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())
