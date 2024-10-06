import pandas as pd


def fun_algoritmo():
    file_path = 'Toneladas y Distancia.xlsx'
    distancia_df = pd.read_excel(file_path, sheet_name='Distancia Municipios a Rellenos')
    distancia_df.columns = distancia_df.columns.str.strip()
    nombres_rellenos = distancia_df.columns[2:].tolist()
    numeros_rellenos = {"Boca del Rio": 1, "La antigua1": 2, "La antigua2": 3, "La antigua3": 4,
                        "Manlio Fabio Altamirano": 5, "Medellin de Bravo": 6, "Puente Nacional": 7, "Tlalixcoyan": 8,
                        "Veracruz": 9}

    distancia_totales = {relleno: 0 for relleno in nombres_rellenos}
    for index, row in distancia_df.iterrows():
        for i, relleno in enumerate(nombres_rellenos):
            distancia = row.iloc[i + 2]
            if isinstance(distancia, (int, float)) and distancia > 0:
                distancia_totales[relleno] += distancia

    rellenos_ordenados = [(relleno, numeros_rellenos[relleno], distancia_totales[relleno]) for relleno in
                          nombres_rellenos]
    rellenos_ordenados.sort(key=lambda x: x[2])
    top_3_rellenos = rellenos_ordenados[:3]
    numeros_top_3 = tuple(numero for _, numero, _ in top_3_rellenos)
    return numeros_top_3


if __name__ == "__main__":
    fun_algoritmo()
