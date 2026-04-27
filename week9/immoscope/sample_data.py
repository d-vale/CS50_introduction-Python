"""Realistic Swiss real estate portfolio generator.

Produces a multi-sheet Excel file modeled on the Quorum ERP export format
used by Bobst Régie Immobilière. Includes 4 deliberately-planted anomalies
so the detection module always finds something on the demo file.
"""
from __future__ import annotations

import random
from datetime import date
from pathlib import Path
from typing import Any

import pandas as pd
from faker import Faker

CITIES = {
    "Yverdon-les-Bains": {"rent_per_m2": 25.0, "price_per_m2": 7000.0, "weight": 4},
    "Lausanne": {"rent_per_m2": 32.0, "price_per_m2": 11000.0, "weight": 3},
    "Genève": {"rent_per_m2": 40.0, "price_per_m2": 14000.0, "weight": 1},
}
LOT_TYPES = ["appartement", "appartement", "appartement", "commercial", "parking"]
TRANSACTION_EXPENSES = ["entretien", "assurance", "taxe", "charges"]
OCCUPANCY_RATE = 0.85


def generate_portfolio(
    filepath: str | Path,
    n_buildings: int = 8,
    seed: int = 42,
) -> Path:
    """Generate a realistic Swiss real estate portfolio Excel file.

    Args:
        filepath: Destination path for the .xlsx file.
        n_buildings: Number of buildings (default 8).
        seed: RNG seed for reproducibility.

    Returns:
        The Path to the generated file.
    """
    rng = random.Random(seed)
    fake = Faker("fr_CH")
    Faker.seed(seed)

    immeubles = _generate_buildings(rng, fake, n_buildings)
    lots = _generate_lots(rng, immeubles)
    baux = _generate_leases(rng, fake, lots, immeubles)
    transactions = _generate_transactions(rng, baux, lots)

    _plant_anomalies(rng, baux, lots, transactions)

    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(filepath, engine="openpyxl") as writer:
        pd.DataFrame(immeubles).to_excel(writer, sheet_name="Immeubles", index=False)
        pd.DataFrame(lots).to_excel(writer, sheet_name="Lots", index=False)
        pd.DataFrame(baux).to_excel(writer, sheet_name="Baux", index=False)
        pd.DataFrame(transactions).to_excel(writer, sheet_name="Transactions", index=False)
    return filepath


def _generate_buildings(rng: random.Random, fake: Faker, n: int) -> list[dict[str, Any]]:
    cities = list(CITIES.keys())
    weights = [CITIES[c]["weight"] for c in cities]
    buildings = []
    for i in range(1, n + 1):
        city = rng.choices(cities, weights=weights, k=1)[0]
        surface = round(rng.uniform(700, 2400), 1)
        price_per_m2 = CITIES[city]["price_per_m2"] * rng.uniform(0.85, 1.15)
        buildings.append({
            "building_id": f"IMM-{i:03d}",
            "name": f"Résidence {fake.last_name()}",
            "address": fake.street_address(),
            "city": city,
            "year_built": rng.randint(1955, 2018),
            "total_surface_m2": surface,
            "estimated_value_chf": round(surface * price_per_m2, 2),
        })
    return buildings


def _generate_lots(
    rng: random.Random,
    buildings: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    lots = []
    for b in buildings:
        n_lots = rng.randint(6, 20)
        remaining_surface = b["total_surface_m2"]
        for j in range(1, n_lots + 1):
            lot_type = rng.choices(LOT_TYPES, k=1)[0]
            if lot_type == "parking":
                surface = round(rng.uniform(12, 18), 1)
                rooms: float | None = None
            elif lot_type == "commercial":
                surface = round(rng.uniform(40, 180), 1)
                rooms = None
            else:
                surface = round(rng.uniform(35, 140), 1)
                rooms = rng.choice([1.5, 2.5, 3.0, 3.5, 4.5, 5.5])
            surface = min(surface, max(remaining_surface * 0.8, 12))
            remaining_surface = max(remaining_surface - surface, 0)
            lots.append({
                "lot_id": f"LOT-{int(b['building_id'].split('-')[1]):03d}-{j:02d}",
                "building_id": b["building_id"],
                "type": lot_type,
                "surface_m2": round(surface, 1),
                "rooms": rooms,
            })
    return lots


def _generate_leases(
    rng: random.Random,
    fake: Faker,
    lots: list[dict[str, Any]],
    buildings: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_building = {b["building_id"]: b for b in buildings}
    baux = []
    today = date.today()
    lease_counter = 1
    for lot in lots:
        is_occupied = rng.random() < OCCUPANCY_RATE
        building = by_building[lot["building_id"]]
        rent_per_m2 = CITIES[building["city"]]["rent_per_m2"]
        if lot["type"] == "parking":
            monthly_rent = round(rng.uniform(120, 220), 2)
            charges = 0.0
        else:
            multiplier = rng.uniform(0.92, 1.10)
            monthly_rent = round(lot["surface_m2"] * rent_per_m2 * multiplier, 2)
            charges = round(monthly_rent * rng.uniform(0.08, 0.18), 2)
        if is_occupied:
            start_offset_months = rng.randint(2, 30)
            start = _add_months(today, -start_offset_months)
            if rng.random() < 0.4:
                end = None
            else:
                end = _add_months(start, rng.choice([24, 36, 48]))
                if end <= today:
                    end = _add_months(today, rng.randint(3, 24))
            baux.append({
                "lease_id": f"BAIL-{start.year}-{lease_counter:04d}",
                "lot_id": lot["lot_id"],
                "tenant_name": fake.name(),
                "start_date": start,
                "end_date": end,
                "monthly_rent_chf": monthly_rent,
                "monthly_charges_chf": charges,
                "status": "actif",
            })
            lease_counter += 1
        else:
            vacant_since = rng.randint(1, 5)
            baux.append({
                "lease_id": f"VAC-{lot['lot_id']}",
                "lot_id": lot["lot_id"],
                "tenant_name": "",
                "start_date": _add_months(today, -vacant_since),
                "end_date": _add_months(today, -vacant_since),
                "monthly_rent_chf": monthly_rent,
                "monthly_charges_chf": 0.0,
                "status": "vacant",
            })
    return baux


def _generate_transactions(
    rng: random.Random,
    baux: list[dict[str, Any]],
    lots: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    transactions = []
    txn_id = 1
    today = date.today()
    months = [_add_months(today, -i) for i in range(24, 0, -1)]
    by_lot = {lot["lot_id"]: lot for lot in lots}
    active_baux = [b for b in baux if b["status"] == "actif"]

    for bail in active_baux:
        start_period = (bail["start_date"].year, bail["start_date"].month)
        end_period = (
            (bail["end_date"].year, bail["end_date"].month)
            if bail["end_date"] is not None else None
        )
        for month in months:
            month_period = (month.year, month.month)
            if month_period >= start_period and (
                end_period is None or month_period <= end_period
            ):
                transactions.append({
                    "transaction_id": f"TXN-{month.year}-{txn_id:06d}",
                    "lot_id": bail["lot_id"],
                    "date": month,
                    "type": "loyer",
                    "amount_chf": bail["monthly_rent_chf"],
                    "description": f"Loyer {month.strftime('%B %Y').lower()}",
                })
                txn_id += 1
                if bail["monthly_charges_chf"] > 0:
                    transactions.append({
                        "transaction_id": f"TXN-{month.year}-{txn_id:06d}",
                        "lot_id": bail["lot_id"],
                        "date": month,
                        "type": "charges",
                        "amount_chf": bail["monthly_charges_chf"],
                        "description": f"Charges {month.strftime('%B %Y').lower()}",
                    })
                    txn_id += 1

    for lot in lots:
        for month in months:
            if rng.random() < 0.06:
                expense_type = rng.choices(TRANSACTION_EXPENSES, k=1)[0]
                amount = -round(rng.uniform(80, 800), 2)
                transactions.append({
                    "transaction_id": f"TXN-{month.year}-{txn_id:06d}",
                    "lot_id": lot["lot_id"],
                    "date": month,
                    "type": expense_type,
                    "amount_chf": amount,
                    "description": f"{expense_type.capitalize()} {month.strftime('%m/%Y')}",
                })
                txn_id += 1

    return transactions


def _plant_anomalies(
    rng: random.Random,
    baux: list[dict[str, Any]],
    lots: list[dict[str, Any]],
    transactions: list[dict[str, Any]],
) -> None:
    """Inject 4 deliberate anomalies so detection always finds something."""
    today = date.today()

    apt_baux = [
        b for b in baux
        if b["status"] == "actif"
        and any(lot["type"] == "appartement" and lot["lot_id"] == b["lot_id"] for lot in lots)
    ]
    if apt_baux:
        target = apt_baux[0]
        target["monthly_rent_chf"] = round(target["monthly_rent_chf"] * 0.65, 2)
        for txn in transactions:
            if txn["lot_id"] == target["lot_id"] and txn["type"] == "loyer":
                txn["amount_chf"] = target["monthly_rent_chf"]

    if lots:
        target_lot = lots[0]
        transactions.append({
            "transaction_id": "TXN-ANOM-EXPENSE",
            "lot_id": target_lot["lot_id"],
            "date": _add_months(today, -2),
            "type": "entretien",
            "amount_chf": -8500.0,
            "description": "Réfection toiture (anomalie démo)",
        })

    vacant_baux = [b for b in baux if b["status"] == "vacant"]
    if vacant_baux:
        vacant_baux[0]["start_date"] = _add_months(today, -10)
        vacant_baux[0]["end_date"] = _add_months(today, -10)

    last_month = _add_months(today, -1)
    if len(apt_baux) > 1:
        target_id = apt_baux[1]["lot_id"]
        before = len(transactions)
        transactions[:] = [
            t for t in transactions
            if not (
                t["lot_id"] == target_id
                and t["type"] == "loyer"
                and t["date"].year == last_month.year
                and t["date"].month == last_month.month
            )
        ]
        _ = before


def _add_months(d: date, months: int) -> date:
    """Add (or subtract) months to a date, clamping the day to month end."""
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    day = min(d.day, _last_day_of_month(year, month))
    return date(year, month, day)


def _last_day_of_month(year: int, month: int) -> int:
    if month == 12:
        return 31
    next_month = date(year, month + 1, 1)
    last = next_month.toordinal() - 1
    return date.fromordinal(last).day
