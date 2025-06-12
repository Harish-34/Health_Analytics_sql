# 🏥 US Healthcare SQL Analytics Project

A complete end-to-end healthcare analytics solution using **PostgreSQL**, **pgAdmin**, and **Python** to uncover business insights from patient and claims data.

This project focuses on solving **20 real-time KPIs** across cost, coverage, delay patterns, physician performance, and patient demographics — driven by SQL automation and visual outputs.

---

## 🔧 Tech Stack & Tools

| Category         | Tools / Libraries                             | Purpose                                                                 |
|------------------|-----------------------------------------------|-------------------------------------------------------------------------|
| 🛢️ Database       | PostgreSQL                                     | Core relational database for storing healthcare data                   |
| 🧰 SQL Tool       | pgAdmin 4                                      | GUI for SQL execution, schema design, and data inspection              |
| 🐍 Programming    | Python (`pandas`, `psycopg2`)                  | Data cleaning, PostgreSQL connection, and CSV automation               |
| 📓 Notebooks      | Jupyter Notebook                               | Data preprocessing and KPI automation in interactive format            |
| 📄 Query Language | SQL                                            | Core logic for solving all 20 business KPIs                            |
| 📈 Visualization  | ERD with `dbdiagram.io`                        | Entity relationship mapping of fact/dimension healthcare schema        |

---


---

## 📁 Folder Structure

<details>
  <summary>📁 <strong>us_healthcare_sql_analysis/</strong> – Click to expand</summary>

📂 data/  
├── 📄 datasets/ — Raw healthcare CSV files  
├── 📄 outputs/ — Cleaned data after preprocessing  

📂 database/  
├── 📜 Defining_Tables.sql — SQL schema with constraints and relationships  
├── 🐍 Load_Data_Scripts.py — Bulk PostgreSQL loader using psycopg2  

📂 notebooks/  
├── 📓 1_data_cleaning.ipynb — Clean and export raw CSVs  
├── 📓 2_eda_analysis.ipynb — Null checks and data exploration  
├── 📓 3_sql_query_runner.ipynb — Dynamic SQL execution and result export  

📂 business_problems_outcomes/  
├── 🧠 01_top_cpt_costs.sql — KPI SQL queries (20 total)  
├── 📄 result_01_top_cpt_costs.csv — Results via pgAdmin  

📂 outputs/  
├── 📄 csvs/ — SQL outputs via Python automation  

📂 diagrams/  
├── 🖼️ ERD_Health_Analytics.png — Entity-Relationship Diagram  

📘 README.md — Project documentation  
</details>

---

## 🧩 Entity Relationship Diagram (ERD)

This ERD illustrates the **star schema** used to model healthcare claims and billing data in PostgreSQL. The central `facttable` connects to multiple dimension tables, enabling efficient joins and analytical flexibility for KPI computation.

### 🗃️ Fact Table

- **`facttable`** — Core transactional table containing:
  - Foreign keys to all dimension tables (e.g., `dimPatientPK`, `dimDateServicePK`, `dimCPTCodePK`)
  - Medical and billing fields like `CPTUnits`, `Gross_Expenses`, `Insurance_Payment`, `Patient_Payment`, `Adjustment`, `AR`

### 🧩 Dimension Tables

- **`dimpatient`** — Patient-level details (name, gender, age, state, region)
- **`dimpayer`** — Insurance provider information
- **`dimphysician`** — Physician metadata (NPI, name, specialty, FTE)
- **`dimspeciality`** — Specialization types with descriptive fields
- **`dimdate`** — Date reference with breakdowns by year, month, weekday
- **`dimtransaction`** — Claim transaction types and adjustment reasons
- **`dimcptcode`** — CPT codes, descriptions, and groupings for procedure classification
- **`dimdiagnosiscode`** — Diagnosis codes with grouping and descriptions
- **`dimhospital`** — Hospital or location data (`LocationName`)

> 🧠 This schema supports comprehensive healthcare analytics across cost, insurance coverage, readmissions, provider efficiency, and more — by enabling multi-dimensional aggregations.

📌 ERD created using: [dbdiagram.io](https://dbdiagram.io)  
📷 Schema diagram below:

![ERD Diagram](diagrams/ERD_Health_Analytics.png)

---


## 📊 Development Lifecycle

This project follows a 5-step data-to-insight pipeline — from raw CSV cleaning to SQL-powered business KPIs and dynamic exports via Python.

---

### 🧼 Step 1: Data Cleaning (`1_data_cleaning.ipynb`)

- Loaded all raw `.csv` files from `data/datasets/`
- Standardized column names to use underscores
- Replaced null values with `"NA"`
- Corrected invalid dates (e.g., `16-12-2019`) and numeric anomalies (`#NUM!`)
- Saved cleaned outputs to `data/outputs/`

---

### 📊 Step 2: Exploratory Data Analysis (`2_eda_analysis.ipynb`)

- Summary of missing/null values
- Unique ID validations and data integrity checks
- Distribution plots for gender, states, payers
- Verified foreign key relationships across all entities

---

### 🗃️ Step 3: PostgreSQL Schema & Data Loading

- **Schema Setup:** [`Defining_Tables.sql`](database/Defining_Tables.sql)  
  Defined relational schema with constraints and normalized tables.

- **Data Load:** [`Load_Data_Scripts.py`](database/Load_Data_Scripts.py)  
  Automatically loads cleaned `.csv` files into PostgreSQL using `psycopg2` with status logging.

---

### 🧠 Step 4: Solving 20 Business KPIs

We created 20 SQL-based KPIs to answer key healthcare business questions — ranging from cost efficiency to insurance coverage and claim delays.

Each KPI includes:

- 🎯 Objective  
- 🧾 SQL query file  
- 📁 Output CSV via **pgAdmin** and **Python**

| KPI No. | KPI Title                                      | Objective                                                                 | SQL Query File                                                                                  | CSV via pgAdmin                                                                                      | CSV via Python                                                                                     |
|--------:|------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| 1       | Top CPT Codes by Total Expenses                | Identify high-cost services and their contribution                        | [01_top_cpt_costs.sql](business_problems_outcomes/01_top_cpt_costs.sql)                         | [result_01_top_cpt_costs.csv](business_problems_outcomes/result_01_top_cpt_costs.csv)           | [result_01_top_cpt_costs.csv](outputs/csvs/result_01_top_cpt_costs.csv)                           |
| 2       | Avg Insurance Payment by Payer                 | Track average insurance payments and coverage %                           | [02_avg_insurance_coverage.sql](business_problems_outcomes/02_avg_insurance_coverage.sql)       | [result_02_avg_insurance_coverage.csv](business_problems_outcomes/result_02_avg_insurance_coverage.csv) | [result_02_avg_insurance_coverage.csv](outputs/csvs/result_02_avg_insurance_coverage.csv)         |
| 3       | Insurance vs Out-of-Pocket Ratio              | Understand cost split between insurance and patients                      | [03_insurance_vs_oop_ratio.sql](business_problems_outcomes/03_insurance_vs_oop_ratio.sql)                                 | [result_03_insurance_vs_oop_ratio.csv](business_problems_outcomes/result_03_insurance_vs_oop_ratio.csv)                   | [result_03_insurance_vs_oop_ratio.csv](outputs/csvs/result_03_insurance_vs_oop_ratio.csv)                                   |
| 4       | Patients Without Insurance Payment             | Count self-pay cases and % out-of-pocket                                  | [04_patients_without_insurance.sql](business_problems_outcomes/04_patients_without_insurance.sql)                     | [result_04_patients_without_insurance.csv](business_problems_outcomes/result_04_patients_without_insurance.csv)       | [result_04_patients_without_insurance.csv](outputs/csvs/result_04_patients_without_insurance.csv)                       |
| 5       | Payers with Most Claims but Least Payment      | Detect low-paying high-claim insurers                                    | [05_payers_most_claims_least_payment.sql](business_problems_outcomes/05_payers_most_claims_least_payment.sql)                 | [result_05_payers_most_claims_least_payment.csv](business_problems_outcomes/result_05_payers_most_claims_least_payment.csv)   | [result_05_payers_most_claims_least_payment.csv](outputs/csvs/result_05_payers_most_claims_least_payment.csv)                   |
| 6       | Avg Patient Payment by State                   | Patient out-of-pocket average by geography                                | [06_avg_patient_payment_by_state.sql](business_problems_outcomes/06_avg_patient_payment_by_state.sql) | [result_06_avg_patient_payment_by_state.csv](business_problems_outcomes/result_06_avg_patient_payment_by_state.csv) | [business_problems_outcomes/result_06_avg_patient_payment_by_state.csv](outputs/csvs/result_06_avg_patient_payment_by_state.csv)   |
| 7       | Avg Claim Cost by Gender                       | Understand cost difference across genders                                 | [07_avg_claim_cost_by_gender.sql](business_problems_outcomes/07_avg_claim_cost_by_gender.sql)                     | [result_07_avg_claim_cost_by_gender.csv](business_problems_outcomes/result_07_avg_claim_cost_by_gender.csv)       | [result_07_avg_claim_cost_by_gender.csv](outputs/csvs/result_07_avg_claim_cost_by_gender.csv)                       |
| 8       | Top 5 States by OOP %                          | Find states with highest out-of-pocket burden                             | [08_top_states_by_oop_percent.sql](business_problems_outcomes/08_top_states_by_oop_percent.sql)                       | [result_08_top_oop_states.csv](business_problems_outcomes/result_08_top_states_by_oop_percent.csv)         | [result_08_top_oop_states.csv](outputs/csvs/result_08_top_states_by_oop_percent.csv)                         |
| 9       | Readmission Detection                          | Track multiple hospital visits per patient                                | [09_readmission_detection.sql](business_problems_outcomes/09_readmission_detection.sql)                           | [result_09_readmission_detection.csv](business_problems_outcomes/result_09_readmission_detection.csv)             | [result_09_readmission_detection.csv](outputs/csvs/result_09_readmission_detection.csv)                             |
| 10      | Monthly Claim Trend                            | Observe claim trends over time                                            | [10_monthly_claim_trend.sql](business_problems_outcomes/10_monthly_claim_trend.sql)             | [result_10_monthly_claim_trend.csv](business_problems_outcomes/result_10_monthly_claim_trend.csv) | [result_10_monthly_claim_trend.csv](outputs/csvs/result_10_monthly_claim_trend.csv)               |
| 11      | Physician Efficiency (Cost/Patient)            | Measure cost-efficiency per physician                                     | [11_physician_cost_efficiency.sql](business_problems_outcomes/11_physician_cost_efficiency.sql)           | [result_11_physician_cost_efficiency.csv](business_problems_outcomes/result_11_physician_cost_efficiency.csv) | [result_11_physician_cost_efficiency.csv](outputs/csvs/result_11_physician_cost_efficiency.csv)             |
| 12      | Claim Volume by Specialty                      | Analyze claim frequency by medical specialty                              | [12_claim_volume_by_specialty.sql](business_problems_outcomes/12_claim_volume_by_specialty.sql)       | [result_12_claim_volume_by_specialty.csv](business_problems_outcomes/result_12_claim_volume_by_specialty.csv) | [result_12_claim_volume_by_specialty.csv](outputs/csvs/result_12_claim_volume_by_specialty.csv)         |
| 13      | Top 5 Expensive Specialties                    | Identify costly specialties in terms of expenses                          | [13_top_expensive_specialties.sql](business_problems_outcomes/13_top_expensive_specialties.sql) | [result_13_top_expensive_specialties.csv](business_problems_outcomes/result_13_top_expensive_specialties.csv) | [result_13_top_expensive_specialties.csv](outputs/csvs/result_13_top_expensive_specialties.csv)   |
| 14      | Diagnosis Groups by Volume + Avg AR            | Rank diagnosis groups and their avg AR                                    | [14_diagnosis_claim_volume_avg_ar.sql](business_problems_outcomes/14_diagnosis_claim_volume_avg_ar.sql)             | [result_14_diagnosis_claim_volume_avg_ar.csv](business_problems_outcomes/result_14_diagnosis_claim_volume_avg_ar.csv) | [result_14_diagnosis_claim_volume_avg_ar.csv](outputs/csvs/result_14_diagnosis_claim_volume_avg_ar.csv)               |
| 15      | Top 10 Diagnosis by AR                         | Identify diagnoses with highest average account receivable                | [15_top_diagnosis_by_highest_ar.sql](business_problems_outcomes/15_top_diagnosis_by_highest_ar.sql)                   | [result_15_top_diagnosis_by_highest_ar.csv](business_problems_outcomes/result_15_top_diagnosis_by_highest_ar.csv)     | [result_15_top_diagnosis_by_highest_ar.csv](outputs/csvs/result_15_top_diagnosis_by_highest_ar.csv)                     |
| 16      | Monthly Claims & Payout Trend                  | Track insurance and patient payment trend over months                     | [16_monthly_claims_payout_trend.sql](business_problems_outcomes/16_monthly_claims_payout_trend.sql)           | [result_16_monthly_claims_payout_trend.csv](business_problems_outcomes/result_16_monthly_claims_payout_trend.csv) | [result_16_monthly_claims_payout_trend.csv](outputs/csvs/result_16_monthly_claims_payout_trend.csv)             |
| 17      | Hospitals with Most Patients                   | Rank hospitals by patient volume and cost                                 | [17_top_hospitals_by_patients.sql](business_problems_outcomes/17_top_hospitals_by_patients.sql)                         | [result_17_top_hospitals_by_patients.csv](business_problems_outcomes/result_17_top_hospitals_by_patients.csv)           | [result_17_top_hospitals_by_patients.csv](outputs/csvs/result_17_top_hospitals_by_patients.csv)                           |
| 18      | Delayed Postings (Post > Service Date)         | Count late claim postings                                                 | [18_delayed_postings_count.sql](business_problems_outcomes/18_delayed_postings_count.sql)                   | [result_18_delayed_postings_count.csv](business_problems_outcomes/result_18_delayed_postings_count.csv)     | [result_18_delayed_postings_count.csv](outputs/csvs/result_18_delayed_postings_count.csv)                     |
| 19      | Avg CPT Units by Procedure Group               | Measure average units used per CPT group                                  | [19_avg_cpt_units_by_grouping.sql](business_problems_outcomes/19_avg_cpt_units_by_grouping.sql)                         | [result_19_avg_cpt_units_by_grouping.csv](business_problems_outcomes/result_19_avg_cpt_units_by_grouping.csv)           | [result_19_avg_cpt_units_by_grouping.csv](outputs/csvs/result_19_avg_cpt_units_by_grouping.csv)                           |
| 20      | Diagnosis with Most Adjustments                | See which diagnoses are most adjusted in billing                          | [20_diagnosis_with_most_adjustments.sql](business_problems_outcomes/20_diagnosis_with_most_adjustments.sql)         | [result_20_diagnosis_with_most_adjustments.csv](business_problems_outcomes/result_20_diagnosis_with_most_adjustments.csv) | [result_20_diagnosis_with_most_adjustments.csv](outputs/csvs/result_20_diagnosis_with_most_adjustments.csv)           |

---

## 🧪 Step 5: Run SQL Queries with Python

Notebook: [`3_sql_query_runner.ipynb`](notebooks/3_sql_query_runner.ipynb)

- Reads all `.sql` files in `business_problems_outcomes/`
- Connects to PostgreSQL database
- Executes each query dynamically
- Saves output result as `.csv` into `outputs/csvs/`

---

## 🚀 Run It Yourself

1. **Load Data to PostgreSQL**  
   Run: `python database/Load_Data_Scripts.py`

2. **Run KPIs**  
   Use either:
   - SQL in **pgAdmin** (manually)
   - Notebook: [`3_sql_query_runner.ipynb`](notebooks/3_sql_query_runner.ipynb)

3. **Check Results**  
   Output `.csv` files are saved in:
   - `business_problems_outcomes/` → via **pgAdmin**
   - `outputs/csvs/` → via **Python script**

---

## 📬 Project Summary & Conclusion

This project delivers a complete **healthcare analytics solution** powered by PostgreSQL, SQL, and Python — designed to transform raw claim data into actionable business insights.

It demonstrates:

- ✅ A fully normalized **PostgreSQL schema** supporting analytical joins and aggregations
- ✅ **20 real-world KPIs** solved using SQL — targeting cost trends, insurance coverage, payer behavior, readmissions, and provider performance
- ✅ Python-based **automation scripts** using `psycopg2` to run SQL queries and export results dynamically
- ✅ Clean and modular **Jupyter notebooks** for data cleaning, EDA, and SQL execution
- ✅ A reusable framework for generating **insights across multiple healthcare dimensions**

> 🚀 This end-to-end system reflects practical data engineering, query optimization, and healthcare domain application — making it both interview-ready and production-scalable.

---

## 📩 Contact

For questions or collaboration, feel free to connect:

- 💼 LinkedIn: [Harish Chowdary](https://www.linkedin.com/in/harish-chowdary)
- 🧑‍💻 GitHub: [Harish-34](https://github.com/Harish-34)























<!-- ### 🔍 Business KPI 1: Top CPT Codes by Total Expenses

**Objective:**  
Identify high-cost medical procedures based on total expense, average cost per unit, and cost contribution to overall healthcare spending.

**SQL File:**  
[business_problems_outcomes/01_top_cpt_costs.sql](business_problems_outcomes/01_top_cpt_costs.sql)

**Result CSV:**  
[business_problems_outcomes/result_01_top_cpt_costs.csv](business_problems_outcomes/result_01_top_cpt_costs.csv)


### 🔍 Business KPI 2: Avg Insurance Payment + Coverage % by Payer

**Objective:**  
Evaluate how much insurance companies are paying on average and how much of the treatment cost they cover.

**SQL File:**  
[business_problems_outcomes/02_avg_insurance_coverage.sql](business_problems_outcomes/02_avg_insurance_coverage.sql)

**Result CSV:**  
[business_problems_outcomes/result_02_avg_insurance_coverage.csv](business_problems_outcomes/result_02_avg_insurance_coverage.csv)


### 🔍 Business KPI 3: Insurance vs Out-of-Pocket Ratio

**Objective:**  
Compare total insurance contributions to what patients are paying out-of-pocket to understand cost burden.

**SQL File:**  
[business_problems_outcomes/03_insurance_vs_oop_ratio.sql](business_problems_outcomes/03_insurance_vs_oop_ratio.sql)

**Result CSV:**  
[business_problems_outcomes/result_03_insurance_vs_oop_ratio.csv](business_problems_outcomes/result_03_insurance_vs_oop_ratio.csv)


### 🔍 Business KPI 4: Patients Without Insurance Payment

**Objective:**  
Calculate how many healthcare claims had zero insurance coverage and determine how much of the total cost was paid out-of-pocket by patients.

**SQL File:**  
[business_problems_outcomes/04_patients_without_insurance.sql](business_problems_outcomes/04_patients_without_insurance.sql)

**Result CSV:**  
[business_problems_outcomes/result_04_patients_without_insurance.csv](business_problems_outcomes/result_04_patients_without_insurance.csv)


### 🔍 Business KPI 5: Payers with Most Claims but Least Payment

**Objective:**  
Spot payers that process the highest volume of claims but contribute the least in terms of insurance payouts.

**SQL File:**  
[business_problems_outcomes/05_payers_most_claims_least_payment.sql](business_problems_outcomes/05_payers_most_claims_least_payment.sql)

**Result CSV:**  
[business_problems_outcomes/result_05_payers_most_claims_least_payment.csv](business_problems_outcomes/result_05_payers_most_claims_least_payment.csv)


### 🔍 Business KPI 6: Avg Patient Payment by State

**Objective:**  
Evaluate how average out-of-pocket payments vary by state to detect regional financial trends and affordability issues.

**SQL File:**  
[business_problems_outcomes/06_avg_patient_payment_by_state.sql](business_problems_outcomes/06_avg_patient_payment_by_state.sql)

**Result CSV:**  
[business_problems_outcomes/result_06_avg_patient_payment_by_state.csv](business_problems_outcomes/result_06_avg_patient_payment_by_state.csv)


### 🔍 Business KPI 7: Avg Claim Cost by Gender

**Objective:**  
Identify any cost variation in healthcare claims between different gender groups, helping highlight potential inequalities or risk trends.

**SQL File:**  
[business_problems_outcomes/07_avg_claim_cost_by_gender.sql](business_problems_outcomes/07_avg_claim_cost_by_gender.sql)

**Result CSV:**  
[business_problems_outcomes/result_07_avg_claim_cost_by_gender.csv](business_problems_outcomes/result_07_avg_claim_cost_by_gender.csv)


### 🔍 Business KPI 8: Top 5 States by Out-of-Pocket %

**Objective:**  
Identify states where patients bear the highest percentage of healthcare costs, indicating regions with higher out-of-pocket burdens.

**SQL File:**  
[business_problems_outcomes/08_top_states_by_oop_percent.sql](business_problems_outcomes/08_top_states_by_oop_percent.sql)

**Result CSV:**  
[business_problems_outcomes/result_08_top_states_by_oop_percent.csv](business_problems_outcomes/result_08_top_states_by_oop_percent.csv)


### 🔍 Business KPI 9: Readmission Detection (Multiple Visits)

**Objective:**  
Detect patients with multiple visits to assess potential readmission patterns, which may signal chronic issues or care gaps.

**SQL File:**  
[business_problems_outcomes/09_readmission_detection.sql](business_problems_outcomes/09_readmission_detection.sql)

**Result CSV:**  
[business_problems_outcomes/result_09_readmission_detection.csv](business_problems_outcomes/result_09_readmission_detection.csv)


### 🔍 Business KPI 10: Monthly Claim Trend

**Objective:**  
Analyze how healthcare claim volumes and expenses change over time, month by month.

**SQL File:**  
[business_problems_outcomes/10_monthly_claim_trend.sql](business_problems_outcomes/10_monthly_claim_trend.sql)

**Result CSV:**  
[business_problems_outcomes/result_10_monthly_claim_trend.csv](business_problems_outcomes/result_10_monthly_claim_trend.csv)


### 🔍 Business KPI 11: Physician Efficiency (Cost per Patient)

**Objective:**  
Determine cost effectiveness of physicians based on how much is spent per patient treated.

**SQL File:**  
[business_problems_outcomes/11_physician_cost_efficiency.sql](business_problems_outcomes/11_physician_cost_efficiency.sql)

**Result CSV:**  
[business_problems_outcomes/result_11_physician_cost_efficiency.csv](business_problems_outcomes/result_11_physician_cost_efficiency.csv)


### 🔍 Business KPI 12: Claim Volume by Specialty

**Objective:**  
Track how many claims are submitted under each physician specialty to understand workload and demand.

**SQL File:**  
[business_problems_outcomes/12_claim_volume_by_specialty.sql](business_problems_outcomes/12_claim_volume_by_specialty.sql)

**Result CSV:**  
[business_problems_outcomes/result_12_claim_volume_by_specialty.csv](business_problems_outcomes/result_12_claim_volume_by_specialty.csv)


### 🔍 Business KPI 13: Top 5 Expensive Specialties

**Objective:**  
Identify the top medical specialties that account for the highest total gross healthcare expenses.

**SQL File:**  
[business_problems_outcomes/13_top_expensive_specialties.sql](business_problems_outcomes/13_top_expensive_specialties.sql)

**Result CSV:**  
[business_problems_outcomes/result_13_top_expensive_specialties.csv](business_problems_outcomes/result_13_top_expensive_specialties.csv)


### 🔍 Business KPI 14: Diagnosis Groups by Claim Volume + Avg AR

**Objective:**  
Analyze which diagnosis groups are most frequently claimed and observe their average AR levels for payment risk profiling.

**SQL File:**  
[business_problems_outcomes/14_diagnosis_claim_volume_avg_ar.sql](business_problems_outcomes/14_diagnosis_claim_volume_avg_ar.sql)

**Result CSV:**  
[business_problems_outcomes/result_14_diagnosis_claim_volume_avg_ar.csv](business_problems_outcomes/result_14_diagnosis_claim_volume_avg_ar.csv)


### 🔍 Business KPI 15: Top 10 Diagnosis by Highest AR

**Objective:**  
Identify diagnosis groups that are associated with the highest average AR (Accounts Receivable), which helps in recognizing categories with slower or riskier payments.

**SQL File:**  
[business_problems_outcomes/15_top_diagnosis_by_highest_ar.sql](business_problems_outcomes/15_top_diagnosis_by_highest_ar.sql)

**Result CSV:**  
[business_problems_outcomes/result_15_top_diagnosis_by_highest_ar.csv](business_problems_outcomes/result_15_top_diagnosis_by_highest_ar.csv)


### 🔍 Business KPI 16: Monthly Claims & Payout Trend

**Objective:**  
Track monthly trends in total claim submissions and payouts (combined insurance and patient payments) to evaluate seasonal patterns and financial performance.

**SQL File:**  
[business_problems_outcomes/16_monthly_claims_payout_trend.sql](business_problems_outcomes/16_monthly_claims_payout_trend.sql)

**Result CSV:**  
[business_problems_outcomes/result_16_monthly_claims_payout_trend.csv](business_problems_outcomes/result_16_monthly_claims_payout_trend.csv)


### 🔍 Business KPI 17: Hospitals with Highest Patients

**Objective:**  
Identify which hospitals are handling the largest patient volumes and evaluate their contribution to total healthcare expenses.

**SQL File:**  
[business_problems_outcomes/17_top_hospitals_by_patients.sql](business_problems_outcomes/17_top_hospitals_by_patients.sql)

**Result CSV:**  
[business_problems_outcomes/result_17_top_hospitals_by_patients.csv](business_problems_outcomes/result_17_top_hospitals_by_patients.csv)


### 🔍 Business KPI 18: Delayed Postings (Post > Service Date)

**Objective:**  
Identify how many claims were posted after the service date, which may indicate administrative inefficiencies or reporting lags.

**SQL File:**  
[business_problems_outcomes/18_delayed_postings_count.sql](business_problems_outcomes/18_delayed_postings_count.sql)

**Result CSV:**  
[business_problems_outcomes/result_18_delayed_postings_count.csv](business_problems_outcomes/result_18_delayed_postings_count.csv)


### 🔍 Business KPI 19: Avg CPT Units by Procedure Type

**Objective:**  
Analyze the average number of CPT units billed for each procedure grouping to identify services with higher operational demand.

**SQL File:**  
[business_problems_outcomes/19_avg_cpt_units_by_grouping.sql](business_problems_outcomes/19_avg_cpt_units_by_grouping.sql)

**Result CSV:**  
[business_problems_outcomes/result_19_avg_cpt_units_by_grouping.csv](business_problems_outcomes/result_19_avg_cpt_units_by_grouping.csv)


### 🔍 Business KPI 20: Diagnosis with Most Adjustments

**Objective:**  
Identify diagnosis categories with the highest total financial adjustments, which may signal frequent billing corrections, denials, or anomalies.

**SQL File:**  
[business_problems_outcomes/20_diagnosis_with_most_adjustments.sql](business_problems_outcomes/20_diagnosis_with_most_adjustments.sql)

**Result CSV:**  
[business_problems_outcomes/result_20_diagnosis_with_most_adjustments.csv](business_problems_outcomes/result_20_diagnosis_with_most_adjustments.csv)

 -->
