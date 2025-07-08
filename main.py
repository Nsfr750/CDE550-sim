import sys
import os
from PyQt6.QtWidgets import (QMainWindow, QApplication, QMenuBar, QMenu, 
                            QStatusBar, QWidget, QVBoxLayout, QLabel, QMessageBox,
                            QHBoxLayout, QPushButton, QDoubleSpinBox, QComboBox, QGroupBox)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QIcon, QFont

# Add the script directory to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

# Import simulator components
try:
    from inverter_sim import InverterSimulato
    from serial_handler import SerialHandler
except ImportError as e:
    print(f"Errore importando componenti del simulatore: {e}")
    raise

class SimulatorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inverter = InverterSimulato()
        self.serial_handler = SerialHandler(self.inverter)
        self.init_ui()
        self.setup_timer()
        
    def init_ui(self):
        main_layout = QHBoxLayout(self)
        
        # Left panel - Controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Control group
        control_group = QGroupBox("Controllo")
        control_layout = QVBoxLayout()
        
        # Control buttons
        self.btn_start = QPushButton("AVVIA")
        self.btn_stop = QPushButton("FERMA")
        self.btn_reset = QPushButton("RESET")
        self.btn_start.setStyleSheet("background-color: #4CAF50; color: white;")
        self.btn_stop.setStyleSheet("background-color: #f44336; color: white;")
        self.btn_reset.setStyleSheet("background-color: #2196F3; color: white;")
        
        # Direction
        self.direction_combo = QComboBox()
        self.direction_combo.addItems(["AVANTI", "INDIETRO"])
        
        control_layout.addWidget(self.btn_start)
        control_layout.addWidget(self.btn_stop)
        control_layout.addWidget(self.btn_reset)
        control_layout.addWidget(QLabel("Direction:"))
        control_layout.addWidget(self.direction_combo)
        control_group.setLayout(control_layout)
        
        # Parameters group
        param_group = QGroupBox("Parametri")
        param_layout = QVBoxLayout()
        
        # Frequency
        freq_layout = QHBoxLayout()
        freq_layout.addWidget(QLabel("Frequenza (Hz):"))
        self.freq_spin = QDoubleSpinBox()
        self.freq_spin.setRange(0.0, 400.0)
        self.freq_spin.setValue(50.0)
        self.freq_spin.setDecimals(1)
        freq_layout.addWidget(self.freq_spin)
        
        # Voltage
        volt_layout = QHBoxLayout()
        volt_layout.addWidget(QLabel("Voltaggio (V):"))
        self.volt_label = QLabel("0.0")
        volt_layout.addWidget(self.volt_label)
        
        # Current
        current_layout = QHBoxLayout()
        current_layout.addWidget(QLabel("Corrente (A):"))
        self.current_label = QLabel("0.0")
        current_layout.addWidget(self.current_label)
        
        # Speed
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Velocità (RPM):"))
        self.speed_label = QLabel("0")
        speed_layout.addWidget(self.speed_label)
        
        param_layout.addLayout(freq_layout)
        param_layout.addLayout(volt_layout)
        param_layout.addLayout(current_layout)
        param_layout.addLayout(speed_layout)
        param_group.setLayout(param_layout)
        
        left_layout.addWidget(control_group)
        left_layout.addWidget(param_group)
        left_layout.addStretch()
        
        # Right panel - Status and alarms
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Status
        status_group = QGroupBox("Stato")
        status_layout = QVBoxLayout()
        self.status_label = QLabel("PRONTO")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50;")
        status_layout.addWidget(self.status_label)
        
        # Alarms
        self.alarm_label = QLabel("Nessun Allarme")
        self.alarm_label.setStyleSheet("color: #f44336;")
        status_layout.addWidget(self.alarm_label)
        
        # Temperature
        temp_layout = QHBoxLayout()
        temp_layout.addWidget(QLabel("Temperatura (°C):"))
        self.temp_label = QLabel("25")
        temp_layout.addWidget(self.temp_label)
        status_layout.addLayout(temp_layout)
        
        status_group.setLayout(status_layout)
        
        # Serial log
        log_group = QGroupBox("Log dei Comandi")
        log_layout = QVBoxLayout()
        self.log_text = QLabel()
        self.log_text.setWordWrap(True)
        log_layout.addWidget(self.log_text)
        log_group.setLayout(log_layout)
        
        right_layout.addWidget(status_group)
        right_layout.addWidget(log_group)
        
        # Add panels to main layout
        main_layout.addWidget(left_panel, stretch=1)
        main_layout.addWidget(right_panel, stretch=1)
        
        # Setup connections
        self.setup_connections()
    
    def setup_connections(self):
        self.btn_start.clicked.connect(self.start_inverter)
        self.btn_stop.clicked.connect(self.stop_inverter)
        self.btn_reset.clicked.connect(self.reset_inverter)
        self.freq_spin.valueChanged.connect(self.update_frequency)
        self.direction_combo.currentTextChanged.connect(self.change_direction)
    
    def setup_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(200)  # Update UI every 200ms
    
    def update_ui(self):
        # Update UI with simulator data
        self.freq_spin.blockSignals(True)
        self.freq_spin.setValue(self.inverter.frequenza_uscita)
        self.freq_spin.blockSignals(False)
        
        self.volt_label.setText(f"{self.inverter.tensione_uscita:.1f}")
        self.current_label.setText(f"{self.inverter.corrente_uscita:.2f}")
        self.speed_label.setText(f"{int(self.inverter.velocita_motore)}")
        self.temp_label.setText(f"{self.inverter.temperatura}")
        
        # Update status
        if self.inverter.allarme_attivo:
            self.status_label.setText("ALLARME")
            self.status_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #f44336;")
            self.alarm_label.setText(self.inverter.descrizione_allarme)
        elif self.inverter.in_marcia:
            self.status_label.setText("IN MARCIA")
            self.status_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50;")
            self.alarm_label.setText("No alarms")
        else:
            self.status_label.setText("PRONTO")
            self.status_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2196F3;")
            self.alarm_label.setText("No alarms")
            
        # Update direction
        self.direction_combo.blockSignals(True)
        self.direction_combo.setCurrentText("AVANTI" if self.inverter.direzione == 1 else "INDIETRO")
        self.direction_combo.blockSignals(False)
    
    def start_inverter(self):
        self.inverter.avvia()
        self.log_serial("Command: AVVIA")
        
    def stop_inverter(self):
        self.inverter.ferma()
        self.log_serial("Command: FERMA")
        
    def reset_inverter(self):
        self.inverter.reset()
        self.log_serial("Command: RESET")
        
    def update_frequency(self, freq):
        self.inverter.imposta_frequenza(freq)
        self.log_serial(f"Frequenza impostata: {freq} Hz")
        
    def change_direction(self, direction):
        dir_value = 1 if direction == "AVANTI" else -1
        self.inverter.cambia_direzione(dir_value)
        self.log_serial(f"Direzione cambaiata a: {direction}")
    
    def log_serial(self, message):
        current_text = self.log_text.text()
        if current_text:
            current_text += "\n"
        self.log_text.setText(current_text + message)
        self.log_text.adjustSize()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang = 'en'  # Default language
        self.setWindowTitle('Simulatore Nidec CDE550')
        self.setMinimumSize(1024, 768)  # Increased default size
        
        # Initialize UI
        self.init_ui()
        
        # Show status in status bar
        self.statusBar().showMessage('Pronto')
    
    def init_ui(self):
        """Initialize the user interface."""
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout(central_widget)
        
        # Add the simulator widget
        self.simulator = SimulatorWidget()
        layout.addWidget(self.simulator)
        
        # Create menu bar
        self.create_menu_bar()
    
    def create_menu_bar(self):
        """Create the menu bar and its actions."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('&File')
        
        # Exit action
        exit_action = QAction('&Esci', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menubar.addMenu('&Aiuto')
        
        # Help action
        help_action = QAction('&Aiuto', self)
        help_action.setShortcut('F1')
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)
               
        # Separator
        help_menu.addSeparator()
        
        # About action
        about_action = QAction('&Informazioni', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        # Sponsor action
        sponsor_action = QAction('&Sponsor', self)
        sponsor_action.triggered.connect(self.show_sponsor)
        help_menu.addAction(sponsor_action)

        # Separator
        help_menu.addSeparator()
        # Check for Updates action
        update_action = QAction('Controllo Aggiornamenti', self)
        update_action.triggered.connect(self.check_updates)
        help_menu.addAction(update_action)
    
    def show_about(self):
        """Show the About dialog."""
        try:
            from script.about import About
            About.show_about(self)
        except ImportError as e:
            QMessageBox.critical(self, 'Error', f'Could not load about dialog: {str(e)}')
    
    def show_help(self):
        """Show the Help window."""
        try:
            from script.help import HelpWindow
            HelpWindow.show_help(self)
        except ImportError as e:
            QMessageBox.critical(self, 'Error', f'Could not load help: {str(e)}')
    
    def show_sponsor(self):
        """Show the Sponsor dialog."""
        try:
            from script.sponsor import Sponsor
            Sponsor.show_sponsor(parent=self)
        except ImportError as e:
            QMessageBox.critical(self, 'Error', f'Could not load sponsor dialog: {str(e)}')
    
    def check_updates(self):
        """Check for application updates."""
        try:
            from script.updates import check_for_updates
            from script.version import get_version
            check_for_updates(parent=self, current_version=get_version())
        except ImportError as e:
            QMessageBox.critical(self, 'Error', f'Could not check for updates: {str(e)}')
    
    def closeEvent(self, event):
        """Handle the window close event."""
        # Clean up any running threads or resources here
        if hasattr(self, 'update_thread'):
            try:
                self.update_thread.stop()
            except:
                pass
        event.accept()

def main():
    try:
        # Create the application
        app = QApplication(sys.argv)
        
        # Set application style
        app.setStyle('Fusion')
        
        # Create and show the main window
        window = MainWindow()
        window.show()
        
        # Start the application event loop
        sys.exit(app.exec())
        
    except Exception as e:
        QMessageBox.critical(None, 'Fatal Error', f'Application failed to start: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main()
