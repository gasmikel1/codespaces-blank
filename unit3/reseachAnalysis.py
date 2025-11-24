# "1 this is a comparison because we are looking for the diffrecnes in yards in the divions."
from helper3 import get_advanced_team_records,  get_season_Results_By_team
import matplotlib.pyplot as plt
import pandas as pd
teamsData=get_advanced_team_records(2024)
print(teamsData)
teameRes = get_season_Results_By_team(2024,'PHI')
print(teameRes)

#"2 J.Willams had the most  targets"

 
# "3yesthe time of possesion is strongly correlated with winning as teams that win tend to have higher time of possesion percentages."