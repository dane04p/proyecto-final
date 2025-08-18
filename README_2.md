## Análisis de Reporte Mundial de Felicidad (World Happiness Report).
### Descripción del Proyecto
Este script automatiza el análisis del World Happiness Report al descargar y organizar los datos desde Kaggle, explorar sus características principales y desarrollar un estudio sobre la relación entre corrupción y felicidad en los países. Asimismo, identifica a las naciones más felices, determina los tres principales factores que influyen en el puntaje de felicidad (PIB per cápita, esperanza de vida y apoyo social) y analiza si existe una relación directa entre un mayor puntaje de felicidad y una mayor esperanza de vida, apoyándose en visualizaciones y métricas estadísticas. 

### Dataset Seleccionado
El dataset seleccionado es el World Happiness Report, que reúne información de más de 150 países sobre bienestar y calidad de vida. Incluye variables como Happiness Score (puntaje de felicidad), GDP per capita (PIB per cápita), Healthy life expectancy (esperanza de vida saludable), Social support (apoyo social), Freedom (libertad de decisión), Generosity y Perceptions of corruption, lo que permite identificar los principales factores asociados a la felicidad.

Fuente: [World Happiness Report] (https://www.kaggle.com/datasets/unsdsn/world-happiness)

Estructura del Proyecto
proyecto-final/

├── data/ │ ├── world_hapiness/ │ ├── 2015.csv │ ├── 2016.csv │ ├── 2017.csv │ ├── 2018.csv │ └── 2019.csv ├── src/ │ └── codigo.py ├── docs/ │ └── plan_analisis.md ├── README.md

## Instruccines de Ejecución
Antes de ejecutar el proyecto:

Importante: Se recomienda abrir el proyecto-final como raíz del proyecto. Si no se hace así, el código podría no ejecutarse correctamente debido a problemas con las rutas relativas.

Pasos para ejecutar el proyecto:

Tener Python 3.10 o superior instalado.
Descargar su token de Kaggle (kaggle.json) desde Kaggle y colocarlo en la siguiente ruta:
C:\Users\<SU_USUARIO>\.kaggle\kaggle.json
Instalar las librerías necesarias: pip install pandas numpy matplotlib plotly kaggle scipy
PAra ejecutar el script abra la terminal o PowerShell en la carpeta donde se encuentra el script.
Ejecute: python nombre_del_script.py

### Funcionalidades del script

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

### Estructura de carpetas

El script crea automáticamente la siguiente estructura:

<carpeta_padre_del_script>/data/world_happiness/

data/ → Carpeta general para los datos.

world_happiness/ → Carpeta donde se guardará el CSV del dataset.

### Resultados esperados

Gráfico de barras: felicidad promedio según cuartiles de corrupción.

Consola: tabla con medias, desviaciones y conteo por cuartil, valor de correlación Pearson y top países más felices.

Mapa interactivo: felicidad por país.

Radar interactivo: factores que más influyen en la felicidad y el factor principal.

### Autores
Kianny Pérez Hernández y Yerlin Vargas Solano


Librerías faltantes:
Asegúrese de tener instaladas las librerías pandas, numpy, matplotlib, plotly, scipy y kaggle.

Permisos al mover archivos:
Ejecute Python con los permisos adecuados o cambie la carpeta de trabajo si es necesario.
