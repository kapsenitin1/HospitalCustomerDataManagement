import os
from src.etl_pipeline import *

def main():
    input_file = "data/input/customer_data.txt"
    archive_dir = "data/archive"
    output_dir = "data/output"

     # Check if input file exists
    if not check_input_file(input_file):
        return

    # Load and process data
    df = load_data(input_file)
    transformed_df = transform_data(df)

    # Save country-specific tables
    save_to_country_tables(transformed_df, output_dir)

    # Archive processed file
    archive_file(input_file, archive_dir)
    print(f"Data processing complete. Files saved in {output_dir}. Input file archived.")

if __name__ == "__main__":
    main()
