# Simulatore Nidec Commander CDE 550

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Version](https://img.shields.io/badge/version-0.0.2-green.svg)](CHANGELOG.md)

Simulatore software dell'inverter Nidec Commander CDE 550 con interfaccia grafica, sviluppato in Python con PyQt6.

## Novità nella versione 0.0.2

- **Localizzazione completa** in italiano dell'interfaccia utente
- **Migliorata la gestione degli allarmi** con riduzione dei falsi positivi
- **Ottimizzazioni delle prestazioni** durante l'avvio e la variazione di carico
- **Documentazione aggiornata** con CHANGELOG dettagliato

## Funzionalità

- Simulazione realistica del comportamento di un inverter Nidec Commander CDE 550
- Interfaccia grafica intuitiva con PyQt6 completamente localizzata in italiano
- Comunicazione seriale tramite pyserial
- Supporto per i principali comandi di controllo
- Simulazione di guasti e allarmi con gestione avanzata
- Monitoraggio in tempo reale dei parametri
- Log degli eventi e degli errori

## Prerequisiti

- Python 3.8 o superiore
- Pip (gestore pacchetti Python)
- Ambiente virtuale Python (consigliato)

## Installazione

1. Clona il repository:
   ```bash
   git clone https://github.com/Nsfr750/CDE550-sim.git
   cd CDE550-sim
   ```

2. Crea e attiva un ambiente virtuale (opzionale ma consigliato):
   ```bash
   # Su Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Su macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo

1. Avvia il simulatore:
   ```bash
   python main.py
   ```

2. L'interfaccia grafica mostrerà:
   - Stato dell'inverter
   - Parametri operativi
   - Log degli eventi
   - Controlli di simulazione

3. Per la connessione seriale:
   - Menù Connessione -> Connetti
   - Seleziona la porta COM desiderata
   - Imposta la velocità di comunicazione (baud rate)
   - Clicca su "Connetti"

## Comandi seriali supportati

| Comando | Descrizione | Esempio |
|---------|-------------|---------|
| `RUN` | Avvia l'inverter | `RUN` |
| `STOP` | Ferma l'inverter | `STOP` |
| `RST` | Resetta gli allarmi | `RST` |
| `FREQ <valore>` | Imposta la frequenza (Hz) | `FREQ 50.0` |
| `DIR <1\|-1>` | Imposta la direzione | `DIR 1` (avanti) |
| `STATUS` | Mostra lo stato completo | `STATUS` |
| `HELP` | Mostra l'elenco comandi | `HELP` |

## Struttura del progetto

```
CDE550-sim/
├── main.py              # Punto di ingresso dell'applicazione
├── inverter_sim.py      # Logica di simulazione dell'inverter
├── serial_handler.py    # Gestione comunicazione seriale
├── script/              # File dell'interfaccia utente e aiuto
│   ├── help.py          # Finestra di aiuto
│   ├── serial_dialog.py # Finestra di connessione seriale
│   └── version.py       # Gestione versione
├── requirements.txt     # Dipendenze del progetto
├── README.md            # Documentazione principale
└── CHANGELOG.md         # Registro delle modifiche
```

## Contributi

I contributi sono ben accetti! Per proporre miglioramenti:

1. Crea un fork del progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Fai commit delle tue modifiche (`git commit -m 'Aggiungi una nuova funzionalità'`)
4. Pusha il branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## Licenza

Distribuito sotto licenza GPL-3.0. Vedi `LICENSE` per maggiori informazioni.

## Contatti

- Autore: Nsfr750
- Email: [nsfr750@yandex.com]
- Repository: https://github.com/Nsfr750/CDE550-sim

---

<div align="center">
  <sub>Sviluppato con ❤️ da Nsfr750</sub>
</div>
