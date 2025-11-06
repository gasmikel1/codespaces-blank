from helper3 import weeklyPlayerStats,plot_weekly_player_stats,plot_player_stat
import matplotlib.pyplot as plt


stats = weeklyPlayerStats(2024, "QB", week=17)  
plot_player_stat(stats, stat="Rushing_tds", top_n=3, title=" QB Rushing Yards tds (2024)", save_path="qb_passing_yards_2024.png"  )
print(stats)

"X Worthy WR 3" 

"D.henry RB rush with 19 rushing_tds"

"J.Goff QB pass with 35 passing_tds"

"T.Tagovailoa         MIA          338.0            1        37           23            0.0           11.0            0       18.620001  62.162162   9.135135"

"24  00-0036442             J.Burrow         CIN          412.0            3        49           39            0.0           25.0            1       36.980000   79.591837   8.408163"