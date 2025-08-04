import glob
import pandas as pd
import matplotlib.pyplot as plt

#ruta donde se encuentran los archivos csv
filenames = glob.glob("/data/*.csv")

archivos_csv = []
#se carga cada archivo csv y se almacena en la lista [archivos_csv]
for filename in filenames:
    try:
        data = pd.read_csv(filename)
        archivos_csv.append(data)
        print(f"Archivo cargado correctamente: {filename}")
    except Exception as e:
        print(f"Error al cargar: {filename} por: {e}")
        
#se concatena todos los dataframes en uno solo   
big_frame = pd.concat(archivos_csv, ignore_index=True)

print(f"\nTotal de archivos procesados: {len(archivos_csv)}")

#se muestra la información del dataframe
print("\nInfo del dataframe: ")
info = big_frame.info()

print("\nResumen estadístico: ")
describe = big_frame.describe()
print(describe)

forma = big_frame.shape
print(f"\nForma del dataframe: {forma}")
    
print("\nTipos de datos: ")
tipos_datos = big_frame.dtypes
print(tipos_datos)

print("\nValores nulos del dataframe: ")
valores_nulos = big_frame.isnull().sum()
print(valores_nulos)

print("\nPrimeras 10 filas del dataset: ")
filas = big_frame.head(10)
print(filas)

#se vusualiza por medio de una grafica usando matplotlib la cantidad de países por región
if 'Region' in big_frame.columns:
    big_frame['Region'].value_counts().plot(kind='bar')
    plt.title("Cantidad de paises por región")
    plt.xlabel("Región")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()