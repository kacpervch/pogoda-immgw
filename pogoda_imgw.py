import requests
import time
from datetime import datetime

def pobierz_dane():
    url = "https://danepubliczne.imgw.pl/api/data/synop/station/wroclaw"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dane = response.json()

        with open("pogoda_historia.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            stacja = dane["stacja"]
            temperatura = dane.get("temperatura", "brak")
            cisnienie = dane.get("cisnienie", "brak")
            f.write(f"{stacja}: {temperatura}°C, ciśnienie: {cisnienie} hPa\n")
    except Exception as e:
        print(f"❌ Błąd: {e}")


for _ in range(24):
    pobierz_dane()
    print("✅ Dane pobane i zapisane. Czekam godzinę...")
    time.sleep(3600)  
