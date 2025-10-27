
---

```markdown
# 🧠 **PSDP Insight AI — Smart Project Efficiency Analyzer**

🚀 *URAAN AI Techathon 2025 – Governance & Public Sector Efficiency*  

---

## 🌐 **Live Applications**

👉 **Main EDA Dashboard (Lovable App):** [https://psdp-insight-dash.lovable.app/](https://psdp-insight-dash.lovable.app/)  
🤖 **AI Efficiency Predictor (Streamlit Model):** [https://ml-uraan-ap--8u2dggoffvk4m8mks4chku.streamlit.app/](https://ml-uraan-ap--8u2dggoffvk4m8mks4chku.streamlit.app/)

---

## 🏛️ **Project Overview**

The **Public Sector Development Programme (PSDP)** funds hundreds of national projects every year across Pakistan.  
However, inefficiencies, missing progress tracking, and non-transparent fund flows lead to wastage and delays.  

Our project — **PSDP Insight AI** — analyzes, visualizes, and predicts PSDP project efficiency using **real government data**, empowering policymakers with actionable, data-driven transparency.

---

## ⚠️ **Problem & Solution**

**Problem:**  
Corruption, inefficient budget utilization, and non-transparent fund flows reduce accountability and project impact.  

**Solution:**  
We built a transparent, data-driven system that visualizes PSDP fund flows, highlights anomalies, and uses AI to predict project efficiency for early risk detection.

---

## 💡 **Our Solution**

We manually extracted and verified **real PSDP 2024-25** data from official PDF reports using Python (`pdfplumber`).  
The dataset was authentic but inconsistent, requiring cleaning, feature engineering, and logic validation.

Then we developed two integrated modules:

### 1️⃣ **EDA Dashboard (Lovable App)**
Interactive analytical dashboard built in **Bolt/Lovable**, featuring:
- Five major data-driven charts.  
- Each chart includes **Interpretation + Recommendations**.  
- Summary metrics and statistical breakdown of PSDP 2024-25.  

### 2️⃣ **Baseline AI Model (Streamlit)**
An ML model that predicts if a project setup is *Efficient (1)* or *Inefficient (0)* based on key project metrics.

📊 **Example Inputs**
- Total Cost  
- Expenditure 2024  
- Allocation 2024-25  
- Throwforward 2025  
- Rupee Funding  
- Ministry  
- Project Type  
- Approval Year  

✅ The model returns **“Efficient” or “Inefficient”** with a confidence percentage.

---

## 🧮 **Dataset**

- **File:** `PSDP_2024_25_verified.csv`  
- **Source:** Extracted from official PSDP 2024-25 reports.  
- **Size:** ~1 000 projects  
- **Columns:**  
  `Project_Title`, `Total_Cost`, `Expenditure_2024`, `Throwforward_2025`, `Allocation_2024_25`, `Ministry`, `Type`, `Utilization%`, `Approval_Year`, etc.

---

## 📊 **Key EDA Charts + Insights**

### 1️⃣ Average Budget Utilization (%) by Ministry  
**Insight:** Ministries like *Law & Justice* and *Railways* exceed 150 % utilization, while others fall below 70 %.  
**Recommendations:**  
- Audit over-utilizing ministries.  
- Improve capacity in under-performing ones.  
- Implement quarterly performance reviews.

---

### 2️⃣ Budget Gap (Approved vs Actual Spending)  
**Insight:** Major under-spending observed in *Water Resources* and *Communication* Divisions.  
**Recommendations:**  
- Re-evaluate delayed projects.  
- Redirect surplus funds.  
- Establish transparent fund-tracking dashboards.

---

### 3️⃣ Budget Utilization by Project Type  
**Insight:** *Ongoing* projects average 139 % utilization; *New* projects only 10 %.  
**Recommendations:**  
- Strengthen feasibility before launching new projects.  
- Avoid multi-year carryovers.  
- Re-align funding to project maturity levels.

---

### 4️⃣ Funding Gap (Total Cost vs Annual Allocation)  
**Insight:** *Water Resources* and *National Heritage* ministries face > Rs 60 B funding shortfalls.  
**Recommendations:**  
- Break mega projects into annual phases.  
- Link allocations to milestone achievements.  
- Digitize cost vs allocation tracking.

---

### 5️⃣ Throwforward 2025 vs Allocation 2024-25  
**Insight:** Ratios exceeding 250 % show backlog stress for 2025.  
**Recommendations:**  
- Cap throwforward below 120 %.  
- Accelerate delayed projects.  
- Tie new allocations to verified physical progress.

---

## 🤖 **Machine Learning Model**

| Metric | Value | Meaning |
|:-------|:------|:--------|
| **Algorithm** | Random Forest Classifier | – |
| **Accuracy** | 0.917 | Excellent performance |
| **Precision (Efficient)** | 0.87 | Few false positives |
| **Recall (Inefficient)** | 0.97 | Detects nearly all inefficiencies |
| **F1-Score** | 0.88 | Balanced performance |

✅ Focused on **risk detection** — identifying potentially inefficient projects early.

---

## 🧩 **Project Structure**

```plaintext
PSDP/
│── 01_pdf_files/                      # Raw PDF data
│── 02_charts/                         # Generated chart HTML files
│── 03_psdp-insight-dash/              # Lovable/Bolt dashboard
│── 01_Extraction_of_Data_From_PDFs.ipynb
│── 02_Data_Cleaning.ipynb             # Cleaning + feature creation
│── 03_ML_Part.ipynb                   # ML model building
│── 04_dashboard.py                    # Streamlit predictor app
│── 05_EDA_Insights.ipynb              # EDA + chart code
│── PSDP_2024_25_verified.csv          # Cleaned dataset
│── psdp_efficiency_model.pkl          # Trained model
│── model_features.pkl                 # Feature structure
│── requirements.txt                   # Dependencies
│── README.md                          # Documentation
```

---

## 👥 **Team**

| Name                | Role                    | Responsibilities                       |
| :------------------ | :---------------------- | :------------------------------------- |
| **Maaz Umar** | Team Lead / ML Engineer | Data cleaning, ML model, Streamlit app |
| **Touseef**   | Data Visualization Lead | EDA charts, Lovable dashboard          |
| **Shawali**   | Documentation Lead      | Insights, recommendations, reporting   |

---

## 🌿 **Future Enhancements (Phase 2)**

**1️⃣ Access to Clean Classified Real Data**

We used real PSDP data but faced gaps and OCR issues. Access to verified classified datasets will yield more robust insights.

**2️⃣ Satellite & Geospatial Integration**

Combine satellite and geospatial data to verify project progress visually and track infrastructure changes.

**3️⃣ Enhanced AI Model**

Train an advanced model (e.g., XGBoost, Explainable AI) using multi-year data for better accuracy and interpretability.

**4️⃣ Automated Data Pipeline + Real-time API Link**

Automate PSDP PDF → CSV extraction and integrate live APIs for continuous fund tracking, anomaly detection, and progress analytics.

---

## 🏁 **Conclusion**

> *PSDP Insight AI bridges human-driven analysis with machine learning — fostering transparency, efficiency, and data-backed governance.*

Trained on verified **PSDP 2024-25** data, it establishes the foundation for **smarter, transparent, and accountable public-sector management in Pakistan.**

---

✅ *Developed by Team PSDP Insight AI — Maaz Umar | Touseef | Shawali*

📅 **Hackathon:** URAAN AI Techathon 2025

🌐 **Main Dashboard:** [psdp-insight-dash.lovable.app](https://psdp-insight-dash.lovable.app/)



```markdown
---

## ⚙️ **How to Run Locally**

Follow these steps to set up and run the PSDP Insight AI project on your local machine.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/psdp-insight-ai.git
cd psdp-insight-ai
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
conda create -n psdp_env python=3.10
conda activate psdp_env
```

*(or use `python -m venv venv` and `venv\Scripts\activate` on Windows)*

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the EDA Dashboard (Lovable / Bolt)

If you want to open the  **interactive visual dashboard** , upload your data and chart files to [Lovable](https://lovable.app/) or your Bolt workspace and run:

```bash
bolt dev
```

### 5️⃣ Run the AI Prediction App (Streamlit)

Launch the Machine Learning model locally:

```bash
streamlit run 04_dashboard.py
```

Once it runs successfully, open the provided **localhost link** in your browser (usually [http://localhost:8501](http://localhost:8501/)).
