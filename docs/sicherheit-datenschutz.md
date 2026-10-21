# Sicherheit und Datenhaltung

RFID ist im geplanten Betrieb eine Zuordnungshilfe und kein Beweis für die Identität
des angeschlossenen Fahrzeugs. Keine Sicherheitszusage zur Authentifizierung ableiten.
RFID-Kennungen und Ladezeiten können personenbezogen sein; Kennungen nicht in normale
Logs schreiben, Zugriff auf Verwaltung und Historie über HA beziehungsweise eigene DB-Rolle.

Ein Ausfall von Data Insight darf keine veraltete Ladezuordnung aktivieren.
Puffer und Betriebsstand müssen nach Wiederanlauf geprüft und Übertragungen idempotent sein.
Datenlücken ausdrücklich markieren. Zählerdifferenzen können Gesamtenergie rekonstruieren,
aber keine unbekannte Fahrzeugzuordnung oder den exakten zeitlichen Verlauf beweisen.

Hardwarezugriff ausschließlich über den Provider. Pro Anschluss ein Befehlsgeber.
EVMS- und HEMS-Lebenszeichen getrennt prüfen; ein lebendes EVMS darf eine abgelaufene
HEMS-Vorgabe nicht erneuern. Schutzfunktionen des Geräts bleiben maßgeblich.
