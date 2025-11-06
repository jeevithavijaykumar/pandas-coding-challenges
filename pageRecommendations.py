import pandas as pd

friendship = pd.DataFrame({'user1_id':[1,1,1,2,2,2,6],
                           'user2_id':[2,3,4,3,4,5,1]})

likes = pd.DataFrame({'user_id':[1,2,3,4,5,6,2,3,6],
                      'page_id':[88,23,24,56,11,33,77,77,88]})

class solution:
    def page_recommendations(self, friendship, likes):

        Liked_pages = likes.loc[likes['user_id'] == 1, 'page_id']
        friends = pd.concat([friendship[friendship['user1_id'] == 1].user2_id,
                           friendship[friendship['user2_id'] == 1].user1_id], axis = 0)
        recomendations = likes['page_id'][(~likes['page_id'].isin(Liked_pages)) & (likes['user_id'].isin(friends))]
        return pd.DataFrame({'recommended_page': recomendations.unique()})

s= solution()
print(s.page_recommendations(friendship,likes))



