import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------
# 1. Descarga y carga del dataset
""" Bloque de código para descargar y cargar el dataset de felicidad mundial desde el API de 
Kaggle. Este script prepara los directorios necesarios, descarga el dataset, lo descomprime y 
lo carga en un DataFrame de pandas."""
# -----------------------------------------------------------

def preparar_directorios():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    work_dir = os.path.join(base_dir, "data")
    os.makedirs(work_dir, exist_ok=True)

    dest_path = os.path.join(work_dir, "world_happiness")
    os.makedirs(dest_path, exist_ok=True)
    return work_dir, dest_path


def descargar_dataset(work_dir, dest_path):
    print("Descargando dataset desde Kaggle...")
    os.system(f'kaggle datasets download -d unsdsn/world-happiness -p "{work_dir}"')

    downloaded_files = [f for f in os.listdir(work_dir) if f.startswith("world-happiness")]
    if not downloaded_files:
        raise FileNotFoundError("No se encontró el dataset descargado en Kaggle.")

    dataset_file = os.path.join(work_dir, downloaded_files[0])

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

    files = os.listdir(dest_path)
    csv_file = [f for f in files if f.endswith(".csv")][0]
    return os.path.join(dest_path, csv_file)


# -----------------------------------------------------------
# 1.1) Exploración adicional: concatenación y análisis descriptivo
# -----------------------------------------------------------

def exploracion_adicional(dest_path):
    archivos_csv = [pd.read_csv(os.path.join(dest_path, f)) for f in os.listdir(dest_path) if f.endswith(".csv")]
    big_frame = pd.concat(archivos_csv, ignore_index=True)

    print(f"\nTotal de archivos procesados: {len(archivos_csv)}")

    print("\nInfo del dataframe: ")
    big_frame.info()

    print("\nResumen estadístico: ")
    print(big_frame.describe())

    forma = big_frame.shape
    print(f"\nForma del dataframe: {forma}")
        
    print("\nTipos de datos: ")
    print(big_frame.dtypes)

    print("\nValores nulos del dataframe: ")
    print(big_frame.isnull().sum())

    print("\nPrimeras 10 filas del dataset: ")
    print(big_frame.head(10))

    if 'Region' in big_frame.columns:
        big_frame['Region'].value_counts().plot(kind='bar')
        plt.title("Cantidad de paises por región")
        plt.xlabel("Región")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    return big_frame


def cargar_dataset(csv_path):
    df = pd.read_csv(csv_path)
    print("Columnas en el dataset:", df.columns.tolist())

    possible_corr = [c for c in df.columns if 'corrup' in c.lower() or 'corrupt' in c.lower()]
    possible_score = [c for c in df.columns if 'score' in c.lower()]
    possible_country = [c for c in df.columns if 'country' in c.lower() or 'region' in c.lower()]

    corruption_col = possible_corr[0]
    score_col = possible_score[0]
    country_col = possible_country[0]

    df = df.dropna(subset=[country_col, corruption_col, score_col])
    return df, country_col, score_col, corruption_col


# -----------------------------------------------------------
# 2) Análisis básico: corrupción vs felicidad
# -----------------------------------------------------------

def analizar_corrupcion(df, corruption_col, score_col):
    df["corrup_real"] = 1 - df[corruption_col]

    df['corr_group'] = pd.qcut(
        df['corrup_real'],
        q=4,
        labels=['Muy baja', 'Baja', 'Alta', 'Muy alta'],
        duplicates='drop'
    )

    grouped = df.groupby('corr_group')[score_col].agg(['mean','std','count']).reset_index()
    print("\nPromedios de felicidad según corrupción:\n", grouped)

    x = np.arange(len(grouped))
    plt.figure(figsize=(8,5))
    bars = plt.bar(x, grouped['mean'], color=plt.cm.viridis(np.linspace(0,1,len(grouped))))

    plt.xticks(x, grouped['corr_group'].astype(str), fontsize=11)
    plt.xlabel('Niveles de corrupción (cuartiles)', fontsize=12)
    plt.ylabel('Felicidad promedio', fontsize=12)
    plt.title('Felicidad promedio según niveles de corrupción', fontsize=14, fontweight='bold')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f"{yval:.2f}",
                 ha='center', va='bottom', fontsize=10)

    plt.ylim(2, 8)
    plt.tight_layout()
    plt.show()

    try:
        from scipy.stats import pearsonr
        r, p = pearsonr(df['corrup_real'], df[score_col])
        print(f"Correlación Pearson corrupción vs felicidad: r = {r:.3f}, p = {p:.3e}")
    except Exception:
        r = np.corrcoef(df['corrup_real'], df[score_col])[0,1]
        print(f"Correlación (sin scipy) ≈ r = {r:.3f}")


# -----------------------------------------------------------
# 3) Análisis avanzado: top países, mapa y radar de factores
# -----------------------------------------------------------

def mostrar_top_paises(df, country_col, score_col, n=10):
    top_countries = df[[country_col, score_col]].sort_values(score_col, ascending=False).head(n)
    print(f"\n🌍 Top {n} países más felices:\n", top_countries)
    return top_countries


def graficar_mapa(df, country_col, score_col):
    fig_map = px.choropleth(
        df,
        locations=country_col,
        locationmode="country names",
        color=score_col,
        color_continuous_scale="Turbo",  
        title="🌍 Índice de felicidad por país",
        hover_name=country_col,
        hover_data={score_col: ':.2f'}
    )

    fig_map.update_layout(
        geo=dict(showframe=False, showcoastlines=True, projection_type="natural earth"),
        title_font=dict(size=18, family="Arial", color="black"),
        coloraxis_colorbar=dict(title="Felicidad", ticks="outside")
    )
    fig_map.show()


def graficar_radar(df, score_col):
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
            name="Influencia en felicidad",
            line=dict(color="royalblue", width=2),
            fillcolor="rgba(65,105,225,0.3)"
        ))

        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[-1,1], showline=True, linewidth=1, gridcolor="lightgrey"),
                angularaxis=dict(showline=True, linewidth=1, gridcolor="lightgrey")
            ),
            title="📊 Factores que influyen en la felicidad",
            title_font=dict(size=16, family="Arial", color="black"),
            showlegend=False
        )
        fig_radar.show()

        top_factor = radar_data.abs().idxmax()
        print(f"\n✅ El factor que más influye en la felicidad es: {top_factor}")
    else:
        print("No se encontraron factores adicionales en el dataset para el gráfico radar.")


# -----------------------------------------------------------
# 4) Llamar a las funciones principales
# -----------------------------------------------------------

if __name__ == "__main__":
    work_dir, dest_path = preparar_directorios()
    csv_path = descargar_dataset(work_dir, dest_path)

    # Exploración inicial (se hace justo después de descargar los datos)
    exploracion_adicional(dest_path)

    # Dataset principal para análisis de corrupción y felicidad
    df, country_col, score_col, corruption_col = cargar_dataset(csv_path)

    analizar_corrupcion(df, corruption_col, score_col)
    mostrar_top_paises(df, country_col, score_col)
    graficar_mapa(df, country_col, score_col)
    graficar_radar(df, score_col)

# -----------------------------------------------------------
# Análisis de resultados
# -----------------------------------------------------------
"""
Pregunta 3. ¿Puede la percepción de la corrupción de un país tener efectos negativos en la 
felicidad de sus habitantes?
------------------------------------------
El análisis de correlación muestra que el valor de p es menor a 0.05 (p ≈ 2.76e-07), 
lo que indica que la relación entre la percepción de corrupción y el puntaje de felicidad 
es estadísticamente significativa, es decir, que no es atribuible al azar.

Por otro lado, el coeficiente de correlación (r ≈ -0.395) refleja una relación negativa y 
de magnitud moderada, lo que indica que a mayor percepción de corrupción, menor es el puntaje 
de felicidad promedio de los países.

Aunque se observa cierta variación entre los cuartiles, la tendencia general confirma que un 
mayor nivel de corrupción percibida se asocia con una menor felicidad en la población. 

Estos hallazgos respaldan la hipótesis de que la corrupción constituye un factor que impacta 
negativamente en el bienestar de los habitantes.

Pregunta 4. ¿Cuáles son los países más felices dentro de la base de datos y qué factores 
explican esa felicidad?
---------------------------------------

Top de países más felices
-------------------------
Los países nórdicos dominan el ranking, con Finlandia, Dinamarca y Suiza en las primeras 
posiciones.
Este patrón sugiere que sociedades con altos niveles de seguridad económica, baja corrupción y
fuertes redes de apoyo social tienden a alcanzar mayores niveles de felicidad.

-------------------------
Factores con mayor influencia en la felicidad
-------------------------
Según el análisis de correlación, los factores que más influyen en la felicidad son:

1. PIB per cápita → Principal determinante, asociado al acceso a recursos materiales,
   oportunidades económicas y estabilidad financiera.
2. Esperanza de vida / salud → Refleja la importancia del sistema de salud y la calidad de vida.
3. Apoyo social → La existencia de redes familiares y comunitarias sólidas incrementa el bienestar.

Otros factores como la libertad individual y la generosidad también muestran relación positiva,
aunque en menor medida.
"""