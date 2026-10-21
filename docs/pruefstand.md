# Prüfstand — 21.10.2026

| Repository | Ergebnis |
|---|---|
| SkytechHEMS | 906 Tests bestanden, 1 übersprungen; Ruff und Frontend-Build erfolgreich |
| Wallbox-Provider | 78 Tests bestanden; Ruff erfolgreich |
| Battery-Provider | 153 Tests bestanden; Ruff erfolgreich |
| Data Insight | 105 Tests bestanden, 27 übersprungen; Ruff erfolgreich |
| Energy Pilot | 637 Tests bestanden; Ruff erfolgreich |
| Powerflow-Card | 132 Tests bestanden; Typprüfung erfolgreich |
| EVMS-Vertragsabgleich | 13 Dateien in 8 Projektpaaren wortgleich; Watt-Protokollkopien gleich |

Die übersprungenen Tests benötigen zusätzliche Umgebung/Datenbank; diese Prüfung ist
keine PostgreSQL-/TimescaleDB-Abnahme. In Data Insight wurde keine Migration geändert.

Lokale HEMS-Formularprüfung mit Test-Supervisor: Anbindungsauswahl, Umschalten von
Ist-Sensor/Ausgabeeinheit auf Rückmeldungszeitlimit, Wattgrenzen, Übernahme eines
EVMS-Ladeziels in einen gültigen Entwurf sowie Hell-/Dunkel-Umschaltung geprüft.
Keine echte HA-Konfiguration gespeichert und keine Geräte angesteuert.

Hardwaretests sind ausdrücklich offen: go-e noch nicht geliefert. EVMS-Laufzeit,
Watt-Provider, RFID und Datenbankerweiterung sind in diesem Arbeitspaket nicht implementiert.
