# Clipboard Automation – Clipboard History Automation for Microsoft Windows 11 and 10 using Python 3

## Description
This is the Python 3 version of the clipboard automation project using the `Clipboard History` feature in Windows 11 and 10. The program uses the `tkinter` toolkit for the graphical interface and `PyAutoGUI` for keystroke automation.

## Features
The program automates the following operations:

1. Automatically opens Notepad on Microsoft Windows 11 and 10 64-bit  
2. Uses Win+V to invoke the Windows Clipboard History  
3. Waits 4 seconds to prevent graphical rendering delays  
4. Reverse automatic navigation of clipboard elements (e.g. 4th, 3rd, 2nd, 1st)  
5. Sequential pasting with 1-second pauses between each item  
6. Automatic line breaks after pasting clipboard content

## Screenshot  
![Png](https://i.ibb.co/JR50q4wL/Immagine-2025-07-05-163132.png)

## Prerequisites
- Microsoft Windows 11 or 10 64-bit  
- Python 3.6+ with `tkinter`  
- Clipboard items already copied  
- Python dependencies (see `requirements.txt`)

## Installation

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Verify installation
```
python -c "import pyautogui, tkinter; print('Dependencies installed successfully')"
```

## Usage

### Method 1: Run directly  
```
python main.py
```

### Method 2: Run the GUI module  
```
python clipboard_gui.py
```

### Method 3: Run from an IDE  
Open `main.py` in your preferred Python IDE and run the file.

## Project Structure  
```
python_clipboard_automation/  
├── main.py  
├── clipboard_gui.py  
├── clipboard_automation.py  
├── requirements.txt  
└── README.md  
```

## Architecture
- `main.py` – Launches the application  
- `clipboard_gui.py` – GUI using tkinter; handles user interaction  
- `clipboard_automation.py` – Business logic for clipboard automation

## Dependencies
- pyautogui  
- Pillow  
- pygetwindow (optional)  
- tkinter

## Technical Notes
- Separation of concerns  
- Threaded automation  
- Error handling with informative messages  
- Optimized timing for stability

## Troubleshooting

### Error: ModuleNotFoundError
```
pip install pyautogui pillow
```

### Error: PyAutoGUI doesn’t work
- Ensure multiple clipboard history is enabled  
- Verify clipboard contains expected content  
- Confirm Notepad opens correctly

### Error: tkinter not found
- On Linux: `sudo apt-get install python3-tk`  
- On Windows: Already included

## Compatibility
- Python: 3.6+  
- Operating System: Windows 11/10 64-bit  
- GUI: tkinter  
- Automation: PyAutoGUI

---

# Clipboard Automation - Automazione Appunti usando la funzionalità `Cronologia Appunti` di Microsoft Windows 11 e 10 - Versione Python 3

## Descrizione
Questa è la versione Python 3 del progetto di automazione degli appunti usando la funzionalità `Cronologia Appunti` di Windows 11 e 10. Il programma utilizza il toolkit `tkinter` per l'interfaccia grafica e `PyAutoGUI` per l'automazione dei tasti.

## Funzionalità
Il programma automatizza le seguenti operazioni:

1. Apertura automatica di Notepad su Microsoft Windows 11 e 10 64-bit  
2. Utilizzo di Win+V per richiamare la cronologia degli appunti  
3. Attesa di 4 secondi per evitare rallentamenti grafici  
4. Navigazione inversa automatica degli elementi della cronologia  
5. Incollaggio sequenziale con pause di 1 secondo  
6. Interruzioni di riga automatiche dopo l’inserimento

## Screenshot  
![Png](https://i.ibb.co/JR50q4wL/Immagine-2025-07-05-163132.png)

## Prerequisiti
- Microsoft Windows 11 o 10 64-bit  
- Python 3.6+ con `tkinter` incluso  
- Elementi già copiati negli appunti  
- Dipendenze Python (vedi `requirements.txt`)

## Installazione

### 1. Installare le dipendenze  
```
pip install -r requirements.txt
```

### 2. Verificare l’installazione  
```
python -c "import pyautogui, tkinter; print('Dipendenze installate correttamente')"
```

## Utilizzo

### Metodo 1: Esecuzione diretta  
```
python main.py
```

### Metodo 2: Esecuzione del modulo GUI  
```
python clipboard_gui.py
```

### Metodo 3: Esecuzione da IDE  
Apri `main.py` nel tuo editor e avvia il file

## Struttura del Progetto  
```
python_clipboard_automation/  
├── main.py  
├── clipboard_gui.py  
├── clipboard_automation.py  
├── requirements.txt  
└── README.md  
```

## Architettura
- main.py – Avvia l’applicazione  
- clipboard_gui.py – GUI in tkinter  
- clipboard_automation.py – Logica di business

## Dipendenze
- pyautogui  
- Pillow  
- pygetwindow (opzionale)  
- tkinter  

## Note Tecniche
- Separazione tra GUI e logica  
- Automazione in thread separato  
- Gestione errori robusta  
- Timing ottimizzato

## Risoluzione Problemi

### Errore: ModuleNotFoundError  
```
pip install pyautogui pillow
```

### Errore: PyAutoGUI non funziona
- Attivare la cronologia appunti in Windows  
- Verificare che ci siano contenuti negli appunti  
- Assicurarsi che Notepad si apra normalmente

### Errore: tkinter non trovato
- Su Linux: `sudo apt-get install python3-tk`  
- Su Windows: già incluso

## Compatibilità
- Python: 3.6+  
- OS: Windows 11/10  
- GUI: tkinter  
- Automazione: PyAutoGUI

---

# 剪贴板自动化 – 使用 Python 3 和 Windows 11/10 的“剪贴板历史记录”功能进行自动化操作

## 描述  
这是一个基于 Python 3 的自动化项目，利用 Microsoft Windows 11 和 10 的“剪贴板历史记录”功能。程序使用 `tkinter` 图形界面和 `PyAutoGUI` 实现按键自动化。

## 功能  
该程序可自动执行以下操作：

1. 自动打开记事本（Windows 11 或 10，64 位）  
2. 使用 Win+V 打开剪贴板历史记录  
3. 等待 4 秒避免界面卡顿  
4. 倒序选择剪贴板项目（第 4 → 第 1）  
5. 每项粘贴间隔 1 秒  
6. 粘贴结束自动换行

## 截图  
![Png](https://i.ibb.co/JR50q4wL/Immagine-2025-07-05-163132.png)

## 前提条件  
- Windows 11 或 10（64 位）  
- Python 3.6+，需包含 `tkinter`  
- 剪贴板中已有项目  
- 依赖项请参阅 `requirements.txt`

## 安装步骤  

### 1. 安装依赖  
```  
pip install -r requirements.txt  
```

### 2. 验证安装  
```  
python -c "import pyautogui, tkinter; print('依赖项安装成功')"  
```

## 使用方法  

### 方法一：直接运行  
```  
python main.py  
```

### 方法二：运行图形界面模块  
```  
python clipboard_gui.py  
```

### 方法三：通过 IDE 启动  
在 IDE 中打开 `main.py` 并运行

## 项目结构  
```  
python_clipboard_automation/  
├── main.py  
├── clipboard_gui.py  
├── clipboard_automation.py  
├── requirements.txt  
└── README.md  
```

## 架构设计  
- main.py – 启动程序  
- clipboard_gui.py – `tkinter` 图形界面  
- clipboard_automation.py – 自动化核心逻辑

## 依赖项  
- pyautogui  
- Pillow  
- pygetwindow（可选）  
- `tkinter`

## 技术说明  
- 界面与逻辑分离清晰  
- 自动化运行于独立线程中  
- 异常处理健壮  
- 时间控制优化避免延迟

## 故障排查  

### 错误：ModuleNotFoundError  
```  
pip install pyautogui pillow  
```

### 错误：PyAutoGUI 无法运行  
- 请确认系统已启用剪贴板历史记录  
- 检查剪贴板是否已复制多个项目  
- 检查记事本是否能正常打开

### 错误：tkinter 未找到  
- 在 Linux 中执行：`sudo apt-get install python3-tk`  
- 在 Windows 上已默认包含

## 兼容性  
- Python：3.6+  
- 操作系统：Windows 11/10（64 位）  
- 图形界面：`tkinter`  
- 自动化工具：`PyAutoGUI`
