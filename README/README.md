# Superstore Cloud Analytics Dashboard

## Project Overview
This project is a cloud-based Big Data analytics dashboard designed to process, analyze, and visualize Superstore sales data. The system performs data cleaning, database loading, analytical queries, dashboard visualization, and AI-powered business insight generation.

---

## Features
- Data cleaning and preprocessing using Python and Pandas
- SQLite database integration
- Analytical business queries
- Interactive dashboard using Chart.js
- KPI cards and region filter
- AI-generated business insights using OpenRouter API

---

## Technologies Used
- Python
- Pandas
- SQLite
- HTML
- CSS
- JavaScript
- Chart.js
- OpenRouter API
- Visual Studio Code

---

## Project Structure

SUPERSTORE_FINAL_PROJECT
│
├── datasets
├── scripts
├── database
├── dashboard
├── screenshots
├── documentation
└── README

---

## Required Python Libraries

Install the required libraries using:

```bash
pip install pandas requests
```

---

## How to Run the Project

### 1. Clean the Dataset

Run the following command in the terminal:

```bash
python clean.py
```

This script removes missing values, normalizes the sales column, removes outliers using the IQR method, and exports the cleaned dataset.

---

### 2. Load Data into SQLite Database

Run:

```bash
python load_database.py
```

This script creates the SQLite database and loads the cleaned dataset into the `superstore_sales` table.

---

### 3. Run Analytical Queries

Run:

```bash
python queries.py
```

This script executes analytical SQL queries such as:
- Total sales per category
- Average sales per region
- Top 10 products by sales

---

### 4. Run AI Insight Generator

Run:

```bash
python ai_insight.py
```

This script sends dataset summary information to the OpenRouter API and generates AI-powered business insights and recommendations.

---

### 5. Open the Dashboard

Open the `index.html` file using Live Server in Visual Studio Code.

The dashboard displays:
- KPI cards
- Bar chart
- Pie chart
- Line chart
- Interactive region filter

---

## AI Integration

The project uses the OpenRouter API together with a free AI language model to generate business insights from real dataset summaries. The AI analyzes information such as total sales, average sales, top-performing category, and top-performing region, then produces recommendations to support business decision-making.

---

## Group Members

- Nermal, Isagani H.
- Balmeo, Michael Angelo
- Cofreros, John Luis
- Siscar, Jasper Roa
- Villegas, Chauncey Hamilton