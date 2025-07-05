import tkinter as tk
from tkinter import messagebox, ttk
import threading
import random
import math
import time
from clipboard_automation import ClipboardAutomation

class ClipboardGUI:
    """
    Interfaccia grafica tkinter per l'automazione degli appunti
    Replica le funzionalità dell'applicazione JavaFX
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.automation = ClipboardAutomation()
        self.bubbles = []
        self.bubble_animation_running = False
        self.setup_gui()
    
    def setup_gui(self):
        """
        Configura l'interfaccia grafica
        """
        # Configurazione finestra principale
        self.root.title("Automazione Appunti")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Centra la finestra sullo schermo
        self.center_window()
        
        # Canvas per le bolle (sfondo)
        self.bubble_canvas = tk.Canvas(self.root, width=500, height=400, highlightthickness=0)
        self.bubble_canvas.place(x=0, y=0)
        
        # Frame principale
        main_frame = ttk.Frame(self.root, padding="30")
        main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Crea i componenti
        self.create_components(main_frame)
        
        # Applica effetti ai componenti
        self.apply_component_effects()
        
        # Inizializza l'animazione delle bolle
        self.initialize_bubble_animation()
        
        # Gestisce la chiusura della finestra
        self.root.protocol("WM_DELETE_WINDOW", self.close_with_animation)
    
    def create_components(self, parent):
        """
        Crea tutti i componenti dell'interfaccia
        """
        # Titolo
        title_label = ttk.Label(
            parent, 
            text="Automazione Appunti",
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame per le configurazioni
        config_frame = ttk.LabelFrame(parent, text="Configurazione", padding="15")
        config_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20), sticky='ew')
        
        # Numero di elementi
        elements_label = ttk.Label(config_frame, text="Numero di elementi:")
        elements_label.grid(row=0, column=0, sticky='w', pady=(0, 10))
        
        self.elements_var = tk.IntVar(value=4)
        self.elements_spinner = ttk.Spinbox(
            config_frame,
            from_=1,
            to=10,
            textvariable=self.elements_var,
            width=10,
            state='readonly'
        )
        self.elements_spinner.grid(row=0, column=1, sticky='w', pady=(0, 10), padx=(10, 0))
        
        # Checkbox separatore
        self.separator_var = tk.BooleanVar(value=True)
        self.separator_checkbox = ttk.Checkbutton(
            config_frame,
            text="Aggiungi separatore '---'",
            variable=self.separator_var
        )
        self.separator_checkbox.grid(row=1, column=0, columnspan=2, sticky='w', pady=(0, 10))
        
        # Checkbox effetti speciali
        self.special_effects_var = tk.BooleanVar(value=True)
        self.special_effects_checkbox = ttk.Checkbutton(
            config_frame,
            text="Abilita effetti speciali",
            variable=self.special_effects_var,
            command=self.toggle_special_effects
        )
        self.special_effects_checkbox.grid(row=2, column=0, columnspan=2, sticky='w')
        
        # Pulsante di avvio
        self.start_button = ttk.Button(
            parent,
            text="Avvia Automazione",
            command=self.start_automation
        )
        self.start_button.grid(row=2, column=0, columnspan=2, pady=(0, 15))
        
        # Label di stato
        self.status_label = ttk.Label(
            parent,
            text="Pronto per l'automazione",
            font=('Arial', 10, 'bold'),
            foreground='green'
        )
        self.status_label.grid(row=3, column=0, columnspan=2)
        
        # Progress bar (inizialmente nascosta)
        self.progress = ttk.Progressbar(
            parent,
            mode='indeterminate',
            length=300
        )
        
        # Configura il grid
        config_frame.columnconfigure(1, weight=1)
    
    def center_window(self):
        """
        Centra la finestra sullo schermo
        """
        self.root.update_idletasks()
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def start_automation(self):
        """
        Avvia il processo di automazione
        """
        # Disabilita il pulsante durante l'esecuzione
        self.start_button.config(state='disabled')
        
        # Aggiorna lo stato
        self.status_label.config(
            text="Automazione in corso...",
            foreground='orange'
        )
        
        # Mostra la progress bar
        self.progress.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        self.progress.start()
        
        # Esegue l'automazione in un thread separato
        automation_thread = threading.Thread(
            target=self.run_automation,
            daemon=True
        )
        automation_thread.start()
    
    def run_automation(self):
        """
        Esegue l'automazione in un thread separato
        """
        try:
            # Piccola pausa prima di iniziare
            time.sleep(2)
            
            # Ottiene i valori configurati dall'utente
            number_of_elements = self.elements_var.get()
            add_separator = self.separator_var.get()
            
            # Esegue l'automazione con i parametri configurati
            success, message = self.automation.execute_automation(number_of_elements, add_separator)
            
            # Aggiorna l'interfaccia nel thread principale
            self.root.after(0, self.automation_completed, success, message)
            
        except Exception as e:
            # Gestisce gli errori
            self.root.after(0, self.automation_completed, False, f"Errore imprevisto: {e}")
    
    def automation_completed(self, success, message):
        """
        Chiamata quando l'automazione è completata
        """
        # Nasconde la progress bar
        self.progress.stop()
        self.progress.grid_remove()
        
        # Riabilita il pulsante
        self.start_button.config(state='normal')
        
        if success:
            # Successo
            self.status_label.config(
                text="Automazione completata con successo!",
                foreground='green'
            )
            messagebox.showinfo("Successo", message)
        else:
            # Errore
            self.status_label.config(
                text="Errore durante l'automazione",
                foreground='red'
            )
            messagebox.showerror("Errore", message)
    
    def apply_component_effects(self):
        """
        Applica effetti hover ai componenti
        """
        # Effetti sui componenti editabili
        self.apply_hover_effects(self.elements_spinner)
        self.apply_hover_effects(self.separator_checkbox)
        self.apply_hover_effects(self.special_effects_checkbox)
        self.apply_button_effects()
    
    def apply_hover_effects(self, widget):
        """
        Applica effetti hover semplici ai widget
        """
        def on_enter(event):
            # Effetto visivo semplice per tkinter/ttk
            try:
                widget.configure(cursor='hand2')
            except:
                pass
        
        def on_leave(event):
            try:
                widget.configure(cursor='')
            except:
                pass
        
        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)
    
    def apply_button_effects(self):
        """
        Applica effetti speciali al pulsante principale
        """
        def on_enter(event):
            if self.special_effects_var.get():
                # Effetto speciale con animazione
                self.animate_button_hover(True)
            else:
                # Effetto semplice
                try:
                    self.start_button.configure(cursor='hand2')
                except:
                    pass
        
        def on_leave(event):
            if self.special_effects_var.get():
                # Ritorno dall'effetto speciale
                self.animate_button_hover(False)
            else:
                # Ritorno dall'effetto semplice
                try:
                    self.start_button.configure(cursor='')
                except:
                    pass
        
        self.start_button.bind('<Enter>', on_enter)
        self.start_button.bind('<Leave>', on_leave)
    
    def animate_button_hover(self, entering):
        """
        Simula l'animazione del pulsante (versione semplificata per tkinter)
        """
        if entering:
            # Simula l'effetto di ingrandimento cambiando il testo
            original_text = self.start_button.cget('text')
            self.start_button.configure(text=f">>> {original_text} <<<")
            self.start_button.configure(cursor='hand2')
        else:
            # Ritorna al testo normale
            text = self.start_button.cget('text')
            if text.startswith('>>> ') and text.endswith(' <<<'):
                original_text = text[4:-4]  # Rimuove >>> e <<<
                self.start_button.configure(text=original_text)
            self.start_button.configure(cursor='')
    
    def initialize_bubble_animation(self):
        """
        Inizializza l'animazione delle bolle
        """
        self.bubble_animation_running = True
        self.create_bubble_periodically()
    
    def create_bubble_periodically(self):
        """
        Crea bolle periodicamente
        """
        if self.bubble_animation_running and self.special_effects_var.get():
            self.create_bubble()
        
        # Programma la prossima bolla
        if self.bubble_animation_running:
            self.root.after(800, self.create_bubble_periodically)
    
    def create_bubble(self):
        """
        Crea una nuova bolla animata
        """
        if not self.special_effects_var.get():
            return
        
        # Parametri casuali per la bolla
        radius = random.randint(3, 11)
        x = random.randint(radius, 500 - radius)
        y = 400 + radius
        
        # Colore blu trasparente (simulato con colore più chiaro)
        colors = ['#87CEEB', '#ADD8E6', '#B0E0E6', '#E0F6FF']
        color = random.choice(colors)
        
        # Crea la bolla
        bubble = self.bubble_canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=color, outline=color, width=1
        )
        
        # Aggiunge la bolla alla lista
        bubble_data = {
            'id': bubble,
            'x': x,
            'y': y,
            'radius': radius,
            'speed': random.uniform(1, 3),
            'sway': random.uniform(-1, 1),
            'sway_speed': random.uniform(0.02, 0.05)
        }
        self.bubbles.append(bubble_data)
        
        # Avvia l'animazione della bolla
        self.animate_bubble(bubble_data)
    
    def animate_bubble(self, bubble_data):
        """
        Anima una singola bolla
        """
        def move_bubble():
            if not self.bubble_animation_running:
                return
            
            # Aggiorna la posizione
            bubble_data['y'] -= bubble_data['speed']
            bubble_data['x'] += math.sin(bubble_data['y'] * bubble_data['sway_speed']) * bubble_data['sway']
            
            # Muove la bolla nel canvas
            try:
                self.bubble_canvas.coords(
                    bubble_data['id'],
                    bubble_data['x'] - bubble_data['radius'],
                    bubble_data['y'] - bubble_data['radius'],
                    bubble_data['x'] + bubble_data['radius'],
                    bubble_data['y'] + bubble_data['radius']
                )
                
                # Continua l'animazione se la bolla è ancora visibile
                if bubble_data['y'] > -bubble_data['radius']:
                    self.root.after(50, move_bubble)
                else:
                    # Rimuove la bolla quando esce dallo schermo
                    self.bubble_canvas.delete(bubble_data['id'])
                    if bubble_data in self.bubbles:
                        self.bubbles.remove(bubble_data)
            except:
                # La bolla è stata già rimossa
                if bubble_data in self.bubbles:
                    self.bubbles.remove(bubble_data)
        
        move_bubble()
    
    def toggle_special_effects(self):
        """
        Gestisce il toggle degli effetti speciali
        """
        if not self.special_effects_var.get():
            # Rimuovi tutte le bolle esistenti
            for bubble_data in self.bubbles[:]:
                try:
                    self.bubble_canvas.delete(bubble_data['id'])
                except:
                    pass
            self.bubbles.clear()
    
    def close_with_animation(self):
        """
        Chiude l'applicazione con animazione (versione semplificata)
        """
        # Ferma l'animazione delle bolle
        self.bubble_animation_running = False
        
        # Animazione di fade out semplificata
        def fade_out(alpha=1.0):
            if alpha > 0:
                self.root.attributes('-alpha', alpha)
                self.root.after(50, lambda: fade_out(alpha - 0.1))
            else:
                self.root.destroy()
        
        fade_out()
    
    def run(self):
        """
        Avvia l'interfaccia grafica
        """
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.root.quit()

def main():
    """
    Funzione principale per avviare l'applicazione
    """
    try:
        app = ClipboardGUI()
        app.run()
    except Exception as e:
        print(f"Errore nell'avvio dell'applicazione: {e}")
        messagebox.showerror("Errore di avvio", f"Impossibile avviare l'applicazione: {e}")

if __name__ == "__main__":
    main()