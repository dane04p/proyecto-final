import os
import zipfile
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------
# 0. Descarga y carga del dataset desde Kaggle
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

    # Ejecutar descarga con subprocess (más seguro que os.system)
    result = subprocess.run([
        "kaggle", "datasets", "download",
        "-d", "unsdsn/world-happiness",
        "-p", work_dir
    ], capture_output=True, text=True, shell=True)

    if result.returncode != 0:
        print("❌ Error en la descarga:", result.stderr)
        raise RuntimeError("La descarga con Kaggle falló. Verifica que kaggle esté instalado y autenticado.")

    # Buscar el archivo ZIP descargado
    zip_files = [f for f in os.listdir(work_dir) if f.endswith(".zip")]
    if not zip_files:
        raise FileNotFoundError("No se encontró ningún archivo ZIP descargado.")

    zip_path = os.path.join(work_dir, zip_files[0])
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)

    # Listar los archivos CSV extraídos
    archivos = [f for f in os.listdir(dest_path) if f.endswith(".csv")]
    print("📂 Archivos descargados:", archivos)

    if not archivos:
        raise FileNotFoundError("No se encontraron archivos CSV en la carpeta de destino.")

    return {f.split(".")[0]: os.path.join(dest_path, f) for f in archivos}


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
        if 2015 <= year <= 2019:
            df = pd.read_csv(path)
            df_n = normalizar_columnas(df, year)
            df_n["Year"] = year
            data.append(df_n)
    if not data:
        raise ValueError("No se pudieron cargar datos de los archivos CSV.")
    return pd.concat(data, ignore_index=True)

# -----------------------------------------------------------
# 1) Pregunta 1 – Factores principales que explican la felicidad
# -----------------------------------------------------------

def analizar_factores(df):
    corr = df.corr(numeric_only=True)["Happiness"].drop("Happiness").sort_values(ascending=False)
    print("\n🔍 Correlaciones con la felicidad:\n", corr)

    top3 = corr.head(3)
    plt.figure(figsize=(6,4))
    top3.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Top 3 factores más influyentes en la felicidad")
    plt.ylabel("Correlación con felicidad")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
    return top3

# -----------------------------------------------------------
# 2) Pregunta 2 – Evolución de la felicidad en el tiempo
# -----------------------------------------------------------

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

# -----------------------------------------------------------
# 3) Pregunta 3 – Corrupción vs felicidad
# -----------------------------------------------------------

def analizar_corrupcion(df):
    df["corrup_real"] = 1 - df["Corruption"]
    df['corr_group'] = pd.qcut(
        df['corrup_real'],
        q=4,
        labels=['Muy baja', 'Baja', 'Alta', 'Muy alta'],
        duplicates='drop'
    )

    grouped = df.groupby('corr_group')["Happiness"].agg(['mean','std','count']).reset_index()
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
        r, p = pearsonr(df['corrup_real'], df["Happiness"])
        print(f"Correlación Pearson corrupción vs felicidad: r = {r:.3f}, p = {p:.3e}")
    except Exception:
        r = np.corrcoef(df['corrup_real'], df["Happiness"])[0,1]
        print(f"Correlación (sin scipy) ≈ r = {r:.3f}")

# -----------------------------------------------------------
# 4) Pregunta 4 – Top países + mapa + radar de factores
# -----------------------------------------------------------

def mostrar_top_paises(df, n=10):
    top_countries = df[["Country", "Happiness"]].sort_values("Happiness", ascending=False).head(n)
    print(f"\n🌍 Top {n} países más felices:\n", top_countries)
    return top_countries


def graficar_mapa(df):
    fig_map = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Happiness",
        color_continuous_scale="Turbo",
        title="🌍 Índice de felicidad por país",
        hover_name="Country",
        hover_data={"Happiness":':.2f'}
    )
    fig_map.update_layout(
        geo=dict(showframe=False, showcoastlines=True, projection_type="natural earth"),
        title_font=dict(size=18, family="Arial", color="black"),
        coloraxis_colorbar=dict(title="Felicidad", ticks="outside")
    )
    fig_map.show()


def graficar_radar(df):
    factors = [c for c in ["GDP","SocialSupport","LifeExpectancy","Freedom","Generosity"] if c in df.columns]
    radar_data = df[factors + ["Happiness"]].corr()["Happiness"].drop("Happiness")

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
        polar=dict(radialaxis=dict(visible=True, range=[-1,1])),
        title="📊 Factores que influyen en la felicidad",
        showlegend=False
    )
    fig_radar.show()
    print(f"\n✅ El factor que más influye en la felicidad es: {radar_data.abs().idxmax()}")

# -----------------------------------------------------------
# Ejecución principal
# -----------------------------------------------------------
if __name__ == "__main__":
    work_dir, dest_path = preparar_directorios()
    dict_files = descargar_dataset(work_dir, dest_path)
    df_all = cargar_datos(dict_files)

    print("Dataset unificado con shape:", df_all.shape)

    # Pregunta 1
    analizar_factores(df_all)

    # Pregunta 2
    analizar_tendencias(df_all)

    # Pregunta 3
    analizar_corrupcion(df_all)

    # Pregunta 4
    mostrar_top_paises(df_all)
    graficar_mapa(df_all)
    graficar_radar(df_all)

# -----------------------------------------------------------
# Análisis de resultados
# -----------------------------------------------------------

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

Pregunta 3. ¿Puede la percepción de la corrupción de un país tener efectos negativos en la 
felicidad de sus habitantes?
-------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------

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