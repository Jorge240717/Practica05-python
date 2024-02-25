import pandas as pd

# Ahora debería haber un salto de línea
df_airbnb = pd.read_csv("/workspaces/Practica05-python/data/airbnb.csv")

apartamentos_alicia = df_airbnb[(df_airbnb['reviews'] > 10) & (df_airbnb['overall_satisfaction'] > 4) & (df_airbnb['bedrooms'] >= 2)]
apartamentos_ordenados = apartamentos_alicia.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])
top_3_alternativas = apartamentos_ordenados.head(3)
print(top_3_alternativas)