
## Shipping a Data Product: From Raw Telegram Data to an Analytical API

An end-to-end data platform for analyzing Ethiopian medical and pharmaceutical content on Telegram.  
This project transforms raw Telegram messages and images into enriched, analytics-ready data using **dbt**, **Dagster**, and **YOLOv8**, and serves insights through a **FastAPI** backend.

---

## Table of Contents
- Project Overview  
- Business Context  
- Objectives  
- Data & Features  
- Project Structure  
- Architecture  
- Pipeline & Processing Steps  
- Engineering Practices  
- Setup & Installation  
- Running the Project  
- Technologies Used  
- Author  

---

## Project Overview
**Medical Telegram Analytics** implements a full ELT pipeline tailored for Ethiopian medical and pharmaceutical Telegram channels.

The system covers the entire data lifecycle:
- Scraping messages and images from public Telegram channels  
- Storing raw data in a data lake and PostgreSQL warehouse  
- Transforming data into a dimensional star schema using dbt  
- Enriching image data with YOLOv8 object detection  
- Serving actionable insights via a FastAPI analytical API  

---

## Business Context
**Kara Solutions**, a leading data consultancy in Ethiopia, requires a scalable and reliable platform to monitor product trends, pricing signals, and visual marketing content across Telegram channels.

### Key Business Questions
- What are the top 10 most frequently mentioned medical products or drugs?  
- How do prices or availability vary across different channels?  
- Which channels publish the most visual content (e.g., pills vs. creams)?  
- What are the daily and weekly posting trends for health-related topics?  

---

## Objectives
- Build a reproducible, secure, and production-ready data pipeline  
- Extract Telegram messages and media into a raw data lake  
- Design and implement a dimensional star schema in PostgreSQL  
- Transform and validate data using dbt  
- Enrich images with YOLOv8-based object detection  
- Expose analytics via a FastAPI service  
- Orchestrate the pipeline using Dagster  
- Ensure reproducibility and versioning with DVC  

---

## Data & Features

### Telegram Channels Scraped
- **CheMed** – Medical products  
- **Lobelia Cosmetics** – Cosmetics & health products  
- **Tikvah Pharma** – Pharmaceuticals  
- Additional channels sourced from *et.tgstat.com/medicine*  

### Raw Data Fields
| Column | Description |
|------|-------------|
| message_id | Unique message identifier |
| channel_name | Telegram channel name |
| message_date | Message timestamp |
| message_text | Full message content |
| has_media | Media presence flag |
| image_path | Local path to downloaded image |
| views | View count |
| forwards | Forward count |

### Derived Features
- Message length and content flags  
- YOLOv8-based image categories: *promotional*, *product_display*, *lifestyle*, *other*  
- Aggregated metrics by channel and time period  

---

## Project Structure
```text
medical-telegram-analytics/
├── config/
├── data/
├── logs/
├── notebooks/
├── scripts/
├── src/
├── api/
├── dbt/
├── orchestration/
├── tests/
├── docker/
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── .env
└── README.md
```

---

## Architecture
Telegram Channels → Scraper → Raw Data Lake → PostgreSQL + dbt → YOLOv8 → FastAPI → Users

---

## Pipeline & Processing Steps
1. **Scraping:** Telethon extracts messages and images  
2. **Transformation:** dbt cleans and models data into star schema  
3. **Enrichment:** YOLOv8 detects and classifies image content  
4. **Serving:** FastAPI exposes analytical endpoints  
5. **Orchestration:** Dagster automates the full pipeline  

---

## Engineering Practices
- Reproducibility with DVC  
- Containerization with Docker  
- Automated testing with Pytest  
- Centralized logging and monitoring  

---

## Setup & Installation
```bash
git clone https://github.com/<username>/medical-telegram-analytics.git
cd medical-telegram-analytics
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

---

## Running the Project
```bash
dvc repro
```

API Docs: http://localhost:8000/docs

---

## Technologies Used
Python, PostgreSQL, dbt, YOLOv8, FastAPI, Dagster, DVC, Docker, Telethon, Pytest

---

## Author
**Kebede G. Daniel**
