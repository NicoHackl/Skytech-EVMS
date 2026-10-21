# Skytech EVMS

**Electric Vehicle Management System** — geplantes Home-Assistant-Add-on für
Fahrzeugverwaltung, RFID-Zuordnung, Ladevermittlung und Ladeauswertungen.

**Stand 21.10.2026: Repository und Schnittstellenplanung vorbereitet. Noch kein
installierbares Add-on.** Die erste go-e-Wallbox ist noch nicht geliefert;
Gerätetyp, Firmware, RFID-Verhalten und technische Ladeumsetzung sind offen.

## Zielbild

- HEMS verteilt ein Leistungsbudget in Watt je Ladeziel.
- EVMS ordnet ein bekanntes Fahrzeug einem physischen Ladepunkt zu und vermittelt
  dessen Budget. Die Bedeutung eines Ladeziels (je Auto oder anders) ist noch offen.
- Der Wallbox-Provider übernimmt Gerätekommunikation und die technische Umsetzung
  des Wattbudgets in Strom, Phasen und Freigabe.
- Data Insight speichert Fahrzeuge, Zuordnungen und Ladehistorie langfristig.
- RFID dient der externen Zuordnung. Die go-e soll dafür keine eigene
  RFID-Zugangsbeschränkung benötigen; diese Eigenschaft ist noch zu prüfen.
- Ein Betrieb mit „unbekanntem Fahrzeug“ gehört vorerst nicht zum Umfang.

HEMS bleibt alternativ direkt mit dem Wallbox-Provider oder einer eigenen
HA-Automation nutzbar. Pro physischem Anschluss gibt es genau einen Befehlsgeber.

[Umsetzungsplan](docs/umsetzungsplan.md) · [Offene Entscheidungen](docs/offene-punkte.md) ·
[Verträge](contract/README.md) · [Projektregeln](AGENTS.md)
