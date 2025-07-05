import subprocess
import time
import pyautogui
import os

class ClipboardAutomation:
    """
    Classe per l'automazione degli appunti di Windows 11
    Gestisce l'apertura di Notepad e l'automazione dei tasti per Win+V
    """
    
    def __init__(self):
        # Configura pyautogui per maggiore affidabilità
        pyautogui.PAUSE = 0.05
        pyautogui.FAILSAFE = True
        self.first_multiple_clipboard_usage = True
    
    def open_notepad(self):
        """
        Apre Notepad di Windows
        """
        try:
            subprocess.Popen(['notepad.exe'])
            # Attende che Notepad si apra completamente
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Errore nell'apertura di Notepad: {e}")
            return False
    
    def click_text_area(self):
        """
        Clicca nell'area di testo di Notepad per dare il focus
        """
        try:
            # Simula un click al centro dello schermo dove dovrebbe essere l'area di testo
            pyautogui.click(400, 300)
            # Pausa per assicurarsi che il focus sia impostato
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Errore nel click dell'area di testo: {e}")
            return False
    
    def open_clipboard_history(self):
        """
        Preme la combinazione Win+V per aprire gli appunti multipli
        """
        try:
            pyautogui.hotkey('win', 'v')
            # Attende 4 secondi per evitare rallentamenti di rendering grafico la prima volta
            waiting_time = 0.5
            if self.first_multiple_clipboard_usage:
                self.first_multiple_clipboard_usage = False
                waiting_time = 0.5
                time.sleep(waiting_time)
                waiting_time = 0.1
            time.sleep(waiting_time)
            return True
        except Exception as e:
            print(f"Errore nell'apertura degli appunti: {e}")
            return False
    
    def navigate_down(self, steps):
        """
        Naviga verso il basso nella lista degli appunti
        :param steps: numero di passi verso il basso
        """
        try:
            for i in range(steps):
                pyautogui.press('down')
                time.sleep(0.1)  # Piccola pausa tra le pressioni
            return True
        except Exception as e:
            print(f"Errore nella navigazione: {e}")
            return False
    
    def press_enter(self):
        """
        Preme Invio per confermare la selezione
        """
        try:
            pyautogui.press('enter')
            time.sleep(0.1)
            return True
        except Exception as e:
            print(f"Errore nella pressione di Invio: {e}")
            return False
    
    def press_the_separator_sequence(self):
        """
        Preme la sequenza per creare il separatore "---"
        """
        try:
            # Tre trattini
            pyautogui.press('-')
            pyautogui.press('-')
            pyautogui.press('-')
            time.sleep(0.1)
            return True
        except Exception as e:
            print(f"Errore nella creazione del separatore: {e}")
            return False
    
    def select_all(self):
        """
        Seleziona tutto il testo con Ctrl+A
        """
        try:
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.1)
            return True
        except Exception as e:
            print(f"Errore nella selezione di tutto: {e}")
            return False
    
    def copy_to_clipboard(self):
        """
        Copia il testo selezionato con Ctrl+C
        """
        try:
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.1)
            return True
        except Exception as e:
            print(f"Errore nella copia negli appunti: {e}")
            return False
    
    def wait_for(self, seconds):
        """
        Attende per il tempo specificato
        :param seconds: secondi di attesa
        """
        time.sleep(seconds)
    
    def paste_clipboard_item(self, position):
        """
        Incolla un elemento specifico dagli appunti
        :param position: posizione dell'elemento (1 = primo, 4 = quarto)
        """
        try:
            # Apre gli appunti
            if not self.open_clipboard_history():
                return False
            
            # Naviga alla posizione desiderata (position-1 perché partiamo da 0)
            if position > 1:
                if not self.navigate_down(position - 1):
                    return False
            
            # Incolla l'elemento selezionato
            if not self.press_enter():
                return False
            
            # Attende qualche istante per evitare che avvenga un doppio incolla
            self.wait_for(0.2)
            
            # Va a capo
            if not self.press_enter():
                return False
            
            return True
        except Exception as e:
            print(f"Errore nell'incollare l'elemento {position}: {e}")
            return False
    
    def execute_automation(self, number_of_elements=4, add_separator=True):
        """
        Esegue l'intera sequenza di automazione con parametri configurabili
        :param number_of_elements: numero di elementi da incollare (1-10)
        :param add_separator: se True aggiunge il separatore "---" alla fine
        """
        try:
            # Apre Notepad
            if not self.open_notepad():
                return False, "Errore nell'apertura di Notepad"
            
            # Attendi l'apertura del blocco note
            self.wait_for(1)
            
            # Incolla gli elementi nell'ordine richiesto: dal più recente al più vecchio
            for i in range(number_of_elements, 0, -1):
                if not self.paste_clipboard_item(i):
                    return False, f"Errore nell'incollare l'elemento {i}"
                
                # Pausa tra gli elementi (tranne l'ultimo)
                if i > 1:
                    self.wait_for(0.1)
            
            # Aggiunge il separatore solo se richiesto
            if add_separator:
                # Va a capo
                if not self.press_enter():
                    return False, "Errore nell'andare a capo"
                # Crea il separatore ---
                if not self.press_the_separator_sequence():
                    return False, "Errore nella creazione del separatore"
                # Va a capo due volte
                if not self.press_enter():
                    return False, "Errore nell'andare a capo"
                if not self.press_enter():
                    return False, "Errore nell'andare a capo"
            
            # Attende 100 millisecondi prima di selezionare e copiare tutto
            self.wait_for(0.1)
            
            # Seleziona tutto il contenuto
            if not self.select_all():
                return False, "Errore nella selezione di tutto il contenuto"
            
            # Copia tutto negli appunti
            if not self.copy_to_clipboard():
                return False, "Errore nella copia negli appunti"
            
            return True, "Automazione completata con successo"
            
        except Exception as e:
            return False, f"Errore generale nell'automazione: {e}"