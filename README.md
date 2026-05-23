Sales Data Pipeline

A complete data analysis pipeline built with Python and pandas using the April 2019 sales dataset.

This project demonstrates a professional data workflow including:

data cleaning
type conversion
feature engineering
KPI computation
CSV export
data visualization with matplotlib

The goal of this project is to simulate a real-world business data analysis workflow similar to what can be found in data-oriented internships and junior data analyst positions.

Project Structure

sales-data-pipeline/

├── data/
│ └── Sales_April_2019.csv

├── output/
│ ├── revenue_by_city.csv
│ ├── revenue_by_hour.csv
│ ├── revenue_by_month.csv
│ ├── revenue_by_product.csv
│ ├── product_sold_by_hour.csv
│ ├── top_product.csv

├── plots/
│ ├── revenue_by_city.png
│ ├── revenue_by_hour.png
│ ├── revenue_by_product.png
│ ├── product_sold_by_hour.png
│ ├── top_product.png

├── sales_pipeline.py
├── requirements.txt
└── README.md

Features
Data Cleaning
Removes empty rows
Removes duplicated header rows
Converts columns to appropriate data types
Handles invalid values using errors="coerce"
Feature Engineering

The pipeline creates additional business-oriented columns:

Revenue
Hour
Month
City
KPI Analysis

The following KPIs are computed:

Total revenue
Revenue by city
Revenue by hour
Revenue by month
Revenue by product
Quantity sold by hour
Top-selling products
Best sales hour
Best sales month
Best sales city
Best-selling product
Visualization

The project automatically generates graphs with matplotlib:

Bar charts
Line charts
Product performance analysis
Revenue evolution graphs
Installation

Install dependencies:

pip install -r requirements.txt

Usage

Run the pipeline with:

python sales_pipeline.py

Technologies Used
Python
pandas
matplotlib
Learning Objectives

This project was built to practice:

professional pandas workflows
business-oriented data analysis
KPI generation
automation pipelines
data visualization
