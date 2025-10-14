import pandas as pd
import nfl_data_py as nfl 
from helperFunction import get_team_records

schdules = nfl.import_schedules([2024])

print(schdules.columns.tolist())

records = get_team_records(2025)
                           
print(records)

print(records[['wins','losses','points_for','points_against']])

# print(records[['wins']].mean())