from helper3 import get_season_totals_by_position,plot_position_stat_bar,plot_player_stat_by_week,get_player_stats

plot_position_stat_bar(2022, 'RB','rushing_yards',save_path="rb_rushing_yards_2022.png",)
plot_position_stat_bar(2023, 'RB','rushing_yards',save_path="rb_rushing_yards_2023.png",)
plot_position_stat_bar(2024, 'RB','rushing_yards',save_path="rb_rushing_yards_2024.png",)


BestRB34=get_season_totals_by_position(2024,"RB")
BestRB33=get_season_totals_by_position(2023,"RB")
BestRB32=get_season_totals_by_position(2022,"RB")

print(BestRB34)
print(BestRB33)
print(BestRB32)

'answer=(Dark Henry in rushing yards )'
plot_player_stat_by_week(2024,'Jalen','Hurts','passing_yards',save_path='Jalen_Hurts_passing_yard_2024.png')
plot_player_stat_by_week(2023,'Jalen','Hurts','passing_yards',save_path='Jalen_Hurts_passing_yard_2023.png')
plot_player_stat_by_week(2022,'Jalen','Hurts','passing_yards',save_path='Jalen_Hurts_passing_yard_2022.png')

# Jalen= get_player_stats(2024,'Jalen','Hurts')
# print(Jalen)
