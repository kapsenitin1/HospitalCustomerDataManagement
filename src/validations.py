import pandas as pd

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and clean data."""
    # Remove rows with missing mandatory fields
    mandatory_fields = ["Customer_Name", "Customer_Id", "Open_Date"]
    for field in mandatory_fields:
        df = df[df[field].notnull()]
    
    # Remove rows with invalid Customer IDs
    df = df[df["Customer_Id"].apply(lambda x: str(x).isdigit())]
    
    return df
