# Twitter Data ETL Pipeline

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for extracting data from the Twitter API, processing it, and loading it into Amazon S3. The pipeline is orchestrated using Apache Airflow, and it runs on an Amazon EC2 instance.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Features
- Extract tweets and user data from the Twitter API.
- Transform data to clean and prepare it for analysis.
- Load processed data into Amazon S3 for storage and further analysis.

## Requirements
- Python 3.x
- Apache Airflow
- boto3 (AWS SDK for Python)
- tweepy (Twitter API client library)
- pandas (for data manipulation)

## Installation
1. **Clone the repository:**
   ```bash
   git clone twitter-airflow-data-engineering-project
   cd twitter-airflow-data-engineering-project
   ```

2. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Apache Airflow:**
   Follow the [Apache Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/install.html).

4. **Configure AWS Credentials:**
   Ensure you have your AWS credentials set up either in `~/.aws/credentials` or export them as environment variables.

## Usage
1. **Start the Airflow services:**
   ```bash
   airflow standalone
   airflow db init
   airflow webserver --port 8080
   airflow scheduler
   ```

2. **Access the Airflow UI:**
   Open a web browser and go to `http://localhost:8080`. You can enable and trigger the DAG that orchestrates the ETL process.

3. **Extract Twitter Data:**
   The pipeline will fetch tweets based on specified parameters using the Twitter API.

4. **Data Processing and Loading:**
   Processed data will be automatically uploaded to your specified Amazon S3 bucket.

## Configuration
- Modify the configuration settings in `twitter_dag.py` to customize your DAG, such as setting up the Twitter API keys, S3 bucket name, etc.
- Update the parameters in `twitter_etl.py` as needed for your data extraction and transformation logic.

## License
