# AGENTS.md — Skytech EVMS

## Zweck und aktueller Umfang

Electric Vehicle Management System als geplantes Home-Assistant-Add-on:
Fahrzeuge, RFID-Zuordnung, Vermittlung von Wattbudgets zu physischen Ladepunkten,
Ladehistorie und Auswertungen mit Data Insight.

Aktuell wird das Repository samt Architektur und Verträgen vorbereitet. Es gibt
noch keinen installierbaren Dienst und keine Hardwarefreigabe. Den Umsetzungsstand
in [docs/umsetzungsplan.md](docs/umsetzungsplan.md) vor jeder Erweiterung lesen.

## Regeln

- Direkte Nutzeranweisungen haben Vorrang. Unklare Anforderungen erfragen und in
  [docs/offene-punkte.md](docs/offene-punkte.md) festhalten; keine offenen Entscheidungen still festlegen.
- Codebezeichner und Dateinamen für Code englisch; Doku, Kommentare, UI und Commits deutsch.
- Arbeitsbranch `agent/main`; nie direkt nach `main` committen oder mergen.
  Abgeschlossene Arbeitspakete committen und auf den eingerichteten Remote pushen.
  Noch nicht festgelegte Remote-Sichtbarkeit vor der Veröffentlichung klären.
- Deutsche Conventional Commits. Änderungen im selben Arbeitspaket dokumentieren.
- Verträge unter `contract/contract_<projektpaar>/` in beiden beteiligten Repos
  wortgleich führen. Status je Seite: implementiert, Entwurf oder Hardware offen.
- Genau eine HA-Schnittstellen-Entität je Einheit; Langzeitdaten nach Data Insight.
- Keine Zugangsdaten in Dateien, Logs oder HA-Entitäten. RFID-Kennungen nicht unnötig loggen.
- Menschliche Datumsangaben `TT.MM.JJJJ`, Uhrzeiten `hh:mm[:ss]`, Umrechnung nach
  `Europe/Berlin`, ohne angehängte Zeitzonenangabe. Maschinenformate dürfen abweichen.
- Geplanter Stack: Python mit aiohttp; React + TypeScript strict + Vite für Ingress.
  Vor einer UI-Implementierung Frontend- und Designregeln aus SkytechHEMS übernehmen:
  Home-Assistant-Design, sichtbarer Hell-/Dunkel-Schalter, Design-Tokens,
  keine UI-/CSS-Bibliothek oder gestaltenden Inline-Styles.
- Prüfung des aktuellen Planungsrepositories: `python3 scripts/check_contracts.py`.
  Sobald Laufzeitcode entsteht, sind Verhaltens- und Ausfalltests sowie Linting Pflicht.

## Einstieg

[Dokumentation](docs/README.md) · [Verträge](contract/README.md)
