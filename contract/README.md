# Projektübergreifende Verträge

Jedes Paar hat `contract/contract_<projektpaar>/`; identische Dateien liegen in beiden
Repositories am selben relativen Pfad. Schnittstellenänderungen ziehen beide Seiten,
Doku und Changelog im selben Arbeitspaket nach. Eine Doku implementiert keine Schnittstelle.

Genau eine HA-Schnittstellen-Entität je Einheit: `sensor.evms_schnittstelle`,
`sensor.hems_schnittstelle`, `sensor.wallbox_provider_schnittstelle`.
Sollwerte und Bestätigung gemäß Watt-Ladeprotokoll; DB-Austausch mit Data Insight ist
eine ausdrückliche Ausnahme. HEMS behält den bestehenden Speicher-State; Ladeziele
stehen additiv im Attribut `ladeziele`.

| Paar | Vertrag | Status |
|---|---|---|
| HEMS ↔ EVMS | [Vertrag](contract_hems_evms/contract_hems_evms.md), [Watt-Protokoll](contract_hems_evms/charging_protocol.md) | HEMS implementiert, EVMS Entwurf |
| EVMS ↔ Wallbox-Provider | [Vertrag](contract_evms_wallbox_provider/contract_evms_wallbox_provider.md) | Entwurf, Hardware offen |
| EVMS ↔ Data Insight | [Vertrag](contract_evms_data_insight/contract_evms_data_insight.md) | Entwurf, keine DB-Migration |

Es gibt noch keinen direkten EVMS-Vertrag mit Energy Pilot, Battery-Provider,
Powerflow-Card oder OmniAI. Zusätzliche Paarungen erst bei einer tatsächlichen Schnittstelle.
