import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# 1. Descarga y carga del dataset desde Kaggle

def preparar_directorios():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    work_dir = os.path.join(base_dir, "data")
    os.makedirs(work_dir, exist_ok=True)

    dest_path = os.path.join(work_dir, "world_happiness")
    os.makedirs(dest_path, exist_ok=True)
    return work_dir, dest_path


def descargar_dataset(work_dir, dest_path):
    print("Descargando dataset desde Kaggle...")

    # Ruta completa de kaggle.exe
    kaggle_path = r"C:\Users\Usuario\AppData\Local\Programs\Python\Python313\Scripts\kaggle.exe"

    # Ejecutar descarga usando la ruta completa
    os.system(f'"{kaggle_path}" datasets download -d unsdsn/world-happiness -p "{work_dir}" --unzip')

    # Verificar archivos descargados
    downloaded_files = [f for f in os.listdir(work_dir) if f.startswith("world-happiness")]
    if not downloaded_files:
        raise FileNotFoundError("No se encontró el dataset descargado en Kaggle.")

    dataset_file = os.path.join(work_dir, downloaded_files[0])

    # Extraer archivos ZIP (si queda alguno)
    if dataset_file.endswith(".zip"):
        with zipfile.ZipFile(dataset_file, 'r') as zip_ref:
            zip_ref.extractall(dest_path)
        print(f"Archivos extraídos en '{dest_path}'")
    elif dataset_file.endswith(".csv"):
        new_path = os.path.join(dest_path, os.path.basename(dataset_file))
        if not os.path.exists(new_path):
            os.rename(dataset_file, new_path)
        print(f"Archivo CSV movido a '{dest_path}'")

    # Archivos CSV por año
    files = [f for f in os.listdir(dest_path) if f.endswith(".csv")]
    return {f.split(".")[0]: os.path.join(dest_path, f) for f in files}

# 2. Columnas para todos los años

def normalizar_columnas(df, year):
    mapping = {}
    if year in [2015, 2016]:
        mapping = {
            "Country": "Country",
            "Happiness Score": "Happiness",
            "Economy (GDP per Capita)": "GDP",
            "Family": "SocialSupport",
            "Health (Life Expectancy)": "LifeExpectancy",
            "Freedom": "Freedom",
            "Trust (Government Corruption)": "Corruption",
            "Generosity": "Generosity",
        }
    elif year == 2017:
        mapping = {
            "Country": "Country",
            "Happiness.Score": "Happiness",
            "Economy..GDP.per.Capita.": "GDP",
            "Family": "SocialSupport",
            "Health..Life.Expectancy.": "LifeExpectancy",
            "Freedom": "Freedom",
            "Trust..Government.Corruption.": "Corruption",
            "Generosity": "Generosity",
        }
    elif year in [2018, 2019]:
        mapping = {
            "Country or region": "Country",
            "Score": "Happiness",
            "GDP per capita": "GDP",
            "Social support": "SocialSupport",
            "Healthy life expectancy": "LifeExpectancy",
            "Freedom to make life choices": "Freedom",
            "Perceptions of corruption": "Corruption",
            "Generosity": "Generosity",
        }
    return df.rename(columns=mapping)[list(mapping.values())]


def cargar_datos(dict_files):
    data = []
    for name, path in dict_files.items():
        year = int("".join([c for c in name if c.isdigit()]) or 0)
        if year >= 2015 and year <= 2019:
            df = pd.read_csv(path)
            df_n = normalizar_columnas(df, year)
            df_n["Year"] = year
            data.append(df_n)
    return pd.concat(data, ignore_index=True)


# 3. Pregunta 1 – Factores principales que explican la felicidad

def analizar_factores(df):
    corr = df.corr(numeric_only=True)["Happiness"].drop("Happiness").sort_values(ascending=False)
    print("\n🔍 Correlaciones con la felicidad:\n", corr)

    # Top 3 factores
    top3 = corr.head(3)
    plt.figure(figsize=(6,4))
    top3.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Top 3 factores más influyentes en la felicidad")
    plt.ylabel("Correlación con felicidad")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    return top3


# 4. Pregunta 2 – Evolución de la felicidad a lo largo del tiempo

def analizar_tendencias(df):
    tendencia = df.groupby("Year")["Happiness"].mean().reset_index()
    plt.figure(figsize=(6,4))
    plt.plot(tendencia["Year"], tendencia["Happiness"], marker="o", linestyle="-", color="green")
    plt.title("Evolución de la felicidad promedio (2015-2019)")
    plt.xlabel("Año")
    plt.ylabel("Felicidad promedio")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()
    print("\nTendencia de felicidad promedio:\n", tendencia)


# 5. Ejecución

if __name__ == "__main__":
    work_dir, dest_path = preparar_directorios()
    dict_files = descargar_dataset(work_dir, dest_path)
    df_all = cargar_datos(dict_files)

    print("Dataset unificado con shape:", df_all.shape)

    # Pregunta 1
    top3 = analizar_factores(df_all)

    # Pregunta 2
    analizar_tendencias(df_all)


# Análisis de resultados

"""
Pregunta 1. ¿Cuáles son los principales factores que explican la felicidad en los países analizados?
-------------------------------------------------------------------------------------------------
El análisis de correlación muestra que los tres factores más influyentes son:
1. PIB per cápita → refleja la importancia de los recursos materiales y la estabilidad económica.
2. Esperanza de vida saludable → evidencia el impacto de la salud en el bienestar.
3. Apoyo social → subraya la relevancia de las redes comunitarias y familiares.

Estos factores presentan correlaciones positivas y significativas, lo que confirma su papel central 
en la determinación de la felicidad de los países.

Pregunta 2. ¿Qué tendencias se observan en la evolución de la felicidad a lo largo del tiempo?
-------------------------------------------------------------------------------------------------
La evolución de la felicidad promedio global entre 2015 y 2019 muestra una tendencia relativamente 
estable, con ligeros aumentos en algunos años. Esto sugiere que, a pesar de variaciones locales, la 
felicidad global ha permanecido constante en el periodo analizado.
"""

