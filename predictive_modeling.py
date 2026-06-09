from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

def run_predictive_modeling():
    print("--- Starting Phase 4: PySpark MLlib Predictive Modeling ---")
    
    # Initialize Spark Session with Windows networking fixes
    spark = SparkSession.builder \
        .appName("SnusSalesPredictiveModel") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .master("local[*]") \
        .getOrCreate()
    
    # Step 1: Load Cleaned Dataset
    try:
        df = spark.read.csv("cleaned_snus_sales.csv", header=True, inferSchema=True)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Step 2: Index Categorical Features (Convert text to numbers for ML)
    print("[ML Processing] Indexing categorical variables...")
    indexer_brand = StringIndexer(inputCol="Brand", outputCol="Brand_Indexed")
    indexer_region = StringIndexer(inputCol="Region", outputCol="Region_Indexed")
    
    df_transformed = indexer_brand.fit(df).transform(df)
    df_transformed = indexer_region.fit(df_transformed).transform(df_transformed)

    # Step 3: Assemble Feature Vectors
    # We will use Price, Customer Age, Brand, and Region to predict the Quantity purchased
    feature_cols = ["Price_Per_Can", "Customer_Age", "Brand_Indexed", "Region_Indexed"]
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    ml_data = assembler.transform(df_transformed).select("features", F.col("Quantity").alias("label"))

    # Step 4: Split Data into Train (80%) and Test (20%) Sets
    train_data, test_data = ml_data.randomSplit([0.8, 0.2], seed=42)
    print(f"[ML Processing] Training Set: {train_data.count()} records | Testing Set: {test_data.count()} records")

    # Step 5: Train Linear Regression Model
    print("[ML Training] Fitting Linear Regression Model...")
    lr = LinearRegression(featuresCol="features", labelCol="label")
    lr_model = lr.fit(train_data)

    # Step 6: Evaluate Model Performance
    predictions = lr_model.transform(test_data)
    evaluator = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="rmse")
    rmse = evaluator.evaluate(predictions)
    
    print("\n--- Model Evaluation Insights ---")
    print(f"Root Mean Squared Error (RMSE) on test data: {round(rmse, 4)}")
    print(f"Model Coefficients: {lr_model.coefficients}")
    print(f"Model Intercept: {round(lr_model.intercept, 4)}")

    # Step 7: Export Sample Predictions for Dashboard Validation
    print("\n[ML Export] Saving sample predictions for BI visualization...")
    predictions.select("prediction", "label").limit(100).toPandas().to_csv("spark_ml_predictions.csv", index=False)
    
    print("Predictive modeling phase complete!")
    spark.stop()

if __name__ == "__main__":
    run_predictive_modeling()