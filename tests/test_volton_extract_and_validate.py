from virta_e2e.sources.volton.extract import extract_data
from virta_e2e.sources.volton.validate import validate_raw_data

if __name__ == "__main__":
    data = extract_data()
    validate_raw_data(data)
