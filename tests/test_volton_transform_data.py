from virta_e2e.sources.volton.transform import transform_data

if __name__ == "__main__":
    data = {
        "rows": [
            {"mtu_start": "2026-10-27T22:00:00Z", "price_eur_mwh": 1.99},
            {"mtu_start": "2026-10-27T22:15:00Z", "price_eur_mwh": 1.99},
            {"mtu_start": "2026-10-27T22:30:00Z", "price_eur_mwh": 1.5},
            {"mtu_start": "2026-10-27T22:45:00Z", "price_eur_mwh": 1.0},
            {"mtu_start": "2026-10-27T23:00:00Z", "price_eur_mwh": 1.51},
        ]
    }

    transform_data(data)
    print(data)
