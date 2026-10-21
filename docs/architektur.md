# Architektur

**Stand: 21.10.2026. Zielbild; EVMS-Laufzeit noch nicht implementiert.**

```text
HEMS ── Wattbudget ──► EVMS ── zugeordnetes Wattbudget ──► Wallbox-Provider ──► Wallbox
HEMS ◄── Rückmeldung ─ EVMS ◄── Messung / Grenzen / RFID ─ Wallbox-Provider
                      │
                      └── Fahrzeuge / Zuordnungen / Ladehistorie ──► Data Insight
```

Alternativen: HEMS → Wallbox-Provider und HEMS → eigene HA-Automation.
HEMS regelt Überschuss und Prioritäten. EVMS besitzt Fahrzeugidentitäten und
Zuordnungen. Der Provider besitzt die technischen Ladeabläufe und Herstellerprotokolle.
Eine HA-Automation übernimmt bei direkter Eigenanbindung dieselben Pflichten wie der Provider.
Der Battery-Provider bleibt für stationäre Speicher zuständig.

## Ladeziele

Der HEMS-Verteiler sieht einen regelbaren Verbraucher in Watt. Noch offen ist,
ob ein EVMS-Ladeziel dauerhaft je Fahrzeug oder nach einem anderen Modell existiert.
Eine stabile HEMS-ID ist von Fahrzeug-ID, physischem Anschluss und laufender
Zuordnung getrennt. Konfiguration und automatische Discovery werden erst nach
Entscheidung des Nutzers umgesetzt.

## Zustände und Ausfälle

Die neue HEMS-Seite erwartet vollständige, regelmäßig erneuerte Rückmeldungen.
Ist kein bekanntes Fahrzeug zugeordnet, veröffentlicht EVMS keine positive Freigabe.
Ladepausen, Verbindungsverlust und tatsächliches Abstecken sind getrennte Zustände.
Ein Messausfall beendet nicht automatisch einen Ladevorgang.

Für jeden Anschluss ist exakt ein Steuerungsweg konfiguriert. Kein automatischer
Wechsel von EVMS auf direkte HEMS-Steuerung bei einem Ausfall. Eine neue Zuordnung
entwertet alte Budgets; der Empfänger akzeptiert positive Vorgaben erst mit passender
Zuordnungskennung und frischem HEMS-Commit.

Data Insight liegt außerhalb der Regelkette. Ein dauerhafter lokaler Puffer für
Konfiguration, laufende Sitzungen und noch nicht bestätigte Übertragungen ist empfohlen,
seine konkrete Ausführung und Grenzen sind vor der Implementierung zu entscheiden.
Ohne nachweisbar gültige Zuordnung wird nach einem Neustart keine Ladung freigegeben.

## Gegenstellen ohne zusätzliche Direktverbindung

Energy Pilot bleibt strategischer Planer über HEMS. Ladeziele und Abfahrtszeiten sind
noch nicht Teil des beschlossenen Erstumfangs; kein neuer direkter EVMS–EP-Vertrag.
Powerflow-Card liest weiter HEMS-Anzeigedaten. OmniAI hat keine Rolle im Echtzeit-Regelweg.
