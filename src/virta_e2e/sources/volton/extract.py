import json
from datetime import datetime, timezone
from pathlib import Path
import requests
from virta_e2e.config import API_URL, RAW_DATA_DIR, HEADERS

# Get electricity spot price from Volton API
def extract_data() -> dict:

    response = requests.get(
        API_URL,
        headers=HEADERS,
        timeout=30,
    )

    # If 404 or 500
    response.raise_for_status()

    # Transform JSON to dict
    data = response.json()

    # Create rawdata dir if there's none
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Timestamp for the filename
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    file_path = RAW_DATA_DIR / f"volton_{timestamp}.json"

    # Save original API call as is. This original raw data is for further processing.
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"Raw data saved: {file_path}")

    return data

if __name__ == "__main__":
    extract_data()