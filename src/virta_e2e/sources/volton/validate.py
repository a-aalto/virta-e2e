from datetime import datetime
from virta_e2e.sources.volton.extract import extract_data

# Validate the rawdata structure from extract stage's API call
def validate_raw_data(data: dict) -> None:

    # Check if data is dict
    if not isinstance(data, dict):
        raise ValueError("API response must be a dictionary.")

    if "rows" not in data:
        raise ValueError("API response is missing 'rows'.")

    rows = data["rows"]

    # Check if 'rows' is type list
    if not isinstance(rows, list):
        raise ValueError("'rows' must be a list.")

    # Check if rows is null or not
    if not rows:
        raise ValueError("API returned no data.")

    # Iterate the rows elements and check their data types and the data
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"Row {index} must be a dictionary.")

        if "mtu_start" not in row:
            raise ValueError(f"Row {index} is missing 'mtu_start'.")

        if "price_eur_mwh" not in row:
            raise ValueError(f"Row {index} is missing 'price_eur_mwh'.")

        # Check timestamp format
        try:
            datetime.fromisoformat(
                row["mtu_start"].replace("Z", "+00:00")
            )
        except (ValueError, AttributeError):
            raise ValueError(
                f"Row {index} has an invalid timestamp."
            )

        price = row["price_eur_mwh"]

        # Price can be null. Otherwise it must be a number
        if price is not None and (
            isinstance(price, bool) or not isinstance(price, (int, float))
        ):
            raise ValueError(f"Row {index} has an invalid price.")

    print(f"Validation successfull: {len(rows)} rows.")

if __name__ == "__main__":
    data = extract_data()
    validate_raw_data(data)