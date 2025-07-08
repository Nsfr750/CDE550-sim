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
        self.setWindowTitle("Nidec CDE550 Simulatore - Aiuto")
        self.setMinimumSize(900, 700)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("Nidec CDE550 Simulatore - Aiuto")
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
        close_btn = QPushButton('Chiudi')
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
                    color: #fafafa;
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
            <h1>Nidec CDE550 Simulatore - Aiuto</h1>
            
            <div class="note">
                <p>Benvenuto nel Simulatore Nidec CDE550. Questa applicazione ti permette di simulare e testare le funzionalità dell'inverter Nidec CDE550.</p>
            </div>
            
            <h2>Per iniziare</h2>
            <p>Il simulatore fornisce un'interfaccia virtuale per l'inverter Nidec CDE550 con le seguenti funzionalità:</p>
            <ul>
                <li>Avvio/Arresto dell'inverter</li>
                <li>Regolazione della frequenza da 0 a 400 Hz</li>
                <li>Controllo della direzione (Avanti/Indietro)</li>
                <li>Monitoraggio in tempo reale dei parametri di uscita</li>
                <li>Simulazione e monitoraggio degli allarmi</li>
            </ul>
            
            <h2>Interfaccia utente</h2>
            
            <h3>Pannello di controllo</h3>
            <p>Il pannello di sinistra contiene tutti gli elementi di controllo:</p>
            <ul>
                <li><strong>AVVIO</strong> - Avvia l'inverter</li>
                <li><strong>FERMO</strong> - Arresta l'inverter</li>
                <li><strong>RESET</strong> - Reimposta lo stato dell'inverter</li>
                <li><strong>Direzione</strong> - Passa tra funzionamento Avanti e Indietro</li>
                <li><strong>Frequenza</strong> - Imposta la frequenza di uscita (0,0-400,0 Hz)</li>
            </ul>
            
            <h3>Pannello di stato</h3>
            <p>Il pannello di destra mostra lo stato corrente e i parametri:</p>
            <ul>
                <li><strong>Stato</strong> - Stato attuale (PRONTO, IN FUNZIONE, ALLARME)</li>
                <li><strong>Allarmi</strong> - Mostra gli allarmi attivi (se presenti)</li>
                <li><strong>Parametri</strong> - Mostra i valori in tempo reale di:
                    <ul>
                        <li>Tensione di uscita (V)</li>
                        <li>Corrente di uscita (A)</li>
                        <li>Velocità motore (giri/min)</li>
                        <li>Temperatura (°C)</li>
                    </ul>
                </li>
                <li><strong>Log comandi</strong> - Mostra la cronologia dei comandi e dei cambiamenti di stato</li>
            </ul>
            
            <h2>Opzioni del menu</h2>
            
            <h3>Menu File</h3>
            <ul>
                <li><strong>Esci</strong> - Chiudi l'applicazione</li>
            </ul>
            
            <h3>Menu Aiuto</h3>
            <ul>
                <li><strong>Aiuto</strong> - Mostra questa documentazione</li>
                <li><strong>Informazioni</strong> - Mostra le informazioni sull'applicazione</li>
                <li><strong>Sponsor</strong> - Informazioni sugli sponsor</li>
                <li><strong>Controlla aggiornamenti</strong> - Verifica la presenza di aggiornamenti</li>
            </ul>
            
            <div class="warning">
                <h3>Note importanti</h3>
                <ul>
                    <li>Questo è uno strumento di simulazione e non si collega ad hardware reale</li>
                    <li>Tutti i parametri mostrati sono valori simulati</li>
                    <li>Utilizzare questo strumento solo per scopi di test e sviluppo</li>
                </ul>
            </div>
            
            <div class="danger">
                <h3>Informazioni sulla sicurezza</h3>
                <p>Quando si lavora con veri inverter Nidec CDE550:</p>
                <ul>
                    <li>Seguire sempre le linee guida sulla sicurezza del produttore</li>
                    <li>Assicurarsi una corretta messa a terra e connessioni elettriche</li>
                    <li>Disconnettere l'alimentazione prima di eseguire qualsiasi manutenzione</li>
                    <li>Solo personale qualificato dovrebbe eseguire interventi sull'apparecchiatura</li>
                </ul>
            </div>
            
            <h2>Scorciatoie da tastiera</h2>
            <ul>
                <li><span class="key">F1</span> - Mostra questo aiuto</li>
                <li><span class="key">Ctrl+Q</span> - Esci dall'applicazione</li>
            </ul>
            
            <div class="note" style="margin-top: 30px;">
                <p>Per ulteriore supporto o per segnalare problemi, visita il nostro <a href="https://github.com/Nsfr750/CDE550-sim">repository GitHub</a>.</p>
                <p>Simulatore Commander CDE550 &copy; 2025 di Nsfr750 - Tutti i diritti riservati</p>
            </div>
        </body>
        </html>
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())
