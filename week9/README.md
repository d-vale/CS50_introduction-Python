# ImmoScope
#### Video Demo: disponible sur demande — contactez-moi en privé.
#### Description:

ImmoScope is a command-line tool that analyses a real-estate portfolio from a multi-sheet Excel
export, computes the financial KPIs that property managers actually care about, surfaces
anomalies, and ships out a polished PDF report alongside a colourful terminal dashboard.

The project is the final submission for Harvard's CS50's Introduction to Programming with Python
(CS50P). It is rooted in a real workplace need: I work at **Bobst Régie Immobilière**, a Swiss
property-management firm in Yverdon-les-Bains, on a bachelor thesis dealing with the **Quorum**
ERP. Quorum exports building, lot, lease and transaction data to spreadsheets that managers then
analyse by hand — a slow, error-prone exercise. ImmoScope demonstrates that a small Python script
can give a régie a defensible second opinion in under three seconds: open the workbook, surface
the dangerous outliers, and hand back a print-ready report ready to go in the file.

The tool is deliberately self-contained. A single command (`python project.py --generate-sample`)
produces a realistic Swiss portfolio so reviewers can run the full pipeline without any input
data. Everything from currency formatting (Swiss apostrophe thousands: `1'850.00 CHF`) to the
French anomaly labels reflects the target market.

### How it works

1. **Ingestion** — `load_portfolio` reads the workbook with `pandas` + `openpyxl`, validates the
   schema (four required sheets, expected columns) and returns four DataFrames.
2. **KPI calculation** — `compute_portfolio_kpis` orchestrates the maths in `immoscope/kpis.py`:
   annual revenue, expenses, NOI, gross/net yields, vacancy rate, average rent per m² by city,
   per-building metrics, and ranked top/bottom buildings.
3. **Anomaly detection** — `immoscope/anomalies.py` runs four detectors (below-market rent,
   excessive expense, long vacancy, missing monthly rent) and returns colour-coded findings.
   A regex (`^LOT-\d{3}-\d{2}$`) validates lot identifiers, satisfying the CS50P "Regular
   Expressions" learning objective.
4. **Terminal dashboard** — `immoscope/dashboard.py` renders an ASCII banner, an overview panel,
   KPI tables and an anomaly table with `rich`. Severity is colour-coded (red/yellow/cyan).
5. **PDF report** — `immoscope/report.py` builds a paginated portfolio report with `reportlab`:
   cover page, executive summary, KPI tables, three `matplotlib` charts (revenue per building,
   expenses pie, monthly cashflow line) embedded as PNG, an anomaly table, and a paginated footer.

### File map

- `project.py` — entry point. Contains the four CS50P-required top-level functions
  (`load_portfolio`, `compute_portfolio_kpis`, `format_chf`, `main`). The first two delegate
  details to the `immoscope/` package but keep meaningful, testable orchestration logic.
- `test_project.py` — `pytest` suite with one `test_<name>` per top-level function plus error-path
  coverage. Uses `tmp_path` fixtures so the repository stays clean.
- `requirements.txt` — pip dependencies (`pandas`, `openpyxl`, `rich`, `matplotlib`, `reportlab`,
  `faker`, `pytest`).
- `immoscope/sample_data.py` — generator producing a deterministic Swiss demo portfolio with four
  intentionally planted anomalies, so the detection module always finds something on the demo.
- `immoscope/loader.py` — schema definitions and column validation; raises `ValueError` with a
  useful message on malformed exports.
- `immoscope/kpis.py` — atomic financial calculations consumed by `compute_portfolio_kpis`.
- `immoscope/anomalies.py` — four anomaly detectors plus the regex `lot_id` validator.
- `immoscope/dashboard.py` — `rich` rendering of the terminal dashboard.
- `immoscope/report.py` — ReportLab + matplotlib PDF generator.

### Design choices

- **`rich` over a web UI** — the demo had to be a single-process CLI for CS50P, and `rich`
  delivers a striking visual result without HTTP boilerplate or a JS bundle.
- **`reportlab` over `weasyprint`** — `weasyprint` needs Cairo and Pango, system libraries that
  reviewers may not have. ReportLab is pure Python wheels and "just works" inside any venv.
- **Swiss apostrophe formatting** — the target audience is Swiss property managers; outputs that
  read `CHF 1'850.00` are immediately recognisable, whereas `CHF 1,850.00` looks American.
- **Four-sheet Excel model** — mirrors the real Quorum ERP schema (Immeubles / Lots / Baux /
  Transactions). Anyone familiar with Quorum recognises the structure on sight.
- **Planted anomalies in demo data** — guarantees that the detection module always has something
  to highlight during the video demo, even with a fixed RNG seed.

### How to run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Generate a demo portfolio
python project.py --generate-sample data/portfolio_demo.xlsx

# Run the full analysis (dashboard + PDF)
python project.py data/portfolio_demo.xlsx

# Dashboard only, no PDF
python project.py --no-pdf data/portfolio_demo.xlsx

# Tests
pytest -v
```

### Limits and future work

- The detectors use static thresholds; a future version could learn building-specific norms.
- There is no direct connection to the Quorum API yet — the current bridge is the Excel export.
- The PDF is not yet branded for a specific régie; a logo and corporate palette would be a
  trivial extension.
