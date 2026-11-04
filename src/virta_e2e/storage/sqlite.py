import sqlite3

from virta_e2e.config import DATABASE_PATH


# Load the data into an SQL table (SQLite3)
def load_data(rows: list[dict]) -> None:

    # Check if virta-e2e/data/ exists, if not, create it
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        # Create the table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS electricity_prices (
                time_start TEXT PRIMARY KEY,
                price_eur_mwh READ
            )
        """)
        # ... and insert the data into the table
        connection.executemany(
            """
            INSERT INTO electricity_prices (
                time_start,
                price_eur_mwh
            )
            VALUES (?, ?)
            ON CONFLICT(time_start)
            DO UPDATE SET
                price_eur_mwh = excluded.price_eur_mwh
            """,
            [(row["time_start"], row["price_eur_mwh"]) for row in rows],
        )
    print(f"Loaded {len(rows)} rows into the database.")
