import pandas as pd
file_path = "/workspaces/Practica05-python/data/winemag-data-130k-v2.csv"
df = pd.read_csv(file_path)
df.rename(columns={'country': 'pais', 'province': 'provincia', 'variety': 'variedad', 'points': 'puntuacion'}, inplace=True)
df['longitud_titulo'] = df['title'].apply(lambda x: len(str(x)))
df['puntuacion_alta'] = df['puntuacion'].apply(lambda x: 'Alta' if x >= 90 else 'Baja')
precio_promedio_por_pais = df.groupby('pais')['price'].mean().reset_index()
precio_promedio_por_pais.rename(columns={'price': 'precio_promedio'}, inplace=True)
num_variedades_por_provincia = df.groupby('provincia')['variedad'].nunique().reset_index()
num_variedades_por_provincia.rename(columns={'variedad': 'num_variedades_unicas'}, inplace=True)
precio_promedio_por_pais.to_csv('precio_promedio_por_pais.csv', index=False)
vinos_mejor_puntuados = df.loc[df.groupby('pais')['puntuacion'].idxmax()]
promedio_precio_y_reviews_por_pais = df.groupby('pais').agg({'price': 'mean', 'puntuacion': 'count'}).reset_index()
promedio_precio_y_reviews_por_pais.rename(columns={'price': 'precio_promedio', 'puntuacion': 'cantidad_reviews'}, inplace=True)
promedio_precio_y_reviews_por_pais.sort_values(by='precio_promedio', ascending=False, inplace=True)
vinos_mejor_puntuados_por_provincia = df.loc[df.groupby('provincia')['puntuacion'].idxmax()]
print("Precio promedio por país:")
print(precio_promedio_por_pais)
print("\nVinos mejor puntuados por país:")
print(vinos_mejor_puntuados[['pais', 'title', 'puntuacion']])
print("\nPromedio de precio de vino y cantidad de reviews obtenidos por país:")
print(promedio_precio_y_reviews_por_pais)
print("\nVinos mejor puntuados por provincia:")
print(vinos_mejor_puntuados_por_provincia[['provincia', 'title', 'puntuacion']])