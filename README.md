# IMGW Pogoda – Wrocław co godzinę

Skrypt w Pythonie automatycznie pobiera dane pogodowe z API IMGW dla stacji **Wrocław** co godzinę przez 24 godziny. Dane zapisywane są do pliku `pogoda_historia.txt`


POTRZEBA ZAINSTALOWAC 
- Python 3.13 (zalecany) oraz wybrać opcje przy instalacji "ADD PYTHON TO PATCH"
- Pakiet `requests` (pobieramy w konsoli: cmd,powershell,git bash) ja wybrałem visualStudioCode

INSTALACJA

1. Pobierz Pythona: [python.org](https://www.python.org/downloads/)
2. Zainstaluj pakiet:
   ```bash
   pip install requests