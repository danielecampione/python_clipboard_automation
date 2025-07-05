#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe principale per l'avvio dell'applicazione di automazione appunti
Compatibile con Python 3 e tkinter

Autore: Generato automaticamente
Versione: 1.0
Data: 2025
"""

from clipboard_gui import main as start_gui

def main():
    """
    Funzione principale che avvia l'interfaccia grafica tkinter
    """
    print("Avvio dell'applicazione di automazione appunti...")
    print("Assicurati di avere almeno 4 elementi negli appunti di sistema.")
    print("Premi Ctrl+C per terminare l'applicazione.")
    print("-" * 50)
    
    try:
        # Avvia l'interfaccia grafica tkinter
        start_gui()
    except KeyboardInterrupt:
        print("\nApplicazione terminata dall'utente.")
    except Exception as e:
        print(f"Errore nell'avvio dell'applicazione: {e}")
        input("Premi Invio per chiudere...")

if __name__ == "__main__":
    main()