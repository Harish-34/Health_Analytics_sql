import os
import psycopg2
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Step 1: Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="Health_DataBase",         # 🔁 Replace with your DB name
    user="postgres",          # 🔁 Replace with your DB username
    password="postgres"       # 🔁 Replace with your DB password
)
cur = conn.cursor()

# Step 2: Get absolute path to cleaned files
base_dir = os.path.dirname(os.path.abspath(__file__))  # gets /database/
clean_dir = os.path.abspath(os.path.join(base_dir, "../data/outputs/"))

# Step 3: File → Table mapping
file_to_table = {
    "cleaned_DimPatient.csv": "dimpatient",
    "cleaned_DimPhysician.csv": "dimphysician",
    "cleaned_DimSpeciality.csv": "dimspeciality",
    "cleaned_DimHospital.csv": "dimhospital",
    "cleaned_DimPayer.csv": "dimpayer",
    "cleaned_DimCptCode.csv": "dimcptcode",
    "cleaned_DimDiagnosisCode.csv": "dimdiagnosiscode",
    "cleaned_DimDate.csv": "dimdate",
    "cleaned_DimTransaction.csv": "dimtransaction",
    "cleaned_FactTable.csv": "facttable"
}

# Step 4: Load each CSV into corresponding table
for file, table in file_to_table.items():
    file_path = os.path.join(clean_dir, file)
    print(f"🔎 Looking for file: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        next(f)  # Skip header row
        try:
            cur.copy_expert(f"COPY {table} FROM STDIN WITH CSV HEADER DELIMITER ','", f)
            print(f"✅ Loaded {file} into {table}")
        except Exception as e:
            print(f"❌ Error loading {file} → {table}: {e}")

# Step 5: Commit and close
conn.commit()
cur.close()
conn.close()
print("🚀 All done.")