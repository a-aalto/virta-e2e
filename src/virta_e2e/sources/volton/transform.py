from datetime import datetime, timezone

# Transform the data
def transform_data(data: dict) -> list[dict]:

    # Transform the timestamps of the data into suitable format (for storing into database)

    transformed_rows = list()
    price_row = "price_eur_mwh"

    for row in data["rows"]:

        timestamp = datetime.fromisoformat(
            row["mtu_start"].replace("Z", "+00:00")
        )

        timestamp = timestamp.astimezone(timezone.utc)

        # Save timestamp in ISO 8601 format
        timestamp = timestamp.isoformat(timespec="seconds").replace(
            "+00:00", "Z"
        )

        transformed_row = {
            "time_start": timestamp,
            price_row: row["price_eur_mwh"]
            
        }

        transformed_rows.append(transformed_row)

    return transformed_rows
