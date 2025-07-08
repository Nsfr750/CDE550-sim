# Simulatore Nidec Commander CDE 550

Questo è un simulatore software dell'inverter Nidec Commander CDE 550 con interfaccia grafica in Python.

## Funzionalità

- Simulazione realistica del comportamento di un inverter Nidec Commander CDE 550
- Interfaccia grafica intuitiva con PyQt6
- Comunicazione seriale tramite pyserial
- Supporto per i principali comandi di controllo
- Simulazione di guasti e allarmi

## Requisiti

- Python 3.8 o superiore
- PyQt6
- pyserial

## Installazione

1. Clona il repository o scarica i file sorgente
2. Installa le dipendenze:
   ```
   pip install -r requirements.txt
   ```

## Utilizzo

1. Avvia il simulatore con il comando:
   ```
   python main.py
   ```

2. L'interfaccia grafica mostrerà lo stato dell'inverter e i parametri principali

3. Per controllare l'inverter tramite porta seriale, connettiti alla porta specificata nell'interfaccia (di default cerca una porta COM disponibile)

## Comandi seriali supportati

- `RUN` - Avvia l'inverter
- `STOP` - Ferma l'inverter
- `RST` - Resetta gli allarmi
- `FREQ <valore>` - Imposta la frequenza (es: `FREQ 50.0`)
- `DIR <1|-1>` - Imposta la direzione (1=avanti, -1=indietro)
- `STATUS` - Mostra lo stato completo
- `HELP` - Mostra l'elenco dei comandi

## Struttura del progetto

- `main.py` - Avvio dell'applicazione e interfaccia grafica
- `inverter_sim.py` - Logica di simulazione dell'inverter
- `serial_handler.py` - Gestione della comunicazione seriale
- `requirements.txt` - Dipendenze del progetto

## Licenza

Questo progetto è rilasciato sotto licenza GPLv3.
