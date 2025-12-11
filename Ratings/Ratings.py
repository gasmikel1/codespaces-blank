# what does it means to be underrated, or overrated?
# To be underratrd you must be a good player but unseen by the masses.
#to be an overrated player you must be a pritty average player that is seen by everyone, and everyone likes.

from helper import get_season_totals_by_position,plot_position_stat_bar,plot_player_stat_by_week,get_player_stats

stat=get_player_stats(2024,'Baker', 'Mayfield')
print(stat)
plot_player_stat_by_week(2024,'Baker', 'Mayfield', 'rushing_yards',save_path=' Baker_mayfield_rushing_yard_2024.png')
plot_player_stat_by_week(2024,'Baker', 'Mayfield', 'passing_yards',save_path=' Baker_mayfield_passing_yard_2024.png')
plot_player_stat_by_week(2024,'Baker', 'Mayfield', 'passing_tds',save_path=' Baker_mayfield_passing_tds_2024.png')
"this guy is pretty underrated sure he's not doing great now, and he had ups and downs ,but he was putting in work. "


stat2024=get_player_stats(2024,'Brock', 'Purdy')
print(stat2024)
plot_player_stat_by_week(2024,'Brock', 'Purdy', 'rushing_yards',save_path=' Brock_Purdy_rushing_yard_2024.png')
plot_player_stat_by_week(2024,'Brock', 'Purdy', 'passing_yards',save_path=' Brock_Purdy_passing_yard_2024.png')
plot_player_stat_by_week(2024,'Brock', 'Purdy', 'passing_tds',save_path=' Brock_Purdy_passing_tds_2024.png')
"He is pretty underrated like no one is talking abut him but he is doing good this season. His passing yards and tds are decent and his rushing yards show that he can make plays with his legs too. If he keeps this up he could be a solid QB in the league."
