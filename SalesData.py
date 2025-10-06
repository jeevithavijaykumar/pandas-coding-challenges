# 1. Finds the top 3 products by total sales in each region
# 2. Only includes products that had sales on at least 10 different days
# 3. Returns results as a dictionary: `{region: [(product_id, total_sales), ...]}`

import pandas as pd
import numpy as np

def analyze_sales(filename):
    result ={}

    df = pd.read_csv(filename)

    df['date_count'] = df.groupby(['product_id'])['date'].transform('nunique')
    valid_df = df.loc[df['date_count'] > 10].reset_index()
    print(valid_df)
    sales_summary = valid_df.groupby(['region','product_id'])['sales_amount'].sum().reset_index(name='total_sales')
    print(sales_summary)
    top_three_products = sales_summary.groupby(['region','product_id'])['total_sales'].nlargest(3).reset_index()
    print(top_three_products)

    for region, group in top_three_products.groupby('region'):
        result[region] = list(zip(group['product_id'], group['total_sales']))

    return result

a = analyze_sales(filename)
print(a)









