# Module 1 Team Task – Situation 2: "Rating Wars"

A weighted film rating: ratings from reviews that readers found helpful count more,
so bots and mass ratings have less impact.

## Setup

Install uv (needs Python and pip):

```bash
pip install uv
```

Then clone the repo and install the dependencies:

```bash
git clone https://github.com/Uzairkheshgi/big_data_and_complex_socio_technical_systems.git
cd big_data_and_complex_socio_technical_systems
uv sync
```

## Data

The data is not in the repo. Place the CSV here, with exactly this file name:

```
module1/data/STS Module 1 Team Task Data.csv
```

## Run

Linux / macOS:

```bash
uv run module1/main.py
```

Windows (PowerShell):

```powershell
uv run module1\main.py
```

Notebooks: open `eda.ipynb`, `weighting.ipynb` and `simulation.ipynb` in that order.

- **VS Code:** open the repo folder, open a notebook, click **Select Kernel** and choose
  the project's `.venv`, then **Run All**. Needs the Python and Jupyter extensions.
- **Browser:** `uv run jupyter lab module1`

## Files

- `data_cleaning.py` – load and clean the CSV
- `eda.ipynb` – exploratory analysis
- `weighting.py`, `weighting.ipynb` – review weight and weighted rating
- `simulation.py`, `simulation.ipynb` – simulated bot attack
- `main.py` – runs everything and prints the results
