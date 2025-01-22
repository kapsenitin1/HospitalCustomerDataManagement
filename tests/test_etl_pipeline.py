import pytest
import pandas as pd
from pathlib import Path
from src.etl_pipeline import transform_data, archive_file

def test_transform_data():
    # Mock input data

    data = {
        "Customer_Name": ["John", "Alex"],
        "Customer_Id": ["12345", "67890"],
        "Open_Date": ["20101012", "20101013"],
        "Last_Consulted_Date": ["20231201", "20231015"],
        "Vaccination_Type": ["MVD", "MVD"],
        "Dr_Name": ["Paul", "John"],
        "State": ["NY", "CA"],
        "Country": ["USA", "USA"],
        "DOB": ["19801012", "19901015"],
        "Is_Active": ["A", "A"]
    }
    df = pd.DataFrame(data)

    # Test transformation
    transformed_df = transform_data(df)
    assert "Age" in transformed_df.columns
    assert "Days_Since_Last_Consulted" in transformed_df.columns
    assert transformed_df["Needs_Followup"].dtype == bool
    assert transformed_df["Needs_Followup"].sum() >= 1  # One customer needs follow-up

def test_archive_file(tmp_path="data/input"):
    # Create a dummy file
    test_file_path = f"{tmp_path}/test.txt"
    test_file = Path(test_file_path)
    test_file.write_text("Test data")

    # Archive the file
    archive_dir = f"{tmp_path}/archive"
    archive_file(str(test_file), str(archive_dir))

    # Check file moved
    assert not test_file.exists()