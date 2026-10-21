# Umsetzungsplan

**Beschluss des Nutzers: 21.10.2026.** Jetzt Repository, HEMS-Vorbereitung und
Verträge/Dokumentation; finale Implementierung und Hardwaretests nach Lieferung der go-e.

| Phase | Inhalt | Stand |
|---|---|---|
| P0 | Repository, Rollen, offene Entscheidungen und Vertragsentwürfe | Vorbereitet |
| P1 | HEMS: drei explizite Watt-Anbindungen, Rückmeldungen, Ausfallverhalten, Tests und Formular | Implementiert und softwaregeprüft; siehe Prüfstand |
| P2 | RFID und Watt-Ansteuerung am konkreten go-e-Modell untersuchen | Wartet auf Hardware |
| P3 | Ladezielmodell und offene Fachfragen entscheiden | Offen, Nutzerentscheidung |
| P4 | Provider: Watt-Umsetzung, Phasenwechsel, Quellenauswahl, RFID-Scan-Erkennung | Entwurf, noch nicht implementiert |
| P5 | EVMS: Add-on, Ingress, Fahrzeugverwaltung, Zuordnung, Routing und Wiederanlauf | Entwurf, noch nicht implementiert |
| P6 | Data Insight: Rolle, Migrationen, Schreibfunktionen, Leseansichten; EVMS-Puffer | Entwurf, noch nicht implementiert |
| P7 | Ladehistorie und Auswertungen, Monats-/Jahresgrenzen | Entwurf, Umfang noch abzustimmen |
| P8 | Gemeinsame Hardwareabnahme, Migrationsanleitung und koordinierte Freigabe | Wartet auf P2–P7 |

## Abnahme vor Freigabe

Alle drei Wege separat prüfen. Bestandsanlagen bleiben bis zur bewussten Migration
auf ihrem bisherigen Weg. Das HEMS allein macht aus dem bisherigen Ampere-Provider
keinen Watt-Empfänger. Fehlende neue Rückmeldung blockiert die neue HEMS-Anbindung.

Die HEMS-Schnittstelle zur Freigabe des neuen Budgets wird mit Mock-Gegenstellen
getestet. Das bestätigt weder die reale Phasenumschaltung noch RFID oder Energiezähler.
Jedes Projekt pflegt seinen tatsächlichen Status im jeweiligen Vertrag.
