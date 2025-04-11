# technical-analysis-pipeline
Stock market tracker with real-time processing and technical analysis features
---

## 🔍 Why This Project?

After years of working across data, product, and growth — and having moved between countries and tech stacks — I wanted to create something that ties together my passions: market behavior, clean data systems, and personal growth through technical challenge.

This project is my 20-day challenge: to build a real-time technical analysis pipeline from scratch using the same tools modern data teams use to ship value at scale.

This repository serves as a **learning lab**, a **showcase**, and a **documentation hub** for that process.

---

## ⚙️ What This Project Does

At its core, this project ingests raw stock data from public APIs, processes it using Apache Spark and Kafka, enriches it with technical indicators (RSI, MACD, EMA, etc.), and outputs actionable insights via dashboards and alerts.

**Key functionalities:**
- ✅ Ingest stock price data from external APIs
- ✅ Store versioned data in AWS S3
- ✅ Stream and process data with Apache Kafka + Spark
- ✅ Calculate technical indicators using Python
- ✅ Feed the output into a basic ML model (Buy/Sell/Hold)
- ✅ Store predictions in a database
- ✅ Visualize outputs with Grafana
- ✅ Send alerts via Telegram bot

This project is **not for trading advice**, but to demonstrate **data engineering, modeling, automation, and DevOps fluency** — all in an end-to-end architecture.

---

## 🛠️ Tech Stack

| Area            | Tools/Tech                     |
|-----------------|-------------------------------|
| Data ingestion  | Python, REST API               |
| Storage         | AWS S3                         |
| Stream handling | Apache Kafka                   |
| ETL Processing  | Apache Spark                   |
| Feature Logic   | pandas, TA-lib, Python math    |
| ML Pipeline     | scikit-learn, XGBoost (TBD)    |
| Dashboarding    | Grafana, PostgreSQL/SQLite     |
| Alerts          | Telegram API                   |
| Infra           | Docker, Kubernetes (stretch)   |
| DevOps          | GitHub Actions (CI/CD)         |

---

## 📚 How This Repo Is Structured

```plaintext
technical-analysis-pipeline/
├── data_ingestion/           # API fetching scripts
├── etl_pipeline/             # Kafka + Spark logic
├── indicators/               # Technical analysis feature logic
├── models/                   # ML scripts + outputs
├── dashboards/               # Grafana or reporting configs
├── alerts/                   # Telegram integration
├── uml/                      # Architecture diagrams
├── notebooks/                # Prototypes and testing
├── README.md                 # You're here!
├── LICENSE.txt               # CC-BY-NC-ND license
├── requirements.txt          # Python dependencies

🧭 Want to Know More?
I'm documenting the full build process publicly on Substack. (https://guidopederiva.substack.com)
I share what works, what breaks, and what I learn each step of the way.

👉 Follow the build journey on Substack
💼 Connect with me on LinkedIn

If you're curious, building something similar, or just want to say hi — I'd love to connect.

📄 License
This project is published under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
You're free to view and share, but not modify or republish.

Guido Pederiva
Data Engineer | Product-Minded Builder | Eternal Learner
guidopede@gmail.com
