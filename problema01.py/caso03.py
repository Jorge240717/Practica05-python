import pandas as pd

# Cargar los datos del archivo CSV
df_airbnb = pd.read_csv("/workspaces/Practica05-python/data/airbnb.csv")
# Filtrar los alojamientos para Diana
alojamientos_diana = df_airbnb[(df_airbnb['price'] <= 50) & (df_airbnb['accommodates'] >= 1) & (df_airbnb['room_type'] == 'Shared room')]

# Ordenar los alojamientos por precio y, para habitaciones compartidas, por puntuación
alojamientos_ordenados = alojamientos_diana.sort_values(by=['price', 'overall_satisfaction'], ascending=[True, False])

# Seleccionar las 10 propiedades más baratas
top_10_propiedades = alojamientos_ordenados.head(10)

# Mostrar las propiedades seleccionadas
print(top_10_propiedades)
