"""Terminal dashboard rendering with rich.

Renders four sections (overview, KPI, top buildings, anomalies) using a
restrained palette so the output stays legible in any terminal theme.
"""
from __future__ import annotations

from typing import Any

from rich.align import Align
from rich.box import HEAVY, ROUNDED
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

BANNER = r"""[bold cyan]
 ___                            ____
|_ _|_ __ ___  _ __ ___   ___  / ___|  ___ ___  _ __   ___
 | || '_ ` _ \| '_ ` _ \ / _ \ \___ \ / __/ _ \| '_ \ / _ \
 | || | | | | | | | | | | (_) | ___) | (_| (_) | |_) |  __/
|___|_| |_| |_|_| |_| |_|\___/ |____/ \___\___/| .__/ \___|
                                               |_|         [/bold cyan]
[dim]Analyse de portefeuille immobilier — format Quorum[/dim]
"""

SEVERITY_STYLES = {
    "high": "bold red",
    "medium": "bold yellow",
    "low": "bold cyan",
}


def render_dashboard(
    data: dict[str, Any],
    kpis: dict[str, Any],
    anomalies: list[dict[str, Any]],
    console: Console | None = None,
) -> None:
    """Render the full terminal dashboard to ``console`` (or a fresh one)."""
    console = console or Console()
    console.print(BANNER)
    console.print(_overview_panel(data, kpis))
    console.print(Columns([_kpi_panel(kpis), _rent_panel(kpis)], equal=False, expand=True))
    console.print(_top_buildings_panel(kpis))
    console.print(_anomalies_panel(anomalies))
    console.print(_footer())


def _overview_panel(data: dict[str, Any], kpis: dict[str, Any]) -> Panel:
    cities = data["immeubles"]["city"].value_counts().to_dict()
    city_str = ", ".join(f"{c} ({n})" for c, n in cities.items())
    body = Text.assemble(
        ("Immeubles  : ", "dim"), (f"{kpis['n_buildings']:>4}\n", "bold"),
        ("Lots       : ", "dim"), (f"{kpis['n_lots']:>4}\n", "bold"),
        ("Baux actifs: ", "dim"), (f"{kpis['n_active_leases']:>4}\n", "bold"),
        ("Vacance    : ", "dim"),
        (f"{kpis['vacancy_rate']:>4.1f} %\n", _vacancy_style(kpis["vacancy_rate"])),
        ("Villes     : ", "dim"), (f"{city_str}", "italic"),
    )
    return Panel(body, title="[bold]Vue d'ensemble[/bold]", border_style="cyan", box=ROUNDED)


def _kpi_panel(kpis: dict[str, Any]) -> Panel:
    from project import format_chf

    table = Table.grid(padding=(0, 2))
    table.add_column(style="dim", justify="right")
    table.add_column(justify="right", style="bold")

    table.add_row("Revenu locatif annuel", _money(format_chf(kpis["annual_revenue"]), positive=True))
    table.add_row("Charges annuelles", _money(format_chf(kpis["annual_expenses"]), positive=False))
    table.add_row("NOI", _money(format_chf(kpis["noi"]), positive=kpis["noi"] >= 0))
    table.add_row("Valeur estimée", format_chf(kpis["total_value"]))
    table.add_row("Rendement brut", _percent(kpis["gross_yield"]))
    table.add_row("Rendement net", _percent(kpis["net_yield"]))
    return Panel(table, title="[bold]KPI financiers[/bold]", border_style="green", box=ROUNDED)


def _rent_panel(kpis: dict[str, Any]) -> Panel:
    by_city = kpis["avg_rent_per_m2_by_city"]
    if not by_city:
        body: Any = Text("Aucune donnée", style="dim")
    else:
        table = Table.grid(padding=(0, 2))
        table.add_column(style="dim")
        table.add_column(justify="right", style="bold")
        for city, val in sorted(by_city.items(), key=lambda kv: -kv[1]):
            table.add_row(city, f"{val:.2f} CHF/m²")
        body = table
    return Panel(body, title="[bold]Loyer moyen au m² par ville[/bold]", border_style="magenta", box=ROUNDED)


def _top_buildings_panel(kpis: dict[str, Any]) -> Panel:
    from project import format_chf

    table = Table(box=HEAVY, header_style="bold cyan", expand=True)
    table.add_column("ID", style="dim")
    table.add_column("Immeuble")
    table.add_column("Ville", style="dim")
    table.add_column("Revenu", justify="right")
    table.add_column("NOI", justify="right", style="bold")
    table.add_column("Rendement net", justify="right")
    table.add_column("Vacance", justify="right")
    for b in kpis["top_buildings"]:
        table.add_row(
            b["building_id"], b["name"], b["city"],
            format_chf(b["annual_revenue"]),
            f"[green]{format_chf(b['noi'])}[/green]",
            _percent(b["net_yield"]),
            f"{b['vacancy_rate']:.1f} %",
        )
    return Panel(table, title="[bold]🏢 Top 3 immeubles par NOI[/bold]", border_style="green", box=ROUNDED)


def _anomalies_panel(anomalies: list[dict[str, Any]]) -> Panel:
    if not anomalies:
        body: Any = Align.center(Text("Aucune anomalie détectée 🎉", style="bold green"))
        return Panel(body, title="[bold]🚨 Anomalies[/bold]", border_style="green", box=ROUNDED)

    table = Table(box=HEAVY, header_style="bold yellow", expand=True)
    table.add_column("Sévérité")
    table.add_column("Type")
    table.add_column("Lot", style="dim")
    table.add_column("Description")
    for a in anomalies:
        style = SEVERITY_STYLES.get(a["severity"], "")
        sev = Text(a["severity"].upper(), style=style)
        table.add_row(sev, a["type"], a["lot_id"], a["description"])

    summary = Text.assemble(
        ("Total : ", "dim"), (f"{len(anomalies)}", "bold"),
        ("   ─   ", "dim"),
        *_severity_breakdown(anomalies),
    )
    return Panel(
        Group(table, Text(""), summary),
        title="[bold]🚨 Anomalies détectées[/bold]",
        border_style="red", box=ROUNDED,
    )


def _severity_breakdown(anomalies: list[dict[str, Any]]) -> list[tuple[str, str]]:
    counts = {"high": 0, "medium": 0, "low": 0}
    for a in anomalies:
        counts[a["severity"]] = counts.get(a["severity"], 0) + 1
    parts: list[tuple[str, str]] = []
    if counts["high"]:
        parts += [(f"{counts['high']} high", "bold red"), ("  ", "")]
    if counts["medium"]:
        parts += [(f"{counts['medium']} medium", "bold yellow"), ("  ", "")]
    if counts["low"]:
        parts += [(f"{counts['low']} low", "bold cyan"), ("  ", "")]
    return parts


def _footer() -> Text:
    return Text.assemble(
        ("\n💡 ", "yellow"),
        ("Pour générer le rapport PDF : ", "dim"),
        ("python project.py <fichier.xlsx>", "bold cyan"),
        ("   |   pour le dashboard seul, ajoutez ", "dim"),
        ("--no-pdf\n", "bold cyan"),
    )


def _money(text: str, positive: bool) -> str:
    color = "green" if positive else "red"
    return f"[{color}]{text}[/{color}]"


def _percent(value: float) -> str:
    color = "green" if value >= 3 else "yellow" if value >= 1 else "red"
    return f"[{color}]{value:.2f} %[/{color}]"


def _vacancy_style(rate: float) -> str:
    if rate < 8:
        return "bold green"
    if rate < 15:
        return "bold yellow"
    return "bold red"
