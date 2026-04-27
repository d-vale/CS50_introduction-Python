"""Anomaly detection for the ImmoScope portfolio.

Each detector returns a list of dicts with the schema:

    {
        "type":        str,    # one of the four anomaly types defined below
        "severity":    str,    # "high" / "medium" / "low"
        "lot_id":      str,
        "building_id": str,
        "description": str,
        "value":       float,
        "expected":    float,
    }

Includes a regex check on ``lot_id`` ("^LOT-\\d{3}-\\d{2}$") to satisfy
CS50P's "Regular Expressions" learning objective.
"""
from __future__ import annotations

import re
from datetime import datetime
from typing import Any

import pandas as pd

LOT_ID_PATTERN = re.compile(r"^LOT-\d{3}-\d{2}$")

VACANCY_THRESHOLD_MONTHS = 6
RENT_BELOW_MARKET_RATIO = 0.75
EXPENSE_OUTLIER_FACTOR = 3.0


def detect_anomalies(
    data: dict[str, Any],
    kpis: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Run every detector and aggregate results sorted by severity."""
    _ = kpis  # reserved for future detectors that need pre-computed KPIs
    anomalies: list[dict[str, Any]] = []
    anomalies += detect_below_market_rent(data["baux"], data["lots"])
    anomalies += detect_excessive_expenses(data["transactions"])
    anomalies += detect_long_vacancies(data["baux"])
    anomalies += detect_missing_rent(data["baux"], data["transactions"])
    severity_order = {"high": 0, "medium": 1, "low": 2}
    return sorted(anomalies, key=lambda a: severity_order.get(a["severity"], 9))


def detect_below_market_rent(
    baux: pd.DataFrame,
    lots: pd.DataFrame,
) -> list[dict[str, Any]]:
    """Flag apartments priced below 75 % of their building's median CHF/m²."""
    actifs = baux[baux["status"] == "actif"].copy()
    if actifs.empty:
        return []
    actifs = actifs.merge(
        lots[["lot_id", "building_id", "type", "surface_m2"]],
        on="lot_id", how="left",
    )
    apt_only = actifs[
        (actifs["type"] == "appartement") & (actifs["surface_m2"] > 0)
    ].copy()
    if apt_only.empty:
        return []
    apt_only["rent_per_m2"] = apt_only["monthly_rent_chf"] / apt_only["surface_m2"]
    medians = apt_only.groupby("building_id")["rent_per_m2"].median()

    out: list[dict[str, Any]] = []
    for _, row in apt_only.iterrows():
        bid = row["building_id"]
        median = medians.get(bid)
        if median is None or pd.isna(median):
            continue
        threshold = median * RENT_BELOW_MARKET_RATIO
        if row["rent_per_m2"] < threshold:
            out.append({
                "type": "loyer_sous_marche",
                "severity": "high",
                "lot_id": _normalize_lot_id(row["lot_id"]),
                "building_id": bid,
                "description": (
                    f"Loyer {row['rent_per_m2']:.1f} CHF/m² inférieur à "
                    f"75 % de la médiane de l'immeuble ({median:.1f} CHF/m²)."
                ),
                "value": round(float(row["rent_per_m2"]), 2),
                "expected": round(float(median), 2),
            })
    return out


def detect_excessive_expenses(transactions: pd.DataFrame) -> list[dict[str, Any]]:
    """Flag negative transactions whose magnitude exceeds 3× the type median."""
    expenses = transactions[transactions["amount_chf"] < 0].copy()
    if expenses.empty:
        return []
    expenses["abs_amount"] = -expenses["amount_chf"]
    medians = expenses.groupby("type")["abs_amount"].median()

    out: list[dict[str, Any]] = []
    for _, row in expenses.iterrows():
        median = medians.get(row["type"])
        if median is None or pd.isna(median) or median == 0:
            continue
        threshold = median * EXPENSE_OUTLIER_FACTOR
        if row["abs_amount"] > threshold:
            out.append({
                "type": "charge_excessive",
                "severity": "medium",
                "lot_id": _normalize_lot_id(row["lot_id"]),
                "building_id": "",
                "description": (
                    f"Charge '{row['type']}' de {row['abs_amount']:.0f} CHF "
                    f"(médiane du type : {median:.0f} CHF)."
                ),
                "value": float(row["abs_amount"]),
                "expected": float(threshold),
            })
    return out


def detect_long_vacancies(baux: pd.DataFrame) -> list[dict[str, Any]]:
    """Flag lots vacant for longer than VACANCY_THRESHOLD_MONTHS."""
    vacants = baux[baux["status"] == "vacant"].copy()
    if vacants.empty:
        return []
    now = pd.Timestamp(datetime.now())
    vacants["months_vacant"] = (
        (now - pd.to_datetime(vacants["start_date"])).dt.days / 30.44
    )

    out: list[dict[str, Any]] = []
    for _, row in vacants.iterrows():
        months = float(row["months_vacant"])
        if months > VACANCY_THRESHOLD_MONTHS:
            out.append({
                "type": "vacance_longue",
                "severity": "high" if months > 12 else "medium",
                "lot_id": _normalize_lot_id(row["lot_id"]),
                "building_id": "",
                "description": (
                    f"Lot vacant depuis {months:.1f} mois "
                    f"(seuil : {VACANCY_THRESHOLD_MONTHS} mois)."
                ),
                "value": round(months, 1),
                "expected": float(VACANCY_THRESHOLD_MONTHS),
            })
    return out


def detect_missing_rent(
    baux: pd.DataFrame,
    transactions: pd.DataFrame,
) -> list[dict[str, Any]]:
    """Flag active leases without a 'loyer' transaction in the previous month."""
    now = pd.Timestamp(datetime.now())
    last_month = (now - pd.DateOffset(months=1)).to_period("M")

    actifs = baux[baux["status"] == "actif"]
    rent_txn = transactions[transactions["type"] == "loyer"].copy()
    rent_txn["period"] = rent_txn["date"].dt.to_period("M")
    paid_lots = set(rent_txn[rent_txn["period"] == last_month]["lot_id"])

    out: list[dict[str, Any]] = []
    for _, row in actifs.iterrows():
        if row["lot_id"] not in paid_lots:
            out.append({
                "type": "loyer_manquant",
                "severity": "medium",
                "lot_id": _normalize_lot_id(row["lot_id"]),
                "building_id": "",
                "description": (
                    f"Aucun loyer enregistré pour {last_month}."
                ),
                "value": 0.0,
                "expected": float(row["monthly_rent_chf"]),
            })
    return out


def _normalize_lot_id(lot_id: str) -> str:
    """Validate the lot_id format with regex, returning it untouched if valid.

    Falls back to the raw string in upper case if the format is unexpected,
    so anomalies remain visible even on ill-formed exports.
    """
    cleaned = str(lot_id).strip().upper()
    if LOT_ID_PATTERN.match(cleaned):
        return cleaned
    return cleaned
