import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_snus_sales_data(num_records=25000):
    print(f"Generating {num_records} raw Snus sales transactions...")
    
    # Base configuration data
    brands = ['ZYN', 'Velo', 'General', 'Göteborgs Rapé', 'Siberia', 'VOLT', 'LYFT']
    product_types = ['Nicotine Pouch', 'Nicotine Pouch', 'Traditional Snus', 'Traditional Snus', 'Traditional Snus', 'Nicotine Pouch', 'Nicotine Pouch']
    flavors = ['Mint', 'Wintergreen', 'Original Tobacco', 'Bergamot', 'Berry', 'Citrus', 'Coffee']
    regions = ['Stockholm', 'Gothenburg', 'Malmö', 'Oslo', 'Bergen', 'International Export']
    channels = ['Online Store', 'Retail Store', 'Gas Station']
    
    data = []
    
    start_date = datetime(2025, 1, 1)
    
    for i in range(num_records):
        order_id = f"ORD{100000 + i}"
        days_offset = random.randint(0, 500)
        timestamp = start_date + timedelta(days=days_offset, hours=random.randint(0,23), minutes=random.randint(0,59))
        
        # Product info generation
        brand_idx = random.choices(range(len(brands)), weights=[0.25, 0.20, 0.15, 0.15, 0.08, 0.12, 0.05])[0]
        brand = brands[brand_idx]
        p_type = product_types[brand_idx]
        flavor = flavors[brand_idx] if random.random() > 0.15 else random.choice(flavors)
        
        # Numeric generation
        strength_mg = random.choice([4, 6, 8, 11, 15, 16, 43]) if p_type == 'Nicotine Pouch' else random.choice([8, 12, 14, 22, 43])
        quantity = random.choices([1, 2, 5, 10, 20, 30], weights=[0.3, 0.2, 0.2, 0.2, 0.07, 0.03])[0]
        price_per_can = round(random.uniform(35.0, 55.0), 2)
        
        # Demographics
        customer_age = random.randint(18, 65)
        customer_gender = random.choices(['M', 'F', 'Unspecified'], weights=[0.65, 0.30, 0.05])[0]
        region = random.choice(regions)
        channel = random.choice(channels)
        
        if random.random() < 0.04: 
            customer_age = np.nan
        if random.random() < 0.03:  
            region = None
            
        data.append([
            order_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'), brand, p_type, 
            flavor, strength_mg, quantity, price_per_can, customer_age, customer_gender, region, channel
        ])
    
    columns = [
        'Order_ID', 'Timestamp', 'Brand', 'Product_Type', 'Flavor', 
        'Strength_mg', 'Quantity', 'Price_Per_Can', 'Customer_Age', 'Customer_Gender', 'Region', 'Sales_Channel'
    ]
    
    df = pd.DataFrame(data, columns=columns)
    
    df_duplicates = df.sample(n=350, random_state=42)
    df = pd.concat([df, df_duplicates], ignore_index=True)
    
    df['Price_Per_Can'] = df['Price_Per_Can'].astype(object)
    
    sample_indices = df.sample(n=50, random_state=42).index
    df.loc[sample_indices, 'Price_Per_Can'] = df.loc[sample_indices, 'Price_Per_Can'].astype(str) + " SEK"
    
    # Save raw file
    df.to_csv("raw_snus_sales.csv", index=False)
    print("Successfully created 'raw_snus_sales.csv' containing simulated raw transactional architecture.")

if __name__ == "__main__":
    generate_snus_sales_data()