# Teststrategie

Aktuell prüft `python3 scripts/check_contracts.py` die Vertragskopien im gemeinsamen
Arbeitsordner. Softwaretests des HEMS liegen im HEMS-Repository.

## Vor Hardware

- Alle drei HEMS-Wege: ausschließlich Watt; normale Verbraucher bleiben unverändert.
- Fehlende, ungültige und veraltete Rückmeldungen stoppen auch unter Zwang.
- Neustart und Zuordnungswechsel entwerten alte Budgets.
- Dynamische Grenzen gelten auch bei Rampen und Totband.
- Schreibfehler und Notabschaltung veröffentlichen kein positives Budget.
- Später: EVMS-Zuordnungen, konkurrierende Scans, Puffer, Wiederholungen, DB-Ausfälle,
  Monats-/Jahresgrenzen und Zeitumstellung mit synthetischen Messwerten testen.

## Nach Lieferung der go-e

Modell, Firmware, Fahrzeug und Testdatum protokollieren. Offener Zugang,
angelernter/unbekannter Chip, wiederholter gleicher Chip, Scan vor/nach Anstecken,
Scan während des Ladens, Wallbox-/HA-/EVMS-Neustart und Netzunterbrechung prüfen.
Ein Scan darf die vom HEMS/EVMS angeforderte Ladung nicht eigenständig ändern.
Strom, Phasen, Istleistung und Zähler gegen Gerät/Referenzmessung prüfen.

Abnahme jedes Steuerungswegs einschließlich Ausfällen. Erst danach den Status
„Hardware offen“ im jeweiligen Vertrag ändern und die gemeinsame Migration freigeben.
