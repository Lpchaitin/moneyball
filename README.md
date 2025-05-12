# 🧢 Moneyball 2.0: ROI Analysis in MLB

## 🧰 Tech Stack
- **Python** – Data scraping, cleaning, and loading
- **SQL** – Analysis and modeling in PostgreSQL
- **AWS RDS (PostgreSQL)** – Cloud-hosted relational database
- **GitHub Actions** – Automated ETL pipelines with papermill
- **Looker Studio** – Final dashboard visualizations
- **DBT** – Data transformations and modeling
- **Jupyter Notebooks** – Data exploration and scripting

## 🎯 Project Objective
This project helps **MLB front offices, analysts, and GMs** identify **how efficiently teams convert payroll into wins**.

- **Problem**: Many teams spend excessively without playoff results
- **Solution**: Analyze ROI (Wins / Payroll) using historical and financial data
- **Goal**: Inform smarter roster investments using data

## 💼 Job Description
This project is aligned with a **Data Scientist role at FanDuel (Jersey City, NJ)** focused on predictive modeling, reporting automation, and business performance analytics.

It directly connects through:
- Use of SQL + Python + Looker
- ROI modeling and sports-focused KPIs
- Data storytelling for business impact

📎 [View Job Description PDF](proposal/job_description.pdf)

## 📦 Data

### Sources
- [Kaggle: MLB Team Payrolls](https://www.kaggle.com/datasets/christophertreasure/mlb-team-payrolls-2011-2024)
- [Baseball Reference Standings](https://www.baseball-reference.com/leagues/MLB/)

### Characteristics
- Time Range: 2011–2024
- Metrics: Wins, Losses, Payroll, Avg Age, Win %, GB
- Raw → Cleaned → Merged in `sql_project` schema

## 📓 Notebooks / Scripts

| File | Purpose |
|------|---------|
| [`notebooks/Kaggle_API_Extract_Load_Raw.ipynb`](notebooks/Kaggle_API_Extract_Load_Raw.ipynb) | Load and clean payroll data from Kaggle |
| [`notebooks/BaseballReference_Web_Scrape_Extract_Load_Raw.ipynb`](notebooks/BaseballReference_Web_Scrape_Extract_Load_Raw.ipynb) | Scrape win/loss data from Baseball Reference |
| [`notebooks/Kaggle_API_SQL_Analysis.ipynb`](notebooks/Kaggle_API_SQL_Analysis.ipynb) | Run SQL queries to analyze payroll data |
| [`notebooks/Team_Payroll_SQL_Analysis.ipynb`](notebooks/Team_Payroll_SQL_Analysis.ipynb) | Join and visualize ROI metrics |

## 🔮 Future Improvements
- Add **player-level salary + WAR** data to model individual ROI
- Integrate **real-time data pipelines** and predictive season forecasting

## Link To Looker Dashboard
[🔍 View Interactive Looker Dashboard](https://lookerstudio.google.com/reporting/3a360374-8f25-4fe0-b92f-341612d21d25/page/p_x0z6ek58rd)

---
> *This project was created as part of the SQL Portfolio to demonstrate data engineering and analytics skills in a real-world scenario.*
