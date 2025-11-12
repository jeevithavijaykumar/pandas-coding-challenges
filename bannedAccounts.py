import pandas as pd

log_info = pd.DataFrame({'account_id':[1,1,2,2,3,3,4,4],'ip_address':[1,2,6,7,9,13,10,11],
                         'login':['2021-02-01 09:00:00','2021-02-01 08:00:00','021-02-01 20:30:00','2021-02-02 20:30:00',
                                  '2021-02-01 16:00:00','2021-02-01 17:00:00','2021-02-01 16:00:00','2021-02-01 17:00:00'],
                         'logout':['2021-02-01 09:30:00','2021-02-01 11:30:00','2021-02-01 22:00:00','2021-02-02 22:00:00',
                                   '2021-02-01 16:59:59','2021-02-01 17:59:59','2021-02-01 17:00:00','2021-02-01 17:59:59']})
class accounts:
    def banned_accounts(self, log_info):
        df = log_info.merge(log_info, on='account_id',how='inner')
        mask = ((df['login_x'] <= df['logout_y']) &
                (df['login_y'] <= df['logout_x']) &
                (df['ip_address_x'] != df['ip_address_y']))
        result = df.loc[mask,['account_id']].drop_duplicates()
        return result

