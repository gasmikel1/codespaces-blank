import pandas as pd
import nfl_data_py as nfl 
from helperFunction import get_team_records

schdules = nfl.import_schedules([2024])

print(schdules.columns.tolist())

records = get_team_records(2024)
                           
print(records)

#print(records[['wins','losses','Home','Away']])

# print(records[['wins']].mean())
# birds =get_season_Results_By_Team(2025,'NYJ')
# print(birds)