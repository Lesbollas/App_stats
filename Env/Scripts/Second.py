import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('Env\Include\Team_stats.csv')
df_average =  df['average_attendance_overall'].mean()
df_grouped = df.groupby('team_name')
df_stats = df_grouped.agg({'average_attendance_overall': 'sum'})
print (df_stats)
print (f'this is average of league : {df_average}')