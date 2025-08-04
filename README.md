#Análisis de Reporte Mundial de Felicidad (World Happiness Report).

##Descripción del Proyecto
Este proyecto realiza una exploración inicial y análisis básico de un conjunto de datos (dataset) que contiene indicadores de felicidad, desarrollo y bienestar de distintos países alrededor del mundo. El objetivo de este primer avence es conocer la estructura de los datos, identificar los valores faltantes, tipos de datos y hacer una visualización básica de la distribución regional de los países.

##Dataset Seleccionado
En este primer avance se utilizaron archivos CSV provenientes de una carpeta "archive" que contiene datos relacionados con el World Happiness Report. Estos archivos fueron cargados y concatenados para realizar un análisis conjunto.

Fuente: [World Happiness Report] (https://www.kaggle.com/datasets/unsdsn/world-happiness)

##Estructura del Proyecto
proyecto-final/
├── data/
│ ├── 2015.csv
│ ├── 2016.csv
│ ├── 2017.csv
│ ├── 2018.csv
│ └── 2019.csv
├── src/
│ └── cargar_data.py
├── docs/
│ └── plan_analisis.md
├── README.md

##Instruccines de Ejecución
Antes de ejecutar el proyecto:
**Importante**: Se recomienda abrir el proyecto-final como raíz del proyecto. Si no se hace así, el código podría no ejecutarse correctamente debido a problemas con las rutas relativas.

Pasos para ejecutar el proyecto:
1. Instalar las librerías: pandas (manipulación de datos) y matplotlib (gráfica)
2. Para instalar pandas con el siguiente comando para Windows: pip install pandas
3. Para instalar matplotlib con el siguiente comando para Windows: pip install matplotlib
4. Ejecutar el script principal (cargar_data.py) ubicada en src; este script cargará todos los archivos csv de la carpeta data, se realizará el análisis y se mostrará en consola la información básica y un gráfico con la cantidad de países por región.

##Autores
Kianny Pérez Hernández
Yerlin Vargas
