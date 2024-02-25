import pandas as pd
import requests
def limpiar_columnas(df):
    df.columns = df.columns.str.lower().str.replace(' ', '').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    df = df.loc[:,~df.columns.duplicated()]
    df['dispositivolegal'] = df['dispositivolegal'].str.replace(',', '')
    return df
def dolarizar_montos(df):
    response = requests.get('https://api.apis.net.pe/v1/tipo-cambio-sunat')
    if response.status_code == 200:
        data = response.json()
        valor_dolar = data['dolar']
        df['montoinversion_dolarizado'] = df['montoinversion'] / valor_dolar
        df['montotransferencia_dolarizado'] = df['montotransferencia'] / valor_dolar
    else:
        print("Error al obtener el tipo de cambio desde el API de Sunat")
    return df
def mapear_estado(df):
    df['estado'] = df['estado'].map({'Actos Previos': 1, 'Resuelto': 0, 'Ejecucion': 2, 'Concluido': 3})
    return df
def generar_reportes(df):
    ubigeos = df[['ubigeo', 'region', 'provincia', 'distrito']].drop_duplicates()
    for region, region_data in df.groupby('region'):
        top_5 = region_data[(region_data['tipo'] == 'Urbano') & (region_data['estado'].isin([1, 2, 3]))].nlargest(5, 'costoinversion')
        if not top_5.empty:
            filename = f'top5_{region}_urbano.xlsx'
            top_5.to_excel(filename, index=False)
def main():
    file_path = "/workspaces/Practica05-python/data/reactiva.xlsx"
    df = pd.read_excel(file_path)
    df = limpiar_columnas(df)
    df = dolarizar_montos(df)
    df = mapear_estado(df)
    generar_reportes(df)
if __name__ == "__main__":
    main()