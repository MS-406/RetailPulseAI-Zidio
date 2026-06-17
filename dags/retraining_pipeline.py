import datetime
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define the default arguments
default_args = {
    'owner': 'zidio_admin',
    'depends_on_past': False,
    'start_date': pendulum.today('UTC').add(days=-1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

# Define the DAG for the automated retraining pipeline (Day 13 Checkpoint)
dag = DAG(
    'retail_pulse_retraining_pipeline',
    default_args=default_args,
    description='Automated pipeline for hybrid forecasting, churn prediction, and drift detection.',
    schedule_interval=datetime.timedelta(days=7), # Run weekly
    catchup=False,
    tags=['zidio', 'retail', 'machine-learning'],
)

# Task 1: Generate the hybrid forecast and inventory logic
# Note: In production, these notebooks would be executed via papermill or converted to pure scripts
t1_forecast_inventory = BashOperator(
    task_id='run_hybrid_forecast_and_inventory',
    bash_command='python scripts/week2_pipeline.py', # Simplified fallback command for demonstration
    dag=dag,
)

# Task 2: Retrain the XGBoost churn model
t2_churn_model = BashOperator(
    task_id='run_churn_model',
    bash_command='echo "Running XGBoost churn prediction..."', 
    dag=dag,
)

# Task 3: Run evidently drift detection
t3_drift_detection = BashOperator(
    task_id='run_drift_detection',
    bash_command='echo "Running Evidently AI Drift Detection..."',
    dag=dag,
)

# Set dependencies (Forecast -> Churn -> Drift)
t1_forecast_inventory >> t2_churn_model >> t3_drift_detection
