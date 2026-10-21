"""Prüft alle betroffenen Vertragskopien im gemeinsamen Skytech-Arbeitsordner."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAIRS = [
    ('SkytechHEMS', 'Skytech-EVMS', 'contract_hems_evms'),
    ('SkytechHEMS', 'Skytech-HEMS-Wallbox-Provider', 'contract_hems_wallbox_provider'),
    ('Skytech-EVMS', 'Skytech-HEMS-Wallbox-Provider', 'contract_evms_wallbox_provider'),
    ('Skytech-EVMS', 'Skytech-Data-Insight', 'contract_evms_data_insight'),
    ('SkytechHEMS', 'Skytech-Data-Insight', 'contract_hems_data_insight'),
    ('SkytechHEMS', 'Skytech-HEMS-Battery-Provider', 'contract_hems_battery_provider'),
    ('SkytechHEMS', 'Skytech-Energy-Pilot', 'contract_hems_energy_pilot'),
    ('SkytechHEMS', 'Skytech-Powerflow-Card', 'contract_powerflow_card_hems'),
]


def main() -> int:
    errors = []
    checked = 0
    for left, right, folder in PAIRS:
        a, b = (ROOT / repo / 'contract' / folder for repo in (left, right))
        if not a.is_dir() or not b.is_dir():
            errors.append(f'Gegenstelle fehlt: {left} / {right} / {folder}')
            continue
        paths = {p.relative_to(a) for p in a.rglob('*') if p.is_file()}
        paths |= {p.relative_to(b) for p in b.rglob('*') if p.is_file()}
        for rel in sorted(paths):
            if not (a / rel).is_file() or not (b / rel).is_file():
                errors.append(f'Vertragskopie fehlt: {folder}/{rel}')
            elif (a / rel).read_bytes() != (b / rel).read_bytes():
                errors.append(f'Vertragskopien verschieden: {folder}/{rel}')
            else:
                checked += 1
    reference = ROOT / 'SkytechHEMS/contract/contract_hems_evms/charging_protocol.md'
    for repo, folder in [
        ('SkytechHEMS', 'contract_hems_automation'),
        ('SkytechHEMS', 'contract_hems_wallbox_provider'),
    ]:
        other = ROOT / repo / 'contract' / folder / 'charging_protocol.md'
        if not other.is_file() or other.read_bytes() != reference.read_bytes():
            errors.append(f'Watt-Protokoll weicht ab: {repo}/{folder}')
    for error in errors:
        print(error)
    print(f'{checked} Vertragsdateien wortgleich; {len(errors)} Fehler.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
