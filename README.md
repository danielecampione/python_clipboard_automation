# Automazione Appunti Windows 11 - Versione Python

## Descrizione
Questa è la versione Python 3 del progetto di automazione degli appunti di Windows 11. Il programma utilizza tkinter per l'interfaccia grafica e PyAutoGUI per l'automazione dei tasti.

## Funzionalità
Il programma automatizza le seguenti operazioni:

1. **Apertura automatica di Notepad** su Windows 11 64-bit
2. **Click automatico** nell'area di testo per impostare il focus
3. **Utilizzo di Win+V** per aprire gli appunti multipli di Windows 11
4. **Attesa di 4 secondi** per evitare rallentamenti di rendering grafico
5. **Navigazione automatica** agli elementi degli appunti (4°, 3°, 2°, 1°)
6. **Incolla sequenziale** con pause di 1 secondo tra ogni elemento
7. **Interruzioni di riga automatiche** dopo ogni elemento incollato

## Prerequisiti
- **Windows 11** 64-bit
- **Python 3.6+** (con tkinter incluso)
- **Almeno 4 elementi** già copiati negli appunti di sistema
- **Dipendenze Python** (vedi requirements.txt)

## Installazione

### 1. Installare le dipendenze
```bash
pip install -r requirements.txt
```

### 2. Verificare l'installazione
```bash
python -c "import pyautogui, tkinter; print('Dipendenze installate correttamente')"
```

## Utilizzo

### Metodo 1: Esecuzione diretta
```bash
python main.py
```

### Metodo 2: Esecuzione del modulo GUI
```bash
python clipboard_gui.py
```

### Metodo 3: Esecuzione da IDE
Apri `main.py` nel tuo IDE Python preferito ed esegui il file.

## Struttura del Progetto
```
py_UB04_02/
├── main.py                    # Punto di ingresso dell'applicazione
├── clipboard_gui.py           # Interfaccia grafica tkinter
├── clipboard_automation.py    # Logica di business per l'automazione
├── requirements.txt           # Dipendenze Python
└── README.md                 # Questa documentazione
```

## Architettura
- **main.py** - Punto di ingresso che avvia l'applicazione
- **clipboard_gui.py** - Interfaccia grafica con tkinter, gestisce l'interazione utente
- **clipboard_automation.py** - Logica di business separata, gestisce l'automazione

## Dipendenze
- **pyautogui** - Automazione GUI (simulazione tasti e mouse)
- **Pillow** - Gestione immagini (dipendenza di PyAutoGUI)
- **pygetwindow** - Gestione finestre (opzionale)
- **tkinter** - GUI (incluso in Python standard)

## Note Tecniche
- **Separazione delle responsabilità**: GUI e logica di business sono completamente separate
- **Threading**: L'automazione viene eseguita in un thread separato per non bloccare l'interfaccia
- **Gestione errori**: Ogni operazione è protetta da try-catch con messaggi informativi
- **Timing ottimizzato**: Pause appropriate per evitare problemi di rendering

## Timing e Pause
- **4 secondi** di attesa dopo Win+V per il rendering degli appunti
- **1 secondo** di pausa tra ogni operazione di incolla
- **2 secondi** di attesa iniziale per l'apertura di Notepad
- **0.1 secondi** tra le pressioni dei tasti di navigazione

## Risoluzione Problemi

### Errore: ModuleNotFoundError
```bash
pip install pyautogui pillow
```

### Errore: PyAutoGUI non funziona
- Assicurati che Windows 11 abbia gli appunti multipli abilitati
- Verifica che ci siano almeno 4 elementi negli appunti
- Controlla che Notepad possa essere aperto normalmente

### Errore: tkinter non trovato
- Su alcune distribuzioni Linux: `sudo apt-get install python3-tk`
- Su Windows: tkinter è incluso nell'installazione standard di Python

## Compatibilità
- **Python**: 3.6+
- **Sistema Operativo**: Windows 11 (testato su 64-bit)
- **GUI Framework**: tkinter (standard)
- **Automazione**: PyAutoGUI