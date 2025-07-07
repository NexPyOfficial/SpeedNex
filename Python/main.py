import os
import speedtest
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from colorama import init, Fore
import threading


init(autoreset=True)


os.makedirs("logs", exist_ok=True)


def run_speedtest(callback=None):
    st = speedtest.Speedtest()
    best = st.get_best_server()

    if callback:
        callback(" Download in corso...")
    download = st.download()

    if callback:
        callback(" Upload in corso...")
    upload = st.upload()

    ping = st.results.ping

    result = {
        "Download": round(download / 1_000_000, 2),
        "Upload": round(upload / 1_000_000, 2),
        "Ping": round(ping, 2),
        "Server": f"{best['sponsor']} - {best['name']} ({best['country']})",
        "Host": best['host']
    }

    save_log(result)
    return result


def save_log(result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = f"logs/speedtest_{file_time}.txt"
    with open(log_path, "w") as f:
        f.write(f"{now}\n\n")
        f.write(f"Server: {result['Server']}\n")
        f.write(f"Host: {result['Host']}\n\n")
        f.write(f"Download: {result['Download']} Mbps\n")
        f.write(f"Ping: {result['Ping']} ms\n")
        f.write(f"Upload: {result['Upload']} Mbps\n")


def console_mode():
    print(Fore.CYAN + " Avvio Speed Test...\n")
    try:
        def live(msg): print(Fore.BLUE + msg)
        results = run_speedtest(callback=live)
        print(Fore.GREEN + "\n Risultati:")
        print(Fore.YELLOW + f"Server: {results['Server']}")
        print(Fore.YELLOW + f"Host: {results['Host']}")
        print(Fore.YELLOW + f"Download: {results['Download']} Mbps")
        print(Fore.YELLOW + f"Ping: {results['Ping']} ms")
        print(Fore.YELLOW + f"Upload: {results['Upload']} Mbps")
        print(Fore.CYAN + "\n Risultati salvati in /logs/")
    except Exception as e:
        print(Fore.RED + f" Errore: {e}")

# Modalità GUI
def gui_mode():
    def start_test():
        def update_status(msg):
            lbl_status.config(text=msg)
            root.update()

        def threaded_test():
            btn.config(state="disabled")
            update_status(" Connessione al server...")
            try:
                results = run_speedtest(callback=update_status)
                lbl_ping.config(text=f" Ping: {results['Ping']} ms")
                lbl_down.config(text=f" Download: {results['Download']} Mbps")
                lbl_up.config(text=f" Upload: {results['Upload']} Mbps")
                lbl_server.config(text=f" Server: {results['Server']}")
                update_status(" Test completato. Log salvato.")
            except Exception as e:
                messagebox.showerror("Errore", str(e))
                update_status(" Errore durante il test.")
            btn.config(state="normal")

        threading.Thread(target=threaded_test).start()

    root = tk.Tk()
    root.title("Speed Test Internet")
    root.geometry("400x320")
    root.configure(bg="#1e1e2f")

    title = tk.Label(root, text="Speed Test della Rete", font=("Helvetica", 16, "bold"), fg="white", bg="#1e1e2f")
    title.pack(pady=15)

    btn = ttk.Button(root, text="Avvia Speed Test", command=start_test)
    btn.pack(pady=10)

    lbl_status = tk.Label(root, text="", fg="lightblue", bg="#1e1e2f", font=("Helvetica", 11))
    lbl_status.pack(pady=5)

    lbl_server = tk.Label(root, text="🌐 Server: -", fg="white", bg="#1e1e2f", font=("Helvetica", 11))
    lbl_server.pack(pady=2)

    lbl_ping = tk.Label(root, text="📍 Ping: -", fg="white", bg="#1e1e2f", font=("Helvetica", 12))
    lbl_down = tk.Label(root, text="⬇️ Download: -", fg="white", bg="#1e1e2f", font=("Helvetica", 12))
    lbl_up = tk.Label(root, text="⬆️ Upload: -", fg="white", bg="#1e1e2f", font=("Helvetica", 12))

    lbl_ping.pack(pady=2)
    lbl_down.pack(pady=2)
    lbl_up.pack(pady=2)

    root.mainloop()

# Selezione modalità
def start():
    try:
        root = tk.Tk()
        root.withdraw()
        scelta = simpledialog.askstring("Modalità", "Scegli 'console' o 'gui'")
        root.destroy()

        if scelta:
            scelta = scelta.strip().lower()
            if scelta == "console":
                console_mode()
            elif scelta == "gui":
                gui_mode()
            else:
                messagebox.showerror("Errore", "Scelta non valida.")
        else:
            messagebox.showinfo("Annullato", "Nessuna scelta effettuata.")
    except Exception:
        print(Fore.MAGENTA + " GUI non disponibile. Passaggio alla modalità console.")
        scelta = input("Scrivi 'console' o 'gui': ").strip().lower()
        if scelta == "gui":
            try:
                gui_mode()
            except:
                print(Fore.RED + "❌ GUI non disponibile.")
        elif scelta == "console":
            console_mode()
        else:
            print(Fore.RED + "Scelta non valida.")

if __name__ == "__main__":
    start()
