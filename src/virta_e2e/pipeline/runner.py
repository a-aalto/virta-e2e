from virta_e2e.sources.volton.extract import extract_data
from virta_e2e.sources.volton.transform import transform_data
from virta_e2e.sources.volton.validate import validate_raw_data
from virta_e2e.storage.sqlite import load_data


def run_pipeline() -> None:

    print("Pipeline is running...")

    # Extract the data
    print("Extracting data...")
    data = extract_data()

    # Validate the raw data
    print("Validating the extracted data...")
    validate_raw_data(data)

    # Transform the data
    print("Transforming the data...")
    transformed_data = transform_data(data)

    # Load the data into SQLite
    print("Loading the data into the SQlite database...")
    load_data(transformed_data)

    print("Pipeline has been executed successfully.")
