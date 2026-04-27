"""PDF report generation with ReportLab and matplotlib charts.

Produces a paginated portfolio report with cover page, executive summary,
KPI tables, three matplotlib charts embedded as PNG images, an anomalies
table, and a paginated footer.
"""
from __future__ import annotations

import tempfile
from datetime import date, datetime
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from reportlab.lib import colors  # noqa: E402
from reportlab.lib.pagesizes import A4  # noqa: E402
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet  # noqa: E402
from reportlab.lib.units import cm, mm  # noqa: E402
from reportlab.pdfgen.canvas import Canvas  # noqa: E402
from reportlab.platypus import (  # noqa: E402
    BaseDocTemplate, Frame, Image, PageBreak, PageTemplate, Paragraph,
    Spacer, Table, TableStyle,
)

PRIMARY = colors.HexColor("#0F4C81")
ACCENT = colors.HexColor("#E89F49")
MUTED = colors.HexColor("#5C6B7A")
LIGHT_BG = colors.HexColor("#F4F6F9")
HIGH_BG = colors.HexColor("#FBE9E7")
MED_BG = colors.HexColor("#FFF4E0")
LOW_BG = colors.HexColor("#E8F0FE")

CHART_DPI = 140


def generate_report(
    data: dict[str, Any],
    kpis: dict[str, Any],
    anomalies: list[dict[str, Any]],
    output_path: str | Path,
) -> Path:
    """Render the full portfolio PDF report to ``output_path``."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    styles = _build_styles()

    with tempfile.TemporaryDirectory() as tmpdir:
        chart_revenue = _chart_revenue_by_building(kpis["building_metrics"], Path(tmpdir))
        chart_expenses = _chart_expenses_pie(kpis["expenses_by_type"], Path(tmpdir))
        chart_cashflow = _chart_monthly_cashflow(kpis["monthly_cashflow"], Path(tmpdir))

        story: list[Any] = []
        story += _cover_page(styles, kpis)
        story.append(PageBreak())
        story += _executive_summary(styles, kpis, anomalies)
        story += _kpi_section(styles, kpis)
        story.append(PageBreak())
        story += _buildings_section(styles, kpis["building_metrics"])
        story.append(PageBreak())
        story += _charts_section(styles, chart_revenue, chart_expenses, chart_cashflow)
        story.append(PageBreak())
        story += _anomalies_section(styles, anomalies)

        doc = _build_doc(output_path)
        doc.build(story)

    return output_path


def _build_doc(output_path: Path) -> BaseDocTemplate:
    doc = BaseDocTemplate(
        str(output_path), pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2.5 * cm,
        title="ImmoScope — Rapport portefeuille",
        author="ImmoScope",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="default", frames=frame, onPage=_paint_footer)])
    return doc


def _build_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title", parent=base["Title"],
            fontName="Helvetica-Bold", fontSize=28, leading=34,
            textColor=PRIMARY, alignment=1,
        ),
        "subtitle": ParagraphStyle(
            "subtitle", parent=base["Heading2"],
            fontName="Helvetica", fontSize=14, leading=18,
            textColor=MUTED, alignment=1,
        ),
        "h1": ParagraphStyle(
            "h1", parent=base["Heading1"],
            fontName="Helvetica-Bold", fontSize=18, leading=22,
            textColor=PRIMARY, spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2", parent=base["Heading2"],
            fontName="Helvetica-Bold", fontSize=13, leading=16,
            textColor=PRIMARY, spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "body", parent=base["BodyText"],
            fontName="Helvetica", fontSize=10.5, leading=14,
            textColor=colors.black, spaceAfter=6,
        ),
        "body_muted": ParagraphStyle(
            "body_muted", parent=base["BodyText"],
            fontName="Helvetica-Oblique", fontSize=9.5, leading=13,
            textColor=MUTED,
        ),
        "kpi_label": ParagraphStyle(
            "kpi_label", parent=base["BodyText"],
            fontName="Helvetica", fontSize=10, textColor=MUTED,
        ),
        "kpi_value": ParagraphStyle(
            "kpi_value", parent=base["BodyText"],
            fontName="Helvetica-Bold", fontSize=14, textColor=PRIMARY,
        ),
    }


def _cover_page(styles: dict[str, ParagraphStyle], kpis: dict[str, Any]) -> list[Any]:
    today = date.today().strftime("%d %B %Y")
    return [
        Spacer(1, 5 * cm),
        Paragraph("ImmoScope", styles["title"]),
        Spacer(1, 0.4 * cm),
        Paragraph("Analyse de portefeuille immobilier", styles["subtitle"]),
        Spacer(1, 3 * cm),
        Paragraph(
            f"<para align='center'><b>Portefeuille</b> &nbsp;&nbsp; "
            f"{kpis['n_buildings']} immeubles &nbsp;·&nbsp; {kpis['n_lots']} lots</para>",
            styles["body"],
        ),
        Spacer(1, 0.6 * cm),
        Paragraph(f"<para align='center'>Rapport généré le {today}</para>", styles["body_muted"]),
        Spacer(1, 6 * cm),
        Paragraph(
            "<para align='center'>Format Quorum ERP simplifié — Bobst Régie Immobilière</para>",
            styles["body_muted"],
        ),
    ]


def _executive_summary(
    styles: dict[str, ParagraphStyle],
    kpis: dict[str, Any],
    anomalies: list[dict[str, Any]],
) -> list[Any]:
    from project import format_chf

    high = sum(1 for a in anomalies if a["severity"] == "high")
    summary = (
        f"Le portefeuille compte <b>{kpis['n_buildings']} immeubles</b> et "
        f"<b>{kpis['n_lots']} lots</b>, dont {kpis['n_active_leases']} sous bail "
        f"actif (taux de vacance : {kpis['vacancy_rate']:.1f} %). "
        f"Le revenu locatif annuel s'élève à <b>{format_chf(kpis['annual_revenue'])}</b>, "
        f"pour un NOI de <b>{format_chf(kpis['noi'])}</b>. "
        f"Le rendement net du portefeuille est de <b>{kpis['net_yield']:.2f} %</b>. "
        f"L'analyse a identifié <b>{len(anomalies)} anomalie(s)</b>"
        + (f", dont {high} de sévérité haute." if high else ".")
    )
    return [Paragraph("Synthèse exécutive", styles["h1"]), Paragraph(summary, styles["body"]), Spacer(1, 0.4 * cm)]


def _kpi_section(styles: dict[str, ParagraphStyle], kpis: dict[str, Any]) -> list[Any]:
    from project import format_chf

    rows = [
        ["Indicateur", "Valeur"],
        ["Revenu locatif annuel", format_chf(kpis["annual_revenue"])],
        ["Charges annuelles", format_chf(kpis["annual_expenses"])],
        ["NOI (Net Operating Income)", format_chf(kpis["noi"])],
        ["Valeur estimée du portefeuille", format_chf(kpis["total_value"])],
        ["Rendement brut", f"{kpis['gross_yield']:.2f} %"],
        ["Rendement net", f"{kpis['net_yield']:.2f} %"],
        ["Taux de vacance", f"{kpis['vacancy_rate']:.2f} %"],
    ]
    table = Table(rows, colWidths=[9 * cm, 7 * cm])
    table.setStyle(_kpi_table_style())
    return [Paragraph("Indicateurs clés", styles["h1"]), table, Spacer(1, 0.5 * cm)]


def _buildings_section(
    styles: dict[str, ParagraphStyle],
    building_metrics: Any,
) -> list[Any]:
    from project import format_chf

    rows = [["ID", "Immeuble", "Ville", "Revenu", "NOI", "Rdt net", "Vacance"]]
    for _, b in building_metrics.iterrows():
        rows.append([
            b["building_id"],
            b["name"][:24],
            b["city"],
            format_chf(b["annual_revenue"]),
            format_chf(b["noi"]),
            f"{b['net_yield']:.2f} %",
            f"{b['vacancy_rate']:.1f} %",
        ])
    table = Table(rows, colWidths=[1.8 * cm, 4.5 * cm, 3.0 * cm, 2.8 * cm, 2.8 * cm, 1.8 * cm, 1.8 * cm])
    table.setStyle(_data_table_style())
    return [Paragraph("Détail par immeuble", styles["h1"]), table, Spacer(1, 0.5 * cm)]


def _charts_section(
    styles: dict[str, ParagraphStyle],
    chart_revenue: Path,
    chart_expenses: Path,
    chart_cashflow: Path,
) -> list[Any]:
    return [
        Paragraph("Visualisations", styles["h1"]),
        Paragraph("Revenus annuels par immeuble", styles["h2"]),
        Image(str(chart_revenue), width=16 * cm, height=8 * cm),
        Spacer(1, 0.5 * cm),
        Paragraph("Répartition des charges (12 derniers mois)", styles["h2"]),
        Image(str(chart_expenses), width=12 * cm, height=8 * cm),
        Spacer(1, 0.5 * cm),
        Paragraph("Cashflow mensuel net (24 mois)", styles["h2"]),
        Image(str(chart_cashflow), width=16 * cm, height=7 * cm),
    ]


def _anomalies_section(
    styles: dict[str, ParagraphStyle],
    anomalies: list[dict[str, Any]],
) -> list[Any]:
    if not anomalies:
        return [
            Paragraph("Anomalies", styles["h1"]),
            Paragraph("Aucune anomalie détectée. Portefeuille en bonne santé.", styles["body"]),
        ]

    rows = [["Sévérité", "Type", "Lot", "Description"]]
    for a in anomalies:
        rows.append([a["severity"].upper(), a["type"], a["lot_id"], a["description"]])
    table = Table(rows, colWidths=[1.8 * cm, 3.5 * cm, 2.5 * cm, 8.8 * cm])
    table.setStyle(_anomaly_table_style(anomalies))
    return [
        Paragraph("Anomalies détectées", styles["h1"]),
        Paragraph(
            f"<b>{len(anomalies)}</b> anomalie(s) identifiée(s) sur le portefeuille.",
            styles["body"],
        ),
        Spacer(1, 0.2 * cm),
        table,
    ]


def _kpi_table_style() -> TableStyle:
    return TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 11),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica"),
        ("FONTNAME", (1, 1), (1, -1), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_BG]),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ])


def _data_table_style() -> TableStyle:
    return TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("ALIGN", (3, 0), (-1, -1), "RIGHT"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_BG]),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
    ])


def _anomaly_table_style(anomalies: list[dict[str, Any]]) -> TableStyle:
    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
    ])
    for i, a in enumerate(anomalies, start=1):
        bg = HIGH_BG if a["severity"] == "high" else MED_BG if a["severity"] == "medium" else LOW_BG
        style.add("BACKGROUND", (0, i), (-1, i), bg)
    return style


def _chart_revenue_by_building(building_metrics: Any, tmpdir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(8, 4))
    bm = building_metrics.sort_values("annual_revenue", ascending=True)
    ax.barh(bm["name"].str.slice(0, 22), bm["annual_revenue"], color="#0F4C81")
    ax.set_xlabel("Revenu locatif annuel (CHF)")
    ax.set_title("Revenus annuels par immeuble")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", labelsize=8)
    fig.tight_layout()
    out = tmpdir / "revenue.png"
    fig.savefig(out, dpi=CHART_DPI, bbox_inches="tight")
    plt.close(fig)
    return out


def _chart_expenses_pie(expenses_by_type: dict[str, float], tmpdir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(6, 5))
    if expenses_by_type:
        labels = list(expenses_by_type.keys())
        values = list(expenses_by_type.values())
        palette = ["#0F4C81", "#E89F49", "#3E7CB1", "#7A9CC6", "#B6C9DD"]
        ax.pie(
            values, labels=labels, autopct="%1.1f%%",
            startangle=90, colors=palette[:len(labels)],
            textprops={"fontsize": 9},
        )
        ax.set_title("Charges par type")
    else:
        ax.text(0.5, 0.5, "Aucune charge",
                horizontalalignment="center", verticalalignment="center")
        ax.axis("off")
    fig.tight_layout()
    out = tmpdir / "expenses.png"
    fig.savefig(out, dpi=CHART_DPI, bbox_inches="tight")
    plt.close(fig)
    return out


def _chart_monthly_cashflow(monthly_cashflow: Any, tmpdir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(9, 4))
    if not monthly_cashflow.empty:
        ax.plot(
            monthly_cashflow["month"], monthly_cashflow["net_cashflow"],
            color="#0F4C81", linewidth=2, marker="o", markersize=4,
        )
        ax.fill_between(
            monthly_cashflow["month"], monthly_cashflow["net_cashflow"],
            alpha=0.15, color="#0F4C81",
        )
        ax.axhline(0, color="#5C6B7A", linewidth=0.5)
        ax.set_xlabel("Mois")
        ax.set_ylabel("Cashflow net (CHF)")
        ax.set_title("Cashflow mensuel net (24 derniers mois)")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", rotation=45, labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
    fig.tight_layout()
    out = tmpdir / "cashflow.png"
    fig.savefig(out, dpi=CHART_DPI, bbox_inches="tight")
    plt.close(fig)
    return out


def _paint_footer(canvas: Canvas, doc: BaseDocTemplate) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    today = datetime.now().strftime("%d/%m/%Y")
    canvas.drawString(
        2 * cm, 1.3 * cm,
        f"ImmoScope — Généré le {today}",
    )
    canvas.drawRightString(
        A4[0] - 2 * cm, 1.3 * cm,
        f"Page {doc.page}",
    )
    canvas.setStrokeColor(MUTED)
    canvas.setLineWidth(0.3)
    canvas.line(2 * cm, 1.7 * cm, A4[0] - 2 * cm, 1.7 * cm)
    canvas.restoreState()
    _ = mm  # keep mm import in case future tweaks need it
