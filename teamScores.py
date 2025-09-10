# Table: Teams
#
# +---------------+----------+
# | Column Name   | Type     |
# +---------------+----------+
# | team_id       | int      |
# | team_name     | varchar  |
# +---------------+----------+
# team_id is the column with unique values of this table.
# Each row of this table represents a single football team.

# Table: Matches
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | match_id      | int     |
# | host_team     | int     |
# | guest_team    | int     |
# | host_goals    | int     |
# | guest_goals   | int     |
# +---------------+---------+
# match_id is the column of unique values of this table.
# Each row is a record of a finished match between two different teams.
# Teams host_team and guest_team are represented by their IDs in the Teams table (team_id), and they scored host_goals and guest_goals goals, respectively.

#You would like to compute the scores of all teams after all matches. Points are awarded as follows:
# A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
# A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
# A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).

# Write a solution that selects the team_id, team_name and num_points of each team in the tournament after all described matches.
# Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.

import pandas as pd
import numpy as np

class Solution:
    def team_scores(self,teams, matches):

        host = matches[['host_team','host_goals','guest_goals']].rename(columns={'host_team':'team_id'})
        guest = matches[['guest_team','guest_goals','host_goals']].rename(columns={'guest_team':'team_id'})
        host['points'] = np.where(host['host_goals'] > host['guest_goals'], 3,
                     np.where(host['host_goals'] == host['guest_goals'],1,0))
        guest['points'] = np.where(guest['guest_goals'] > guest['host_goals'], 3,
                     np.where(guest['host_goals'] == guest['guest_goals'],1,0))
        host_guest = pd.concat([host[['team_id','points']],guest[['team_id','points']]],ignore_index=True)
        df = host_guest.groupby('team_id')['points'].sum().reset_index(name='num_points')
        result = teams.merge(df, on ='team_id', how ='left').fillna(0)
        result['num_points'] = result['num_points'].astype(int)
        return result[['team_id','team_name','num_points']].sort_values(by=['num_points','team_id'],ascending=[False,True])


teams_df = pd.DataFrame({
    "team_id": [10, 20, 30, 40, 50],
    "team_name": ["Leetcode FC", "NewYork FC", "Atlanta FC", "Chicago FC", "Toronto FC"]
})

matches_df = pd.DataFrame({
    "host_team": [10, 20, 30, 10],
    "guest_team": [20, 30, 50, 50],
    "host_goals": [2, 1, 0, 3],
    "guest_goals": [1, 1, 0, 2]
})

s = Solution()
print(s.team_scores(teams_df, matches_df))