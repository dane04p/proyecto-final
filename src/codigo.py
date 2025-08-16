import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------
# 1. Descarga y carga del dataset
# -----------------------------------------------------------

def preparar_directorios():
    """Crea carpeta padre/data/world_happiness para guardar dataset"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # carpeta padre
    work_dir = os.path.join(base_dir, "data")
    os.makedirs(work_dir, exist_ok=True)

    dest_path = os.path.join(work_dir, "world_happiness")
    os.makedirs(dest_path, exist_ok=True)
    return work_dir, dest_path


def descargar_dataset(work_dir, dest_path):
    """Descarga dataset de Kaggle y lo descomprime/mueve"""
    print("Descargando dataset desde Kaggle...")
    os.system(f'kaggle datasets download -d unsdsn/world-happiness -p "{work_dir}"')

    downloaded_files = [f for f in os.listdir(work_dir) if f.startswith("world-happiness")]
    if not downloaded_files:
        raise FileNotFoundError("No se encontró el dataset descargado en Kaggle.")

    dataset_file = os.path.join(work_dir, downloaded_files[0])

    # Extraer o mover
    if dataset_file.endswith(".zip"):
        with zipfile.ZipFile(dataset_file, 'r') as zip_ref:
            zip_ref.extractall(dest_path)
        print(f"Archivo ZIP descomprimido en '{dest_path}'")
    elif dataset_file.endswith(".csv"):
        new_path = os.path.join(dest_path, os.path.basename(dataset_file))
        if not os.path.exists(new_path):
            os.rename(dataset_file, new_path)
        print(f"Archivo CSV movido a '{dest_path}'")
    else:
        raise ValueError(f"Formato no esperado: {dataset_file}")

    # Detectar CSV
    files = os.listdir(dest_path)
    csv_file = [f for f in files if f.endswith(".csv")][0]
    return os.path.join(dest_path, csv_file)


def cargar_dataset(csv_path):
    """Lee CSV y detecta columnas clave"""
    df = pd.read_csv(csv_path)
    print("Columnas en el dataset:", df.columns.tolist())

    possible_corr = [c for c in df.columns if 'corrup' in c.lower() or 'corrupt' in c.lower()]
    possible_score = [c for c in df.columns if 'ladder' in c.lower() or 'score' in c.lower() or 'happiness' in c.lower()]
    possible_country = [c for c in df.columns if 'country' in c.lower()]

    corruption_col = possible_corr[0]
    score_col = possible_score[0]
    country_col = possible_country[0]

    df = df.dropna(subset=[country_col, corruption_col, score_col])
    return df, country_col, score_col, corruption_col


# -----------------------------------------------------------
# 2) Análisis básico: corrupción vs felicidad
# -----------------------------------------------------------

def analizar_corrupcion(df, corruption_col, score_col):
    """Agrupa por cuartiles de corrupción y grafica felicidad promedio"""
    df['corr_group'] = pd.qcut(
        df[corruption_col],
        q=4,
        labels=['Muy baja', 'Baja', 'Alta', 'Muy alta'],
        duplicates='drop'
    )

    grouped = df.groupby('corr_group')[score_col].agg(['mean','std','count']).reset_index()
    print("\nPromedios de felicidad según corrupción:\n", grouped)

    # gráfico
    x = np.arange(len(grouped))
    plt.figure(figsize=(8,5))
    plt.bar(x, grouped['mean'])
    plt.xticks(x, grouped['corr_group'].astype(str))
    plt.xlabel('Percepción de corrupción (cuartiles)')
    plt.ylabel('Felicidad promedio')
    plt.title('Felicidad promedio por nivel de corrupción')
    plt.tight_layout()
    plt.show()

    # correlación
    try:
        from scipy.stats import pearsonr
        r, p = pearsonr(df[corruption_col], df[score_col])
        print(f"Correlación Pearson corrupción vs felicidad: r = {r:.3f}, p = {p:.3e}")
    except Exception:
        r = np.corrcoef(df[corruption_col], df[score_col])[0,1]
        print(f"Correlación (sin scipy) ≈ r = {r:.3f}")

# -----------------------------------------------------------
# 3) Análisis avanzado: top países, mapa y radar
# -----------------------------------------------------------

def mostrar_top_paises(df, country_col, score_col, n=10):
    """Imprime y devuelve top n países más felices"""
    top_countries = df[[country_col, score_col]].sort_values(score_col, ascending=False).head(n)
    print(f"\n🌍 Top {n} países más felices:\n", top_countries)
    return top_countries


def graficar_mapa(df, country_col, score_col):
    """Mapa mundial coloreado por puntaje de felicidad"""
    fig_map = px.choropleth(
        df,
        locations=country_col,
        locationmode="country names",
        color=score_col,
        color_continuous_scale="Viridis",
        title="Mapa de felicidad por país"
    )
    fig_map.show()


def graficar_radar(df, score_col):
    """Radar con correlaciones de factores (PIB, salud, apoyo social, etc.)"""
    factors = [c for c in df.columns if any(k in c.lower() for k in [
        "gdp", "economy", "social", "family", "health", "life", "freedom", "generosity"
    ])]

    if factors:
        radar_data = df[factors + [score_col]].corr()[score_col].drop(score_col)

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=radar_data.values,
            theta=radar_data.index,
            fill='toself',
            name="Influencia en felicidad"
        ))

        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[-1,1])),
            showlegend=False,
            title="Factores que influyen en la felicidad (correlación con score)"
        )
        fig_radar.show()

        # Factor número 1
        top_factor = radar_data.abs().idxmax()
        print(f"\n✅ El factor que más influye en la felicidad es: {top_factor}")
    else:
        print("No se encontraron factores adicionales en el dataset para el gráfico radar.")


# -----------------------------------------------------------
# Llamar a las funciones principales
# -----------------------------------------------------------

if __name__ == "__main__":
    work_dir, dest_path = preparar_directorios()
    csv_path = descargar_dataset(work_dir, dest_path)
    df, country_col, score_col, corruption_col = cargar_dataset(csv_path)

    # Análisis 1: corrupción vs felicidad
    analizar_corrupcion(df, corruption_col, score_col)

    # Análisis 2: países más felices
    mostrar_top_paises(df, country_col, score_col)

    # Análisis 3: mapa de felicidad
    graficar_mapa(df, country_col, score_col)

    # Análisis 4: radar de factores
    graficar_radar(df, score_col)
    
# -----------------------------------------------------------
# Análisis de resultados
# -----------------------------------------------------------
"""Análisis de resultados: 
P3 / Al ser el valor de p menor a 0.05, podemos concluir que existe una correlación 
significativa entre la percepción de corrupción y el puntaje de felicidad. Que no se debe al azar.
El valor de r indica la fuerza y dirección de esta relación. 
En este caso al ser una correlación negativa significa que a medida que aumenta la percepción de 
corrupción, el puntaje de felicidad tiende a disminuir. Y al ser r de 0.37 indica una correlación moderada. 
P4 / El factor que más influye en la felicidad es el PIB per cápita, seguido por la salud y el apoyo social.
Los 3 países con mayor puntaje de felicidad son Finlandia, Dinamarca y Suiza."""