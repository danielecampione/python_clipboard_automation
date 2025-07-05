# Clipboard Automation - Automazione Appunti usando la funzionalità "Cronologia Appunti" di Microsoft Windows 11 e 10 - Versione Python 3

## Descrizione
Questa è la versione Python 3 del progetto di automazione degli appunti usando la funzionalità "Cronologia Appunti" di Windows 11 e 10. Il programma utilizza il toolkit tkinter per l'interfaccia grafica e PyAutoGUI per l'automazione dei tasti.

## Funzionalità
Il programma automatizza le seguenti operazioni:

1. **Apertura automatica di Notepad** su Microsoft Windows 11 e 10 64-bit
2. **Utilizzo di Win+V** per usare la funzionalità "Cronologia Appunti" di Windows 11 e 10
3. **Attesa di 4 secondi** per evitare rallentamenti di rendering grafico
4. **Navigazione automatica** inversa degli elementi degli appunti (per esempio 4°, 3°, 2°, 1°)
5. **Aggiunta sequenziale tramite la funzionalità Incolla** con pause di 1 secondo tra ogni elemento
6. **Interruzioni di riga automatiche** dopo aver incollato l'intero contenuto degli appunti

## Prerequisiti
- **Microsoft Windows 11** 64-bit o **Microsoft Windows 10** 64-bit
- **Python 3.6+** (con tkinter incluso)
- **Elementi** già copiati negli appunti di sistema nella stessa quantità di quelli indicati dall'utente
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
python_clipboard_automation/
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

## Risoluzione Problemi

### Errore: ModuleNotFoundError
```bash
pip install pyautogui pillow
```

### Errore: PyAutoGUI non funziona
- Assicurati che Windows 11 abbia gli appunti multipli abilitati
- Verifica che ci siano gli elementi negli appunti nella stessa quantità indicata dall'utente
- Controlla che Notepad possa essere aperto normalmente

### Errore: tkinter non trovato
- Su alcune distribuzioni Linux: `sudo apt-get install python3-tk`
- Su Windows: tkinter è incluso nell'installazione standard di Python

## Compatibilità
- **Python**: 3.6+
- **Sistema Operativo**: Microsoft Windows 11 (testato su 64-bit), Microsoft Windows 10
- **GUI Framework**: tkinter (standard)
- **Automazione**: PyAutoGUI
