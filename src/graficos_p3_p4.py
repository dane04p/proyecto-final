import kaggle  # pip install kaggle (requiere token kaggle.json en C:\Users\TU_USUARIO\.kaggle\)
#descargar token en https://www.kaggle.com/account
import zipfile
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# 1) Definir carpeta de trabajo automáticamente (subcarpeta "data" en la carpeta padre del script)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # carpeta padre
work_dir = os.path.join(base_dir, "data")                              # subcarpeta "data"
os.makedirs(work_dir, exist_ok=True)

# Carpeta destino para archivos extraídos
dest_path = os.path.join(work_dir, "world_happiness")
os.makedirs(dest_path, exist_ok=True)

# 2) Descargar dataset con Kaggle API
print("Descargando dataset desde Kaggle...")
os.system(f'kaggle datasets download -d unsdsn/world-happiness -p "{work_dir}"')

# 3) Detectar archivo descargado (puede ser ZIP o CSV)
downloaded_files = [f for f in os.listdir(work_dir) if f.startswith("world-happiness")]
if not downloaded_files:
    raise FileNotFoundError("No se encontró el dataset descargado en Kaggle.")

dataset_file = os.path.join(work_dir, downloaded_files[0])

# 4) Extraer contenido si es ZIP, o mover si es CSV
if dataset_file.endswith(".zip"):
    with zipfile.ZipFile(dataset_file, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
    print(f"Archivo ZIP descomprimido en '{dest_path}'")
elif dataset_file.endswith(".csv"):
    # Mover el CSV directamente a la carpeta destino
    new_path = os.path.join(dest_path, os.path.basename(dataset_file))
    if not os.path.exists(new_path):
        os.rename(dataset_file, new_path)
    print(f"Archivo CSV movido a '{dest_path}'")
else:
    raise ValueError(f"Formato no esperado: {dataset_file}")

# 5) Detectar y cargar CSV
files = os.listdir(dest_path)
print("Archivos disponibles:", files)

csv_file = [f for f in files if f.endswith(".csv")][0]
csv_path = os.path.join(dest_path, csv_file)

df = pd.read_csv(csv_path)
print("Columnas en el dataset:", df.columns.tolist())

# 6) Identificar columnas clave
possible_corr = [c for c in df.columns if 'corrup' in c.lower() or 'corrupt' in c.lower()]
possible_score = [c for c in df.columns if 'ladder' in c.lower() or 'score' in c.lower() or 'happiness' in c.lower()]
possible_country = [c for c in df.columns if 'country' in c.lower()]

corruption_col = possible_corr[0]
score_col = possible_score[0]
country_col = possible_country[0]

# 7) Limpiar y seleccionar datos
df = df[[country_col, corruption_col, score_col]].dropna()

# 8) Agrupar por cuartiles de corrupción
df['corr_group'] = pd.qcut(
    df[corruption_col],
    q=4,
    labels=['Muy baja', 'Baja', 'Alta', 'Muy alta'],
    duplicates='drop'
)

grouped = df.groupby('corr_group')[score_col].agg(['mean','std','count']).reset_index()
print(grouped)

# 9) Gráfico de barras
x = np.arange(len(grouped))
means = grouped['mean']

plt.figure(figsize=(8,5))
plt.bar(x, means)
plt.xticks(x, grouped['corr_group'].astype(str))
plt.xlabel('Percepción de corrupción (cuartiles)')
plt.ylabel('Puntaje de felicidad promedio')
plt.title('Felicidad promedio por nivel de percepción de corrupción')
plt.tight_layout()
plt.show()

# 10) Correlación Pearson
try:
    from scipy.stats import pearsonr
    r, p = pearsonr(df[corruption_col], df[score_col])
    print(f"Pearson r = {r:.3f}, p = {p:.3e}")
except Exception:
    r = np.corrcoef(df[corruption_col], df[score_col])[0,1]
    print(f"scipy no disponible. Correlación aproximada r = {r:.3f}")

# Análisis de resultados: Al ser el valor de p menor a 0.05, podemos concluir que existe una correlación 
# significativa entre la percepción de corrupción y el puntaje de felicidad. Que no se debe al azar.
# El valor de r indica la fuerza y dirección de esta relación. 
# En este caso al ser una correlación negativa significa que a medida que aumenta la percepción de 
# corrupción, el puntaje de felicidad tiende a disminuir. Y al ser r de 0.37 indica una correlación moderada.