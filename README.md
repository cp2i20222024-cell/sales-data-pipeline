# Sales Data Pipeline

Python data analysis pipeline built with **pandas** and **matplotlib** using the April 2019 sales dataset.

This project simulates a real-world business data workflow commonly found in junior data analyst and business intelligence positions.

---

## Features

### Data Cleaning

- Removes empty rows
- Removes duplicated header rows
- Converts columns to proper data types
- Handles invalid values with `errors="coerce"`

### Feature Engineering

The pipeline automatically creates new business-oriented columns:

- `Revenue`
- `Hour`
- `Month`
- `City`

### KPI Analysis

Computed KPIs include:

#### Revenue KPIs

- Total revenue
- Revenue by city
- Revenue by hour
- Revenue by month
- Revenue by product
- Best revenue hour
- Best revenue month
- Best revenue city
- Best revenue product
- Average revenue per order by city
- Top 5 cities by revenue

#### Product KPIs

- Quantity sold by hour
- Top-selling products
- Best-selling product by quantity
- Top 5 most sold products

#### Order KPIs

- Orders by city
- Orders by hour
- Average order value
- City with the most orders
- Hour with the most orders
- Number of orders per product

### Visualization

Automatic graph generation with matplotlib:

- Bar charts
- Line charts
- Revenue evolution
- Product performance analysis

---

## Project Structure

```text
sales-data-pipeline/
│
├── data/
│   └── Sales_April_2019.csv
│
├── output/
│   ├── revenue_by_city.csv
│   ├── revenue_by_hour.csv
│   ├── revenue_by_month.csv
│   ├── revenue_by_product.csv
│   ├── product_sold_by_hour.csv
│   ├── top_product.csv
│   ├── orders_by_city.csv
│   ├── orders_by_hour.csv
│   ├── average_revenue_by_order_by_city.csv
│   ├── orders_per_product.csv
│   ├── top_5_products.csv
│   └── top_5_cities.csv
│
├── plots/
│   ├── revenue_by_city.png
│   ├── revenue_by_hour.png
│   ├── revenue_by_product.png
│   ├── product_sold_by_hour.png
│   └── top_product.png
│
├── sales_pipeline.py
├── requirements.txt
└── README.md
````

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the pipeline:

```bash
python sales_pipeline.py
```

---

## Technologies Used

* Python
* pandas
* matplotlib

---

## Example Workflow

1. Load raw CSV dataset
2. Clean invalid data
3. Convert data types
4. Enrich the dataset
5. Compute KPIs
6. Export CSV reports
7. Generate graphs automatically

---

## Learning Objectives

This project was built to practice:

* Professional pandas workflows
* Business-oriented data analysis
* KPI generation
* Automation pipelines
* Data visualization

