# Datenmodell — Entwurf

EVMS besitzt die fachliche Verwaltung; Data Insight die dauerhafte Ablage.
Geplant sind Fahrzeuge mit stabiler ID, RFID-Zuordnungen mit zeitlicher Gültigkeit,
physische Ladepunkte, Ladeziele, zeitlich begrenzte Anschlusszuordnungen,
Ladevorgänge und Energieabschnitte. Die genaue Ladeziel- und Sitzungssemantik ist offen.

Ein Name oder ein HEMS-Präfix ist keine unveränderliche Fahrzeugidentität.
Ausgemusterte Fahrzeuge werden archiviert; ihre historischen Ladevorgänge bleiben lesbar.
Korrekturen müssen nachvollziehbar sein. Messwerte, Ersatzberechnungen und Datenlücken
werden getrennt gekennzeichnet. Wallboxenergie ist nicht gleich Batteriezuwachs.

Zeitabschnitte erlauben eine Aufteilung über Tages-, Monats- und Jahresgrenzen.
Eine Sitzungssumme allein genügt dafür nicht. Wiederholte Übertragung derselben
Abschnitte darf keine Doppelzählung erzeugen.

Die Datenbankmigration und tatsächlichen Funktionssignaturen sind noch nicht implementiert.
Autoritativ ist der [Data-Insight-Vertrag](../contract/contract_evms_data_insight/contract_evms_data_insight.md).
