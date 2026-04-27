"""Excel parsing helpers for ImmoScope.

The public entry point lives in `project.load_portfolio`; this module
centralises the schema definition and validation logic so it stays out of the
top-level CS50P file.
"""
from __future__ import annotations

import pandas as pd

EXPECTED_SCHEMA: dict[str, list[str]] = {
    "Immeubles": [
        "building_id", "name", "address", "city",
        "year_built", "total_surface_m2", "estimated_value_chf",
    ],
    "Lots": ["lot_id", "building_id", "type", "surface_m2", "rooms"],
    "Baux": [
        "lease_id", "lot_id", "tenant_name", "start_date", "end_date",
        "monthly_rent_chf", "monthly_charges_chf", "status",
    ],
    "Transactions": [
        "transaction_id", "lot_id", "date", "type", "amount_chf", "description",
    ],
}

DATE_COLUMNS: dict[str, list[str]] = {
    "Baux": ["start_date", "end_date"],
    "Transactions": ["date"],
}


def read_workbook(filepath: str) -> dict[str, pd.DataFrame]:
    """Read all required sheets from an Excel workbook.

    Args:
        filepath: Path to the .xlsx file.

    Returns:
        Mapping of sheet-key (lowercased French label) to DataFrame.

    Raises:
        ValueError: If a required sheet or column is missing.
    """
    xls = pd.ExcelFile(filepath)
    missing_sheets = [s for s in EXPECTED_SCHEMA if s not in xls.sheet_names]
    if missing_sheets:
        raise ValueError(
            f"Feuilles manquantes dans le fichier Excel : {', '.join(missing_sheets)}"
        )

    out: dict[str, pd.DataFrame] = {}
    for sheet, expected_cols in EXPECTED_SCHEMA.items():
        df = pd.read_excel(filepath, sheet_name=sheet)
        missing_cols = [c for c in expected_cols if c not in df.columns]
        if missing_cols:
            raise ValueError(
                f"Colonnes manquantes dans la feuille '{sheet}' : {', '.join(missing_cols)}"
            )
        for col in DATE_COLUMNS.get(sheet, []):
            df[col] = pd.to_datetime(df[col], errors="coerce")
        out[_french_key(sheet)] = df
    return out


def _french_key(sheet_name: str) -> str:
    """Return the canonical lowercase key used in the load_portfolio dict."""
    return {
        "Immeubles": "immeubles",
        "Lots": "lots",
        "Baux": "baux",
        "Transactions": "transactions",
    }[sheet_name]
