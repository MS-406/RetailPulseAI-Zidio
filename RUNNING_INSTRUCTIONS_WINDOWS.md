Prerequisites

- Python 3.11+ installed and on PATH
- Git (optional) if pulling the repo
- Windows PowerShell or CMD

1) Create and activate a virtual environment (recommended)

PowerShell (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

CMD:

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

2) Upgrade pip and install dependencies

If you are located inside the `RetailPulseAI-Zidio` folder (recommended):

```powershell
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

If you are at the workspace root (one level above the `RetailPulseAI-Zidio` folder):

```powershell
python -m pip install --upgrade pip
pip install -r RetailPulseAI-Zidio\requirements.txt
```

If some packages (Prophet, torch) fail to install, install wheels from PyPI or use CPU-only torch:

```powershell
pip install prophet
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

3) Verify data files

Ensure the raw data file exists at `RetailPulseAI-Zidio\data\raw\online_retail.csv` (or at the workspace root `online_retail.csv`).

4) Run the reproducible Week 2 pipeline

If you are inside the `RetailPulseAI-Zidio` folder (current directory):

```powershell
python .\scripts\week2_pipeline.py
```

If you are at the workspace root (one level above the project folder):

```powershell
python RetailPulseAI-Zidio\scripts\week2_pipeline.py
```

This will create outputs under `RetailPulseAI-Zidio\exports` and write the report to `RetailPulseAI-Zidio\reports\week1_week2_completion_report.md`.

5) Optional: run the analysis script

```powershell
python retail_pulse_analysis.py
```

This script is a standalone runner that writes artifacts to `retail_pulse_outputs/`.

6) Explore notebooks

Open the notebooks under `RetailPulseAI-Zidio\notebooks` in Jupyter or VS Code and run cells interactively. Use the activated environment so kernels see installed packages.

Troubleshooting

- Encoding errors loading CSV: if reading fails, try `encoding:"ISO-8859-1"` or `encoding:"latin1"`.
- Heavy installs: consider installing CPU-only PyTorch and skipping optional packages like `apache-airflow` if not used locally.
- If `pip install -r requirements.txt` fails due to `prophet` or `lightning`, install them separately with prebuilt wheels or use conda.

Want me to run the install in your PowerShell now or create a helper `run_all.bat`?