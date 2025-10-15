# Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
# Return the result table in any order.

import pandas as pd

sales_person = pd.DataFrame({'sales_id' : [1,2,3,4,5], 'name': ['John','Amy','Mark','Pam','Alex'],
                             'Salary':[100000, 85000, 70000, 120000,65000 ],
                             'commission_rate':[6, 5, 8, 10, 9]})

company = pd.DataFrame({'com_id': [1,2,3,4], 'name' :['RED','ORANGE','YELLOW','GREEN'],
                        'city': ['Boston', 'NewYork', 'Boston','Austin']})

orders = pd.DataFrame({'orders_id': [1,2,3,4], 'order_date' : ['1/1/2014','2/1/2014','3/1/2014','4/1/2014'],
                       'com_id' : [3,4,1,1],'sales_id' : [4,5,1,4],'amount' : [10000,5000,50000,25000]})



class Solution:
    def sales(self, sales_person, company, orders):
        orders_with_company  = orders.merge(company, how='inner', on='com_id')
        orderswithRed = orders_with_company ['sales_id'][orders_with_company ['name'] == 'RED']
        result = sales_person[~sales_person['sales_id'].isin(orderswithRed)]
        return pd.DataFrame({'name': result['name'].unique()})


