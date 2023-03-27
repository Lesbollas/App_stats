from tkinter import *
import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('Env\Include\Team_stats.csv')
df_average =  df['average_attendance_overall'].mean()
df_grouped = df.groupby('team_name')
df_stats = df_grouped.agg({'average_attendance_overall': 'sum'})
print (df_stats)
print (f'this is average of league : {df_average}')

 













 
### Fenêtre graphique ###
# fenetre = Tk()
# #Cliquer pour afficher 
# def afficher_variable():
#     var = df_average
#     resultat.config(text=var)

# label = Label(fenetre, text="Cliquez sur le bouton pour afficher la moyenne de la league. ")
# label.pack()
# resultat = Label(fenetre)
# resultat.pack()

# bouton = Button(fenetre, text="Afficher la variable", command=afficher_variable)
# bouton.pack()

# fenetre.mainloop()
#######################################