import pandas as pd

file_path = 'D:\OS-PRJ\22019_kbo_for_kaggle_v2.csv'  # 데이터 세트 경로로 바꾸십시오.
data = pd.read_csv(file_path)

# Task 1
def top_10_players_in_stats(year, stat):
    return data[(data['p_year'] == year) & (data['year'] == year - 1)].sort_values(by=stat, ascending=False).head(10)[['batter_name', 'p_year', stat]]

# Task 2
def top_player_by_position_war(year):
    data_year = data[(data['p_year'] == year) & (data['year'] == year - 1)]
    return data_year.loc[data_year.groupby('cp')['war'].idxmax()][['batter_name', 'cp', 'war']]

# Task 3
def highest_correlation_with_salary():
    relevant_stats = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
    return data[relevant_stats + ['salary']].corr()['salary'].drop('salary').sort_values(ascending=False).head(1)



task_1_results = {year: {stat: top_10_players_in_stats(year, stat) for stat in ['H', 'avg', 'HR', 'OBP']} for year in range(2015, 2019)}
task_2_results = top_player_by_position_war(2018)
task_3_results = highest_correlation_with_salary()

task_1_results, task_2_results, task_3_results