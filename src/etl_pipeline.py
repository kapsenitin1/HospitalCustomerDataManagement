import os
import pandas as pd
import shutil
from datetime import datetime
from src.validations import validate_data
from src.utils import setup_logging

logger = setup_logging("HospitalCustomerDataManagement")

def check_input_file(file_path: str) -> bool:
    """Check if the input file exists."""
    if not os.path.exists(file_path):
        logger.error(f"Input file '{file_path}' not found.")
        return False
    logger.info(f"Input file '{file_path}' found.")
    return True

def archive_file(file_path: str, archive_dir: str):
    """Move processed file to the archive directory."""
    os.makedirs(archive_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = os.path.basename(file_path)
    archived_path = os.path.join(archive_dir, f"{file_name}_{timestamp}")
    shutil.move(file_path, archived_path)
    logger.info(f"File '{file_path}' archived to '{archived_path}'.")

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a file into a DataFrame."""
    try:
        df = pd.read_csv(file_path, sep="|", skiprows=1, header=None)
        df.columns = [
            "Extra","Record_Type", "Customer_Name", "Customer_Id", "Open_Date",
            "Last_Consulted_Date", "Vaccination_Type", "Dr_Name",
            "State", "Country", "DOB", "Is_Active"
        ]
        df = df.drop(columns=["Extra", "Record_Type"])
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise ValueError(f"Error loading data: {e}")

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Transform data by adding derived columns and filtering."""
    # Convert date columns to datetime
    date_cols = ["Open_Date", "Last_Consulted_Date", "DOB"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], format="%Y%m%d", errors="coerce")
    
    # Add derived columns
    today = pd.Timestamp.now()
    df["Age"] = (today - df["DOB"]).dt.days // 365
    df["Days_Since_Last_Consulted"] = (today - df["Last_Consulted_Date"]).dt.days
    df["Needs_Followup"] = df["Days_Since_Last_Consulted"] > 30

    # Drop invalid records
    df = validate_data(df)
    return df

def save_to_country_tables(df: pd.DataFrame, output_dir: str):
    """Save records to country-specific tables."""
    os.makedirs(output_dir, exist_ok=True)
    df = df.filter(items=["Customer_Id", "Customer_Name", "Country", "Vaccination_Type", "Last_Consulted_Date", "Age", "Days_Since_Last_Consulted", "Needs_Followup"])
    
    countries = df["Country"].unique()
    for country in countries:
        country_df = df[df["Country"] == country]
        output_path = f"{output_dir}/Table_{country}.txt"
        country_df = country_df.drop("Country", axis=1)
        country_df.to_csv(output_path, sep="|", index=False)
        logger.info(f"Country-specific table saved to '{output_path}'.")
