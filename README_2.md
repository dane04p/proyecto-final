## Análisis de Felicidad y Corrupción (World Happiness Report)

Este script descarga y analiza automáticamente el World Happiness Report, mostrando cómo la percepción de corrupción afecta la felicidad de 
los países y cuáles factores influyen más en ella.

### 1. Requisitos

Tener Python 3.10 o superior instalado.

Descargar su token de Kaggle (kaggle.json) desde Kaggle y colocarlo en la siguiente ruta:

C:\Users\<SU_USUARIO>\.kaggle\kaggle.json


Instalar las librerías necesarias:

pip install pandas numpy matplotlib plotly kaggle scipy

### 2. Ejecución

Abra la terminal o PowerShell en la carpeta donde se encuentra el script.

Ejecute:

python nombre_del_script.py

### 3. Funcionalidades del script

- Descarga y preparación del dataset desde Kaggle.

- Análisis de corrupción vs felicidad:

- Agrupa los países por cuartiles de percepción de corrupción.

- Calcula y muestra la felicidad promedio por cada cuartil.

- Genera un gráfico de barras.

- Calcula la correlación Pearson entre corrupción y felicidad.

- Top países más felices:

- Muestra en consola los 10 países con mayor puntaje de felicidad.

- Mapa mundial de felicidad:

- Muestra un mapa interactivo coloreado según el puntaje de felicidad de cada país.

- Radar de factores que influyen en la felicidad:

- Calcula la correlación de distintos factores (PIB, salud, apoyo social, libertad, generosidad) con la felicidad.

- Genera un gráfico radar interactivo mostrando la influencia de cada factor.

- Indica cuál es el factor que más influye en la felicidad.

### 4. Estructura de carpetas

El script crea automáticamente la siguiente estructura:

<carpeta_padre_del_script>/data/world_happiness/


data/ → Carpeta general para los datos.

world_happiness/ → Carpeta donde se guardará el CSV del dataset.

### 5. Resultados esperados

Gráfico de barras: felicidad promedio según cuartiles de corrupción.

Consola: tabla con medias, desviaciones y conteo por cuartil, valor de correlación Pearson y top países más felices.

Mapa interactivo: felicidad por país.

Radar interactivo: factores que más influyen en la felicidad y el factor principal.

### 6. Problemas comunes y soluciones

Error FileNotFoundError de Kaggle:
Verifique que el archivo kaggle.json esté en la ruta correcta y que la API de Kaggle esté configurada correctamente.

Librerías faltantes:
Asegúrese de tener instaladas las librerías pandas, numpy, matplotlib, plotly, scipy y kaggle.

Permisos al mover archivos:
Ejecute Python con los permisos adecuados o cambie la carpeta de trabajo si es necesario.
