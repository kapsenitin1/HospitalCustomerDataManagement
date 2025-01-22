import pandas as pd
import random
from faker import Faker

# Initialize Faker and set seed for reproducibility
fake = Faker()
Faker.seed(42)
random.seed(42)

# Constants
NUM_RECORDS = 100
COUNTRIES = ["USA", "India", "Canada"]
STATES = {
    "USA": ["NY", "CA", "TX", "FL", "WA"],
    "India": ["MH", "DL", "KA", "TN", "UP"],
    "Canada": ["ON", "QC", "BC", "AB", "NS"],
}
VACCINATION_TYPES = ["MVD", "BCG", "COVID", "Hepatitis"]
RECORD_TYPE = "D"

# Generate customer data
def generate_customer_data(num_records):
    records = []
    for _ in range(num_records):
        country = random.choice(COUNTRIES)
        state = random.choice(STATES[country])
        record = {
            "": "",
            "H": RECORD_TYPE,
            "Customer_Name": fake.first_name(),
            "Customer_Id": random.randint(10000, 99999),
            "Open_Date": fake.date_between(start_date="-10y", end_date="today").strftime("%Y%m%d"),
            "Last_Consulted_Date": fake.date_between(start_date="-5y", end_date="today").strftime("%Y%m%d"),
            "Vaccination_Type": random.choice(VACCINATION_TYPES),
            "Doctor_Name": fake.first_name(),
            "State": state,
            "Country": country,
            "Date_of_Birth": fake.date_of_birth(minimum_age=1, maximum_age=100).strftime("%Y%m%d"),
            "Is_Active": random.choice(["A", "I"]),
        }
        records.append(record)
    return records

# Create data and save to file
data = generate_customer_data(NUM_RECORDS)
df = pd.DataFrame(data)

# Save to pipe-delimited file
file_path = "data/input/customer_data.txt"
df.to_csv(file_path, sep="|", index=False, header=True)

file_path
