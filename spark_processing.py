from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def run_spark_processing():
    print("PySpark Big Data Processing")
    

    spark = SparkSession.builder \
        .appName("SnusSalesProcessing") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .master("local[*]") \
        .getOrCreate()
    
    # Loading the cleaned data into a Spark DataFrame
    try:
        df = spark.read.csv("cleaned_snus_sales.csv", header=True, inferSchema=True)
        print(f"Successfully loaded data into Spark. Total Records: {df.count()}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Perform high-level aggregations
    print("\n[Spark] Calculating Brand Sales Performance...")
    brand_summary = df.groupBy("Brand").agg(
        F.sum("Quantity").alias("Total_Cans_Sold"),
        F.round(F.sum(df.Quantity * df.Price_Per_Can), 2).alias("Total_Revenue_SEK"),
        F.round(F.avg("Price_Per_Can"), 2).alias("Avg_Price_Per_Can")
    ).orderBy(F.desc("Total_Revenue_SEK"))
    
    brand_summary.show()

    print("\n[Spark] Calculating Regional Demographics (Average Age by Region)...")
    region_summary = df.groupBy("Region").agg(
        F.round(F.avg("Customer_Age"), 1).alias("Avg_Customer_Age"),
        F.count("Order_ID").alias("Total_Orders")
    ).orderBy(F.desc("Total_Orders"))
    
    region_summary.show()

    print("[Spark] Exporting processed results to local files...")
    brand_summary.toPandas().to_csv("spark_brand_insights.csv", index=False)
    region_summary.toPandas().to_csv("spark_region_insights.csv", index=False)
    
    print("PySpark processing complete. Saved aggregated metric insights.")
    spark.stop()

if __name__ == "__main__":
    run_spark_processing()