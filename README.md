# \# sales-data-pipeline

# 

# A complete data analysis pipeline built with Python and pandas using the April 2019 sales dataset.

# 

# This project demonstrates a professional data workflow including:

# 

# \* data cleaning,

# \* type conversion,

# \* feature engineering,

# \* KPI computation,

# \* CSV export,

# \* data visualization with matplotlib.

# 

# The goal of this project is to simulate a real-world business data analysis workflow similar to what can be found in data-oriented internships and junior data analyst positions.

# 

# \---

# 

# \# Project Structure

# 

# sales-data-pipeline/

# │

# ├── data/

# │   └── Sales\_April\_2019.csv

# │

# ├── output/

# │   ├── revenue\_by\_city.csv

# │   ├── revenue\_by\_hour.csv

# │   ├── revenue\_by\_month.csv

# │   ├── revenue\_by\_product.csv

# │   ├── product\_sold\_by\_hour.csv

# │   ├── top\_product.csv

# │

# ├── plots/

# │   ├── revenue\_by\_city.png

# │   ├── revenue\_by\_hour.png

# │   ├── revenue\_by\_product.png

# │   ├── product\_sold\_by\_hour.png

# │   ├── top\_product.png

# │

# ├── sales\_pipeline.py

# ├── requirements.txt

# └── README.md

# 

# \---

# 

# \# Features

# 

# \## Data Cleaning

# 

# \* Removes empty rows

# \* Removes duplicated header rows

# \* Converts columns to appropriate data types

# \* Handles invalid values with `errors="coerce"`

# 

# \## Feature Engineering

# 

# The pipeline creates additional business-oriented columns:

# 

# \* Revenue

# \* Hour

# \* Month

# \* City

# 

# \## KPI Analysis

# 

# The following KPIs are computed:

# 

# \* Total revenue

# \* Revenue by city

# \* Revenue by hour

# \* Revenue by month

# \* Revenue by product

# \* Quantity sold by hour

# \* Top-selling products

# \* Best sales hour

# \* Best sales month

# \* Best sales city

# \* Best-selling product

# 

# \## Data Export

# 

# The pipeline automatically exports:

# 

# \* cleaned datasets,

# \* KPI tables,

# \* generated visualizations.

# 

# \## Visualization

# 

# The project generates professional graphs using matplotlib:

# 

# \* bar charts,

# \* line charts,

# \* sales evolution graphs,

# \* product performance analysis.

# 

# \---

# 

# \# Installation

# 

# Install the required dependencies:

# 

# pip install -r requirements.txt

# 

# \---

# 

# \# Requirements

# 

# requirements.txt content:

# 

# pandas

# matplotlib

# 

# \---

# 

# \# Usage

# 

# Run the pipeline with:

# 

# python sales\_pipeline.py

# 

# \---

# 

# \# Dataset

# 

# Dataset used:

# 

# April Sales 2019 Dataset from Kaggle.

# 

# Columns:

# 

# \* Order ID

# \* Product

# \* Quantity Ordered

# \* Price Each

# \* Order Date

# \* Purchase Address

# 

# \---

# 

# \# Technologies Used

# 

# \* Python

# \* pandas

# \* matplotlib

# \* CSV data processing

# 

# \---

# 

# \# Example Workflow

# 

# 1\. Load raw CSV data

# 2\. Clean invalid rows

# 3\. Convert data types

# 4\. Enrich dataset with business features

# 5\. Compute KPIs

# 6\. Export CSV reports

# 7\. Generate graphs automatically

# 

# \---

# 

# \# Learning Objectives

# 

# This project was built to practice:

# 

# \* professional pandas workflows,

# \* business-oriented data analysis,

# \* automation pipelines,

# \* KPI generation,

# \* data visualization.

