#!/bin/bash

echo "🔧 Running DB migration..."
airflow db migrate

echo "👤 Creating admin user..."
airflow users create \
  --username "${AIRFLOW_ADMIN_USERNAME}" \
  --firstname "${AIRFLOW_ADMIN_FIRSTNAME}" \
  --lastname "${AIRFLOW_ADMIN_LASTNAME}" \
  --role Admin \
  --password "${AIRFLOW_ADMIN_PASSWORD}" \
  --email "${AIRFLOW_ADMIN_EMAIL}"

echo "🚀 Starting Airflow webserver..."
exec airflow webserver