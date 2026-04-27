"""Pytest suite for the four top-level functions of project.py.

Each test is named ``test_<function>`` to satisfy the CS50P submission rules.
Fixtures use ``tmp_path`` so the repository stays clean.
"""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from project import compute_portfolio_kpis, format_chf, load_portfolio, main


@pytest.fixture
def demo_workbook(tmp_path: Path) -> Path:
    """Generate a small portfolio workbook for round-trip tests."""
    from immoscope.sample_data import generate_portfolio
    out = tmp_path / "portfolio.xlsx"
    return generate_portfolio(out, n_buildings=3, seed=7)


@pytest.fixture
def mini_data() -> dict[str, pd.DataFrame]:
    """A hand-crafted, deterministic portfolio used for KPI assertions."""
    today = pd.Timestamp(date.today())
    immeubles = pd.DataFrame([
        {
            "building_id": "IMM-001", "name": "Test Lake", "address": "Rue 1",
            "city": "Yverdon-les-Bains", "year_built": 2000,
            "total_surface_m2": 200.0, "estimated_value_chf": 1_000_000.0,
        },
    ])
    lots = pd.DataFrame([
        {"lot_id": "LOT-001-01", "building_id": "IMM-001", "type": "appartement",
         "surface_m2": 80.0, "rooms": 3.5},
        {"lot_id": "LOT-001-02", "building_id": "IMM-001", "type": "appartement",
         "surface_m2": 60.0, "rooms": 2.5},
    ])
    baux = pd.DataFrame([
        {"lease_id": "B1", "lot_id": "LOT-001-01", "tenant_name": "A",
         "start_date": today - pd.Timedelta(days=200),
         "end_date": today + pd.Timedelta(days=200),
         "monthly_rent_chf": 2000.0, "monthly_charges_chf": 200.0, "status": "actif"},
        {"lease_id": "B2", "lot_id": "LOT-001-02", "tenant_name": "",
         "start_date": today - pd.Timedelta(days=100),
         "end_date": today - pd.Timedelta(days=100),
         "monthly_rent_chf": 1500.0, "monthly_charges_chf": 0.0, "status": "vacant"},
    ])
    transactions = pd.DataFrame([
        {"transaction_id": "T1", "lot_id": "LOT-001-01",
         "date": today - pd.Timedelta(days=30), "type": "loyer",
         "amount_chf": 2000.0, "description": "Loyer"},
        {"transaction_id": "T2", "lot_id": "LOT-001-01",
         "date": today - pd.Timedelta(days=60), "type": "entretien",
         "amount_chf": -500.0, "description": "Réparation"},
    ])
    return {"immeubles": immeubles, "lots": lots, "baux": baux, "transactions": transactions}


def test_load_portfolio(demo_workbook: Path, tmp_path: Path) -> None:
    data = load_portfolio(str(demo_workbook))
    assert set(data.keys()) == {"immeubles", "lots", "baux", "transactions"}
    assert "building_id" in data["immeubles"].columns
    assert "lot_id" in data["lots"].columns
    assert "monthly_rent_chf" in data["baux"].columns
    assert "amount_chf" in data["transactions"].columns
    assert len(data["immeubles"]) == 3

    with pytest.raises(FileNotFoundError):
        load_portfolio(str(tmp_path / "missing.xlsx"))

    bad = tmp_path / "bad.xlsx"
    pd.DataFrame({"foo": [1]}).to_excel(bad, sheet_name="WrongSheet", index=False)
    with pytest.raises(ValueError):
        load_portfolio(str(bad))


def test_compute_portfolio_kpis(mini_data: dict[str, pd.DataFrame]) -> None:
    kpis = compute_portfolio_kpis(mini_data)
    assert kpis["n_buildings"] == 1
    assert kpis["n_lots"] == 2
    assert kpis["n_active_leases"] == 1
    assert kpis["annual_revenue"] == pytest.approx(2000.0 * 12)
    assert kpis["annual_expenses"] == pytest.approx(500.0)
    assert kpis["noi"] == pytest.approx(24000.0 - 500.0)
    assert kpis["vacancy_rate"] == pytest.approx(50.0)
    assert kpis["gross_yield"] == pytest.approx(2.4, rel=0.01)
    assert "Yverdon-les-Bains" in kpis["avg_rent_per_m2_by_city"]
    assert isinstance(kpis["top_buildings"], list)
    assert "building_metrics" in kpis


def test_format_chf() -> None:
    assert format_chf(1850.0) == "1'850.00 CHF"
    assert format_chf(0) == "0.00 CHF"
    assert format_chf(-250.5) == "-250.50 CHF"
    assert format_chf(1_234_567.89) == "1'234'567.89 CHF"
    assert format_chf(999) == "999.00 CHF"
    assert format_chf(1000) == "1'000.00 CHF"
    with pytest.raises(TypeError):
        format_chf("pas un nombre")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        format_chf(None)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        format_chf(True)  # type: ignore[arg-type]


def test_main(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    target = tmp_path / "demo.xlsx"
    result = subprocess.run(
        [sys.executable, "project.py", "--generate-sample", str(target)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert target.is_file()
    assert target.stat().st_size > 5_000

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["project.py", "missing.xlsx"])
    assert main() == 1
