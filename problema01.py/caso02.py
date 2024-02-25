import pandas as pd

# Cargar el DataFrame
df_airbnb = pd.read_csv("/workspaces/Practica05-python/data/airbnb.csv")


# Cargar el DataFrame


# Filtrar las propiedades de Roberto y Clara
propiedades_roberto_clara = df_airbnb[df_airbnb['room_id'].isin([97503, 90387])]

# Guardar el DataFrame en un archivo Excel
propiedades_roberto_clara.to_excel("roberto.xlsx", index=False)

# Filtrar las propiedades de Roberto y Clara
propiedades_roberto_clara = df_airbnb[df_airbnb['room_id'].isin([97503, 90387])]

# Guardar el DataFrame en un archivo Excel
propiedades_roberto_clara.to_excel("roberto.xls", index=False)

