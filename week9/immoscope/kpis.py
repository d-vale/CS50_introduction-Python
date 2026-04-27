"""Portfolio-level KPI calculations.

Atomic helpers consumed by `project.compute_portfolio_kpis`. Keeping the math
in a dedicated module lets `project.py` stay focused on orchestration while
remaining testable in its own right.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

import pandas as pd

ANNUALIZATION_MONTHS = 12
LOOKBACK_MONTHS = 12


def compute_annual_revenue(baux: pd.DataFrame) -> float:
    """Sum monthly rents of active leases, annualised over 12 months."""
    actifs = baux[baux["status"] == "actif"]
    return float(actifs["monthly_rent_chf"].sum() * ANNUALIZATION_MONTHS)


def compute_annual_expenses(transactions: pd.DataFrame) -> float:
    """Sum negative transactions over the trailing 12 months (returned positive)."""
    cutoff = pd.Timestamp(datetime.now()) - pd.DateOffset(months=LOOKBACK_MONTHS)
    recent = transactions[
        (transactions["date"] >= cutoff) & (transactions["amount_chf"] < 0)
    ]
    return float(-recent["amount_chf"].sum())


def compute_total_value(immeubles: pd.DataFrame) -> float:
    """Sum estimated values of all buildings."""
    return float(immeubles["estimated_value_chf"].sum())


def compute_vacancy_rate(baux: pd.DataFrame) -> float:
    """Percentage of leases marked 'vacant'."""
    if baux.empty:
        return 0.0
    vacant = (baux["status"] == "vacant").sum()
    return float(vacant / len(baux) * 100)


def compute_avg_rent_per_m2_by_city(
    baux: pd.DataFrame,
    lots: pd.DataFrame,
    immeubles: pd.DataFrame,
) -> dict[str, float]:
    """Average monthly rent per m² grouped by city, only for active leases."""
    actifs = baux[baux["status"] == "actif"]
    merged = actifs.merge(lots[["lot_id", "building_id", "surface_m2"]], on="lot_id")
    merged = merged.merge(immeubles[["building_id", "city"]], on="building_id")
    merged = merged[merged["surface_m2"] > 0]
    merged["rent_per_m2"] = merged["monthly_rent_chf"] / merged["surface_m2"]
    grouped = merged.groupby("city")["rent_per_m2"].mean()
    return {city: round(float(val), 2) for city, val in grouped.items()}


def compute_building_metrics(
    immeubles: pd.DataFrame,
    lots: pd.DataFrame,
    baux: pd.DataFrame,
    transactions: pd.DataFrame,
) -> pd.DataFrame:
    """Per-building NOI, gross yield, vacancy rate."""
    cutoff = pd.Timestamp(datetime.now()) - pd.DateOffset(months=LOOKBACK_MONTHS)
    recent = transactions[transactions["date"] >= cutoff]
    lots_with_building = lots[["lot_id", "building_id"]]
    recent = recent.merge(lots_with_building, on="lot_id", how="left")

    rows: list[dict[str, Any]] = []
    for _, b in immeubles.iterrows():
        b_lots = lots[lots["building_id"] == b["building_id"]]
        b_lot_ids = set(b_lots["lot_id"])
        b_baux = baux[baux["lot_id"].isin(b_lot_ids)]
        actifs = b_baux[b_baux["status"] == "actif"]
        revenue = float(actifs["monthly_rent_chf"].sum() * ANNUALIZATION_MONTHS)
        b_txn = recent[recent["building_id"] == b["building_id"]]
        expenses = float(-b_txn[b_txn["amount_chf"] < 0]["amount_chf"].sum())
        noi = revenue - expenses
        vacancy = (
            (b_baux["status"] == "vacant").sum() / len(b_baux) * 100
            if len(b_baux) > 0 else 0.0
        )
        gross_yield = (
            revenue / b["estimated_value_chf"] * 100
            if b["estimated_value_chf"] > 0 else 0.0
        )
        net_yield = (
            noi / b["estimated_value_chf"] * 100
            if b["estimated_value_chf"] > 0 else 0.0
        )
        rows.append({
            "building_id": b["building_id"],
            "name": b["name"],
            "city": b["city"],
            "annual_revenue": round(revenue, 2),
            "annual_expenses": round(expenses, 2),
            "noi": round(noi, 2),
            "gross_yield": round(gross_yield, 2),
            "net_yield": round(net_yield, 2),
            "vacancy_rate": round(float(vacancy), 2),
        })
    return pd.DataFrame(rows)


def top_buildings_by_noi(building_metrics: pd.DataFrame, n: int = 3) -> list[dict[str, Any]]:
    """Top N buildings sorted by NOI descending."""
    return building_metrics.sort_values("noi", ascending=False).head(n).to_dict("records")


def bottom_buildings_by_yield(
    building_metrics: pd.DataFrame, n: int = 3,
) -> list[dict[str, Any]]:
    """Bottom N buildings sorted by net yield ascending."""
    return building_metrics.sort_values("net_yield", ascending=True).head(n).to_dict("records")


def monthly_cashflow(transactions: pd.DataFrame, months: int = 24) -> pd.DataFrame:
    """Net cash flow per month over the trailing N months."""
    cutoff = pd.Timestamp(datetime.now()) - pd.DateOffset(months=months)
    recent = transactions[transactions["date"] >= cutoff].copy()
    recent["month"] = recent["date"].dt.to_period("M").dt.to_timestamp()
    grouped = recent.groupby("month")["amount_chf"].sum().reset_index()
    grouped.columns = ["month", "net_cashflow"]
    return grouped


def expenses_by_type(transactions: pd.DataFrame) -> dict[str, float]:
    """Total expenses (positive values) grouped by transaction type."""
    cutoff = pd.Timestamp(datetime.now()) - pd.DateOffset(months=LOOKBACK_MONTHS)
    recent = transactions[
        (transactions["date"] >= cutoff) & (transactions["amount_chf"] < 0)
    ]
    grouped = recent.groupby("type")["amount_chf"].sum()
    return {t: float(-amt) for t, amt in grouped.items()}
