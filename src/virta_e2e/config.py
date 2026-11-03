# Contains information on project settings, API data sources and database
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Volton API
API_URL = "https://public-data.volton.energy/v1/day-ahead-spot-fi/latest.json"

# Data storage destinations
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATABASE_PATH = PROJECT_ROOT / "data" / "virta.e2e.db"