# SpeedNex

SpeedNex è un tool Python per misurare la velocità della rete internet con due modalità: **Console** e **GUI**.  
Permette di eseguire test di velocità (download, upload, ping) con visualizzazione live e salva i risultati in log per consultazioni future.

---

## Caratteristiche

- Scelta tra interfaccia grafica (GUI) e modalità console all’avvio
- Visualizzazione live della progressione del test
- Report dettagliati con download, upload e ping
- Salvataggio automatico dei risultati in file di log (cartella `/logs/`)
- Utilizzo di librerie popolari: `speedtest-cli`, `tkinter`, `colorama`

---

## Requisiti

- Python 3.7 o superiore
- Librerie Python:
  - `speedtest-cli`
  - `colorama`

Installa le dipendenze con:

```bash
pip install -r requirements.txt
