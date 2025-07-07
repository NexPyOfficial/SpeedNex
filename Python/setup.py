import os
import sys
import zipfile
import shutil
import subprocess
from pathlib import Path

# Auto-elevazione a admin su Windows
def is_admin():
    import ctypes
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if os.name == "nt" and not is_admin():
    import ctypes
    # Rilancio lo script come admin e termino quello attuale
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

print("""
  _________________________________________________    _______  _______________  ___
 /   _____/\______   \_   _____/\_   _____/\______ \   \      \ \_   _____/\   \/  /
 \_____  \  |     ___/|    __)_  |    __)_  |    |  \  /   |   \ |    __)_  \     / 
 /        \ |    |    |        \ |        \ |    `   \/    |    \|        \ /     \ 
/_______  / |____|   /_______  //_______  //_______  /\____|__  /_______  //___/\  \
        \/                   \/         \/         \/         \/        \/       \_/
""")

print("[0] pip\n[1] pip3\n[2] Alternative")

c = input(">>>: ")

# Pacchetti da installare
packages = "speedtest-cli colorama tkinter"

if c == "0":
    os.system(f"pip install {packages}")
elif c == "1":
    os.system(f"pip3 install {packages}")
elif c == "2":
    os.system(f"py -m pip install {packages}")

# Verifica che requests e colorama siano installati
try:
    import requests
    from colorama import init, Fore, Style
except ImportError:
    print("[ERROR] Moduli mancanti. Per favore installali manualmente con 'pip install speedtest-cli colorama'")
    sys.exit(1)

# Inizializza colorama per i colori su Windows
init(autoreset=True)

print(f"{Fore.GREEN}Fatto!")
