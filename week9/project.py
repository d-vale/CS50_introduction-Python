"""ImmoScope — CS50P final project.

Real-estate portfolio analyser modelled after the Quorum ERP exports used by
Bobst Régie Immobilière (Yverdon-les-Bains, Suisse). Reads a multi-sheet Excel
file, computes business KPIs, surfaces anomalies, and renders both a terminal
dashboard (rich) and a printable PDF report (reportlab).

Top-level functions (CS50P requirement — at least three plus `main`):
    - load_portfolio:           Excel ingestion + schema validation.
    - compute_portfolio_kpis:   Headline financial KPIs for the whole portfolio.
    - format_chf:               Swiss-formatted currency strings (``1'850.00 CHF``).
    - main:                     CLI entry-point.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from numbers import Real
from pathlib import Path
from typing import Any

from rich.console import Console

from immoscope import kpis as kpi_module
from immoscope import loader

console = Console()
err_console = Console(stderr=True, style="bold red")


def load_portfolio(filepath: str) -> dict[str, Any]:
    """Load a Quorum-style portfolio workbook from disk.

    Args:
        filepath: Path to the .xlsx export.

    Returns:
        Dict with four pandas DataFrames keyed by:
        ``immeubles``, ``lots``, ``baux``, ``transactions``.

    Raises:
        FileNotFoundError: If ``filepath`` does not exist.
        ValueError: If a required sheet or column is missing.
    """
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"Fichier introuvable : {filepath}")
    return loader.read_workbook(str(path))


def compute_portfolio_kpis(data: dict[str, Any]) -> dict[str, Any]:
    """Aggregate the headline KPIs that drive both the dashboard and the PDF.

    Args:
        data: The dict returned by :func:`load_portfolio`.

    Returns:
        Dict with keys: ``annual_revenue``, ``annual_expenses``, ``noi``,
        ``gross_yield``, ``net_yield``, ``vacancy_rate``,
        ``avg_rent_per_m2_by_city``, ``top_buildings``, ``bottom_buildings``,
        ``building_metrics``, ``monthly_cashflow``, ``expenses_by_type``.
    """
    immeubles = data["immeubles"]
    lots = data["lots"]
    baux = data["baux"]
    transactions = data["transactions"]

    revenue = kpi_module.compute_annual_revenue(baux)
    expenses = kpi_module.compute_annual_expenses(transactions)
    noi = revenue - expenses
    total_value = kpi_module.compute_total_value(immeubles)
    gross_yield = (revenue / total_value * 100) if total_value > 0 else 0.0
    net_yield = (noi / total_value * 100) if total_value > 0 else 0.0
    vacancy = kpi_module.compute_vacancy_rate(baux)
    rent_by_city = kpi_module.compute_avg_rent_per_m2_by_city(baux, lots, immeubles)
    bm = kpi_module.compute_building_metrics(immeubles, lots, baux, transactions)

    return {
        "annual_revenue": round(revenue, 2),
        "annual_expenses": round(expenses, 2),
        "noi": round(noi, 2),
        "gross_yield": round(gross_yield, 2),
        "net_yield": round(net_yield, 2),
        "vacancy_rate": round(vacancy, 2),
        "total_value": round(total_value, 2),
        "n_buildings": int(len(immeubles)),
        "n_lots": int(len(lots)),
        "n_active_leases": int((baux["status"] == "actif").sum()),
        "avg_rent_per_m2_by_city": rent_by_city,
        "building_metrics": bm,
        "top_buildings": kpi_module.top_buildings_by_noi(bm, n=3),
        "bottom_buildings": kpi_module.bottom_buildings_by_yield(bm, n=3),
        "monthly_cashflow": kpi_module.monthly_cashflow(transactions, months=24),
        "expenses_by_type": kpi_module.expenses_by_type(transactions),
    }


def format_chf(amount: float) -> str:
    """Format a number as a Swiss-style CHF amount (apostrophe thousands).

    Examples:
        >>> format_chf(1850.0)
        "1'850.00 CHF"
        >>> format_chf(-250.5)
        "-250.50 CHF"

    Args:
        amount: Numeric value (int or float).

    Returns:
        The formatted string with apostrophe thousands separators.

    Raises:
        TypeError: If ``amount`` is not a real number.
    """
    if isinstance(amount, bool) or not isinstance(amount, Real):
        raise TypeError(f"format_chf attend un nombre, reçu {type(amount).__name__}")
    sign = "-" if amount < 0 else ""
    abs_amount = abs(float(amount))
    integer_part, decimal_part = f"{abs_amount:,.2f}".split(".")
    integer_with_apostrophes = integer_part.replace(",", "'")
    return f"{sign}{integer_with_apostrophes}.{decimal_part} CHF"


def main() -> int:
    """CLI entry-point. Returns the process exit code."""
    parser = argparse.ArgumentParser(
        prog="project.py",
        description=(
            "ImmoScope — analyse de portefeuille immobilier "
            "(format Quorum ERP simplifié)."
        ),
    )
    parser.add_argument(
        "filepath", nargs="?",
        help="Chemin vers le fichier Excel du portefeuille (.xlsx).",
    )
    parser.add_argument(
        "--generate-sample", metavar="PATH",
        help="Génère un portefeuille de démonstration au chemin indiqué.",
    )
    parser.add_argument(
        "--no-pdf", action="store_true",
        help="Affiche le dashboard sans produire de PDF.",
    )
    parser.add_argument(
        "--output-dir", default="output",
        help="Dossier de sortie pour le rapport PDF (défaut : output/).",
    )
    args = parser.parse_args()

    if args.generate_sample:
        from immoscope.sample_data import generate_portfolio
        with console.status("[cyan]Génération du portefeuille de démonstration..."):
            path = generate_portfolio(args.generate_sample)
        console.print(f"[green]✓[/green] Portefeuille généré : [bold]{path}[/bold]")
        return 0

    if not args.filepath:
        parser.print_help()
        return 1

    try:
        with console.status("[cyan]Chargement du portefeuille..."):
            data = load_portfolio(args.filepath)
        with console.status("[cyan]Calcul des KPI..."):
            kpis = compute_portfolio_kpis(data)
        with console.status("[cyan]Détection des anomalies..."):
            from immoscope.anomalies import detect_anomalies
            anomalies = detect_anomalies(data, kpis)

        from immoscope.dashboard import render_dashboard
        render_dashboard(data, kpis, anomalies, console=console)

        if not args.no_pdf:
            from immoscope.report import generate_report
            output_path = Path(args.output_dir) / f"rapport_immoscope_{date.today():%Y-%m-%d}.pdf"
            with console.status("[cyan]Génération du rapport PDF..."):
                generate_report(data, kpis, anomalies, output_path)
            console.print(
                f"\n[green]✓[/green] Rapport PDF généré : [bold]{output_path}[/bold]\n"
            )
    except FileNotFoundError as exc:
        err_console.print(f"Erreur : {exc}")
        return 1
    except ValueError as exc:
        err_console.print(f"Erreur de validation : {exc}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
