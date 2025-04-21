
import boto3
import os
import hashlib
from pathlib import Path
from datetime import datetime

# AWS and S3 configuration
BUCKET_NAME = 'technical-analysis-data' 
PROFILE_NAME = 'data-pipeline'
BASE_DIR = Path(__file__).resolve().parent          # /opt/airflow/data_ingestion
PRICE_DIR = BASE_DIR / "output" / "prices"
FUND_DIR  = BASE_DIR / "output" / "fundamentals"
LOG_FILE  = BASE_DIR / "output" / "upload_log.txt"

# Setup session using AWS CLI profile
session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
)
s3 = session.client('s3')

def compute_hash(file_path):
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def read_log():
    """Read log into a dict: {filename: hash}"""
    if not LOG_FILE.exists():
        return {}
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
    return dict(line.strip().split('\t')[:2] for line in lines)

def write_log(file_path, file_hash):
    with open(LOG_FILE, 'a') as log:
        log.write(f"{file_path.name}\t{file_hash}\t{datetime.now().isoformat()}\n")

def upload_file(file_path, s3_folder, uploaded_log):
    file_hash = compute_hash(file_path)
    if uploaded_log.get(file_path.name) == file_hash:
        print(f"⏩ Skipping {file_path.name}, content unchanged.")
        return
    s3_key = f"{s3_folder}/{file_path.name}"
    try:
        s3.upload_file(str(file_path), BUCKET_NAME, s3_key)
        print(f"✅ Uploaded: {file_path.name} → s3://{BUCKET_NAME}/{s3_key}")
        write_log(file_path, file_hash)
    except Exception as e:
        print(f"❌ Failed to upload {file_path.name}: {e}")

def upload_all_files():
    uploaded_log = read_log()
    for file in PRICE_DIR.glob("*.csv"):
        upload_file(file, "prices", uploaded_log)
    for file in FUND_DIR.glob("*.json"):
        upload_file(file, "fundamentals", uploaded_log)

if __name__ == "__main__":
    upload_all_files()
