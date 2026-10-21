# Offene Punkte

**Stand: 21.10.2026. Keine offene Frage gilt als stillschweigend entschieden.**

## Bereits entschieden

- Name Skytech EVMS; eigenes HA-Add-on als Ziel.
- HEMS gibt für die neuen Wallbox-Wege Wattbudgets aus.
- Drei Wege: über EVMS, direkt zum Wallbox-Provider, eigene HA-Automation.
- Fahrzeug-ID bevorzugt, falls ein Gerät sie tatsächlich liefert; RFID als akzeptierte
  Alternative, sofern extern auswertbar ohne go-e-Zugangsbeschränkung.
- Vorerst kein Betrieb als „unbekanntes Fahrzeug“.
- Langzeitablage mit Data Insight.
- go-e noch nicht geliefert; Modell und Firmware sind nicht bekannt.

## Fachliche Entscheidungen vor EVMS-Implementierung

| ID | Frage | Blockiert |
|---|---|---|
| F-01 | Dauerhaft ein Ladeziel je Fahrzeug oder ein anderes Modell? Wie werden Ziele in HEMS angelegt? | Fahrzeug-/Zielverwaltung |
| F-02 | Scan vor/nach Einstecken: Zuordnungsfenster, verspäteter Scan, widersprüchliche Karten, manuelle Korrektur? | RFID-Zustandsautomat |
| F-03 | Welche Fahrzeugdaten und Grenzen, wie viele Fahrzeuge und Anschlüsse? | Konfiguration |
| F-04 | Sitzung von Anstecken bis Abstecken mit Ladephasen darin? | Sitzungsmodell |
| F-05 | Auswertung nur Wallboxenergie oder auch Batterieenergie, PV/Netz/Speicher, Kosten? Welche Bilanzierungsregel? | Auswertung |
| F-06 | Öffentliche Ladungen, Gastfahrzeuge und Importe später erforderlich? | Erweiterungen |
| F-07 | Auswertungen direkt im EVMS, Grafana ergänzend? | Oberfläche |
| F-08 | Ladeziele/Abfahrtszeiten bereits im Erstumfang? Wie werden sie Energy Pilot zugänglich? | Planungserweiterung |
| F-09 | Konfiguration dauerhaft in Data Insight, lokaler Betriebsstand/Puffer: Speichergrenze und Wiederanlauf? | Persistenz |
| F-10 | Gemeinsame Anschluss-/Phasenlimits mehrerer Ladepunkte und Zuständigkeit dafür? | Mehrfachbetrieb |
| F-11 | Prüfzeiten und Start-/Stopp-/Phasenwechselstrategie passend zu Fahrzeug und Wallbox? | Provider |

## Hardwareabhängige Fragen

- Exaktes Modell und Firmware erst nach Lieferung erfassen.
- Erkennt der offene Modus bekannte UND nicht angelernte RFID-Chips ohne Lade-Nebenwirkung?
- Ist ein erneuter Scan derselben Karte zuverlässig erkennbar, auch über Neustarts?
- Reicht Modbus oder ist ergänzend die lokale API für Scan-Zeitpunkt/Ereignis nötig?
- Welche Freigaben sind für die Ausgabe der Kennung erforderlich, und welche weiteren
  Ausgabekanäle werden dadurch aktiviert?
- Zählerauflösung, Reset beim Anstecken, Neustarts, Energie in Ladepausen prüfen.
- Wattbudget → Strom/Phasen: echte Leistungsaufnahme, Mindeststrom, Umschaltzeiten,
  Watchdogs und Wiederanlauf mit Fahrzeug prüfen.
