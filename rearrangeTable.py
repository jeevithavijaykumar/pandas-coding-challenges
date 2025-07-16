# Write a solution to rearrange the Products table so that each row has (product_id, store, price).
# If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
# Return the result table in any order.
#Input:
# Products table:
# +------------+--------+--------+--------+
# | product_id | store1 | store2 | store3 |
# +------------+--------+--------+--------+
# | 0          | 95     | 100    | 105    |
# | 1          | 70     | null   | 80     |
# +------------+--------+--------+--------+
#Output:
# +------------+--------+-------+
# | product_id | store  | price |
# +------------+--------+-------+
# | 0          | store1 | 95    |
# | 0          | store2 | 100   |
# | 0          | store3 | 105   |
# | 1          | store1 | 70    |
#  1          | store3 | 80    |
# +------------+--------+-------+

import pandas as pd

products = pd.DataFrame({
            'product_id':[1,2],
            'store1':[95,70],
            'store2':[100, None],
            'store3':[105,80]
})

def rearrangetable(products):

    melted = pd.melt(products, id_vars='product_id', value_vars=['store1','store2','store3'],
                     var_name='store', value_name='price').dropna(subset=['price'])
    return melted

output = rearrangetable(products)
print(output)







