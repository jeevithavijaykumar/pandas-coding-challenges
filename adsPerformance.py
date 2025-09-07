#Table: Ads

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | ad_id         | int     |
# | user_id       | int     |
# | action        | enum    |
# +---------------+---------+
 # (ad_id, user_id) is the primary key (combination of columns with unique values) for this table.

# Write a solution to find the ctr of each Ad. Round ctr to two decimal points.
# Return the result table ordered by ctr in descending order and by ad_id in ascending order in case of a tie.
# The result format is in the following example.

import pandas as pd
import numpy as np

class Solution:
    def ads_performance(self,ads):

        ads['click'] = np.where(ads['action']=='Clicked',1,0)
        ads['view'] = np.where(ads['action']=='Viewed',1,0)
        result = ads.groupby('ad_id')[['click','view']].sum().reset_index()
        result['ctr'] = np.where((result['click']+ result['view'])== 0, 0,
                        round((result['click'])/(result['click'] + result['view'])*100,2))

        return result[['ad_id','ctr']].sort_values(by=['ctr','ad_id'], ascending=[False,True])


data = {"ad_id":   [1, 2, 3, 5, 1, 2, 3, 1, 2, 1],
        "user_id": [1, 2, 3, 5, 7, 7, 5, 4, 11, 2],
        "action":  ["Clicked", "Clicked", "Viewed", "Ignored", "Ignored",
                "Viewed", "Clicked", "Viewed", "Viewed", "Clicked"]}

ads = pd.DataFrame(data)
s= Solution()
print(s.ads_performance(ads))
