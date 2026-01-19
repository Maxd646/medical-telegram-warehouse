from dagster import asset, Definitions
import subprocess

@asset
def telegram_scrape():
    subprocess.run(["python", "src/scraper.py"], check=True)

@asset(deps=[telegram_scrape])
def raw_to_postgres():
    subprocess.run(["python", "scripts/db_setup.py"], check=True)

@asset(deps=[raw_to_postgres])
def dbt_transform():
    subprocess.run(["dbt", "run"], cwd="medical_warehouse", check=True)
    subprocess.run(["dbt", "test"], cwd="medical_warehouse", check=True)

@asset(deps=[dbt_transform])
def yolo_enrichment():
    subprocess.run(["python", "src/yolo_detect.py"], check=True)

defs = Definitions(
    assets=[telegram_scrape, raw_to_postgres, dbt_transform, yolo_enrichment]
)
