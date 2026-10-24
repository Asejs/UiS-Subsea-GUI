# UiS Subsea – operatørgrensesnitt (prototype)

Tidlig prototype av operatørgrensesnittet til **Fenris**, ROV-en UiS Subsea bygde for MATE ROV World Championship 2022. Laget som del av bacheloroppgaven *Operatørgrensesnitt og topside-kommunikasjon for fjernstyrt undervannsfartøy* (Datateknologi, Universitetet i Stavanger, 2022) av Åse Jortveit Sagebakken og Vebjørn Lia Riiser.

Det ferdige topside-systemet ligger i [VebjornRiiser/uis-subsea](https://github.com/VebjornRiiser/uis-subsea).

## Om prosjektet

Topside-systemet styrer ROV-en fra land:

- **Operatørgrensesnitt** som viser sanntidsvideo fra front- og havbunnskamera, sensordata (dybde, orientering, temperatur, lekkasje, effektforbruk) og motorpådrag for thrustere og manipulator
- **Styring med Xbox-kontroller**, med kontrollerprofiler som kan endres i grensesnittet
- **Kommunikasjon over TCP** mellom topside og mini-PC-en i ROV-en, med kommandoer og sensordata i JSON
- **Videostrøm som MJPEG over HTTP**
- **Logging av sensordata** til fil, brukt til feilsøking under vanntestene

ROV-en ble vanntestet og kvalifiserte seg til MATE ROV World Championship 2022.

## Denne prototypen

Prototypen ble laget i starten av prosjektet, i januar 2022, for å prøve to tilnærminger:

- En webløsning i **Flask** med HTML, CSS og JavaScript, med utgangspunkt i fjorårets grensesnitt (`app/`)
- Et skrivebordsgrensesnitt i **PyQt5**, laget i Qt Designer (`SUBSEAGUI.ui`, `SUBSEAGUI.py`)

Gruppen valgte PyQt i det ferdige systemet.

## Kjøre webprototypen

```bash
pip install -r requirements.txt
python app.py
```

Åpne http://localhost:5000.
