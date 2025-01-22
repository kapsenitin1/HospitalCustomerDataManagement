# Hospital Customer Data Management

Hospital Customer Data Management is an ETL-based system designed to handle customer data for a global multi-specialty hospital network. The system processes and organizes patient data into country-specific tables, supporting vaccination tracking, doctor consultations and customer details. The project utilizes Python for handling the ETL pipeline and performs data validation and logging. 

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [ETL Pipeline](#etl-pipeline)
5. [File Format](#file-format)

## Project Overview

The system is designed to manage customer data for a multi-specialty hospital chain with locations worldwide. Patient data is pulled from the source system, processed and stored in country-specific tables. The data is validated, archived, and logged during the ETL process. The primary goal is to ensure smooth and scalable customer data management across locations.

### Key Features:
- **ETL Process:** Extract, transform, and load customer data into corresponding country tables.
- **Vaccination Tracking:** Handling patient vaccination details.
- **Consultation Tracking:** Recording doctor visits and consultations.
- **Logging & Archiving:** All processing steps are logged, and data files are archived post-processing.

## Usage

To start the ETL pipeline:

1. Place the `customer_data.txt` file in the input directory.
2. Run the ETL pipeline by executing the following command:

    ```bash
    python src/main.py
    ```

This will process the customer data and create country-specific tables in the database.

### Output
- **File format:** Data is processed and saved into a pipe-delimited format (`|`).
- **Logs:** A detailed log file will be generated during the execution.

## ETL Pipeline

The ETL pipeline consists of the following steps:

1. **Data Extraction:**
   - Customer data is pulled from the source system and stored in `customer_data.txt`.
   
2. **Data Transformation:**
   - The data is transformed by validating, filtering, and cleaning it (e.g. handling missing values, converting date formats, etc.).
   - Country-based processing ensures that customer records are routed to the correct country tables.

3. **Data Loading:**
   - The transformed data is loaded into staging tables, followed by country-specific tables.
   - Each country's table includes additional derived columns, such as `age` and `days since last consultation >30`.

4. **Archiving:**
   - Once processed, the `customer_data.txt` file is moved to the `Archive` folder.

5. **Logging:**
   - All steps of the ETL process are logged with appropriate timestamps for traceability.

## File Format

The input file `customer_data.txt` follows a pipe-delimited format (`|`) and consists of the following columns:

### Header Record Layout:

|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Type|Dr_Name|State|Country|DOB|Is_Active

### Data Record Layout:

|D|Alex|123457|20101012|20121013|MVD|Paul|SA|USA|06031987|A

### Data File Specifications:

- **File Name**: customer_data.txt
- **Delimiter**: Pipe (`|`)
- **Date Format**: `YYYYMMDD`
- **Mandatory Columns**: Customer Name, Customer ID, Open Date, and Country.

### Data Types & Constraints:

- **Customer Name**: VARCHAR(255), Mandatory
- **Customer ID**: VARCHAR(18), Mandatory
- **Open Date**: DATE(8), Mandatory
- **Vaccination Type**: CHAR(5), Optional
- **Doctor Name**: VARCHAR(255), Optional
- **State**: VARCHAR(5), Optional
- **Country**: VARCHAR(5), Optional
- **Date of Birth (DOB)**: DATE(8), Optional
- **Active Customer Flag**: CHAR(1), Optional

## Unit Testing

- Switch to HospitalCustomerDataManagement folder on your local machine
- Run pytest command to test pass/failure of unit test cases