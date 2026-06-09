# Big_Data_Project
# Scalable Snus Sales Analytics & Predictive Modeling

## Project Overview

This project aims to build a straightforward, automated data pipeline, taking the raw, unorganized transaction data, cleaning it up using Pandas, shifting it into a distributed PySpark environment to handle the heavy aggregations. Thus trains the machine learning model to predict how much product people actually buy, and plug the results into a clean, easy-to-read Tableau dashboard. 

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

## Pipeline Architecture & Tech Stack

Instead of bundling everything into one giant massive script, the pipeline is split into clean, modular layers:
[ Raw Data Ingest ] ──► [ Cleaning / EDA ] ──► [ Scale-Out Engine ] ──► [ ML Modeling ] ──► [ Visuals ]
      (Pandas)                       (PySpark Core)                     (PySpark MLlib)      (Tableau)

## Data Prep (Pandas)  
Handles the initial workload of data, handling duplicate orders, fixing broken data types, and patching up missing data fields.

## Processing Engine (PySpark):
Takes the clean data and uses a distributed cluster setup to calculate high-level brand revenues and regional trends simultaneously.

## Advanced Analytics (PySpark MLlib):
Runs a distributed Linear Regression model right inside the Spark environment to forecast consumer purchasing behavior.

## Visualization (Tableau Public):
Uses the final aggregated CSV exports to render an analytics dashboard.

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

## Installation & Running the Code

## Prerequisites
You will need **Python 3.10+**, **Java JDK 17**, and **Apache Spark** installed on your computer.

To run the pipeline from start to finish, navigate to your project directory and execute the scripts in this order:

1. preprocessing_eda.py ## To clean the raw dataset

2. spark_processing.py ## To process the clean data and to create the regional and brand analystics tables

3. predictive_modeling.py ## To create the final ML prediction table

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

## Key Findings & Insights

## The Most Popular Brand ( by revenue ) is
          ZYN - Rev: 1.7 mil SEK with 38,112 cans sold

## The "Premium" Option is
          Velo - Rev: 1.39 mil SEK with the highest avg. price/can with 45.06 SEK/ can

## Nicotine pouches are more popular in
          Gothenburg - 4,139 orders
          Oslo - 4,079 orders
          Stockholm - 4,057 orders

## Typically, people that use snus are
          41 - 42 years old

## Observing customer habbits, we can predict that people will buy
          Between 5 and 6 cans/ transaction (5.78-6.14)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

## Visual Aid

## For an easier time visualizing the statistics presented before, make sure to check out

sales_analytics_dashboard.twb (Using Tableau)
          