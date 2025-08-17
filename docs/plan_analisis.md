# Análisis de Reporte Mundial de Felicidad (World Happiness Report)

## Proyecto final Técnico Básico en Python

## Primer entrega

### Justificación de elección del dataset

<p>
Para el siguiente proyecto se eligió el dataset: Reporte Mundial de Felicidad (Singhlo, 2023). Esto debido a que es una base de datos robusta que contiene información real de aproximadamente 155 países al rededor del mundo.

La cual a través de su contenido permite acceder a distintas variables como lo son: el puntaje de felicidad, el PIB per cápita, apoyo social o familia, la esperanza de vida entre otros.

Indicadores que al correlacionarlos contra el puntaje de felicidad pueden brindar información de mucho valor para el desarollo social, político y psicológico de una nación. Lo que lo convierte en un tema de gran interés en la actualidad, en un mundo que presenta un aumento importante en la cantidad de enfermedades mentales (Global Burden of Disease Study, 2025).

Por lo que además de ser información muy versatil para la elaboración de distintos tipos de visualizaciones, también permite explorar diferentes escenarios y conocer por ejemplo cuáles son los principales indicadores que influyen en la felicidad de las personas, la lista de los paíces más felices e identificar que variable es la que tiene mayor impacto en dichas estadísticas.
</p>

### Plan de Análisis

#### Preguntas de Investigación.
<p>
A través del presente análisis se pretenden responder las siguientes preguntas:

1.	¿Cuáles son los 3 principales factores que influyen en el puntaje de felicidad de un país?
2.	¿Existe una relación directa entre un mayor puntaje de felicidad y una mayor esperanza de vida?
3.	¿Puede la percepción de la corrupción de un país tener efectos negativos en la felicidad de sus habitantes?
4.	¿Cuáles son los países más felices dentro de la base de datos y qué factores explican esa felicidad?
</p>

#### Hipótesis iniciales.
<p>
Con el objetivo de elaborar una base a partir de la cual comenzar a generar relaciones entre la variables y lograr comprender mejor los resultados, se planteó una hipótesis inicial para cada una de las preguntas que se desea contestar. Las cuales se enumeran a continuación:

1. Los 3 indicadores con mayor influencia en el puntaje de felicidad de un país son: El PIB per capita, el apoyo social y la esperanza de vida.
2. Sí existe una relación directa entre la esperanza de vida y el puntaje felicidad. Lo que quiere decir que a mayor felicidad mayor esperanza de vida y visceversa.
3. Sí, a mayor desconfianza en el gobierno menor puntaje de felicidad tendrá dicho país.
4. Los países más felices de la base de datos son los que presentan un mayor PIB per capita.
</p>

#### Ejemplo de visualizaciones a utilizar.
<p>
Para generar un análisis completo de la información y lograr responder las preguntas planteadas se crearán distintas visualizaciones.

Una de ellas es la elaboración de un ***diagrama de correlación***, donde al comparar el puntaje de felicidad versus la demás variables se podrá observar cuál de estas presenta una mayor influencia ya sea positiva o negativa en la felicidad de las personas.

Para la segunda hipótesis se generará un ***gráfico de dispersión*** que muestre cómo es el comportamiento entre la esperanza de vida y la percepción de felicidad, tratando de indentificar una tendencia positiva entre estos.  Este punto se podrá reforzar por medio de un ***gráfico lineal*** donde además se visualice el comportamiento de ambas variables a través del tiempo y la existencia de posibles patrones.

Por otro lado, con ***gráficos de barras*** se compararán las variables de percepción de la corrupción versus el grado de felicidad, lo que permitirá entender si estas se encuentran directamente relacionadas y si el crecimiento de una provoca la disminución de la otra.

Finalmente, se pretende realizar un ***mapa geográfico*** donde a través de la coloración de los países se logre observar cuál es el orden de felicidad de estos. Y por medio de un ***gráfico radar*** determinar cuales son los factores que tienen una mayor influencia en dicha felicidad. Logrando determinar así si el factor número 1 es el PIB per capita tal como se esperaba.
</p>

#### Metodología.

Para la ejecución del proyecto final se divide la metodología en 4 pasos:
- Descarga y análisis de los datos: Se creará un código en Python que permita al usuario descargar, limpiar y realizar una exploración rápida de los tipos de datos y comportamiento de las variables.
- Desarrollo de hipótesis: A partir de la información encontrada se determinarán las preguntas que se desean responder y se plantearán las hipótesis iniciales sobre las cuales basar el análisis.
- Elaboración de visualizaciones: Se probará si las visualizaciones planteadas brindan los resultados esperados por medio de la utilización de distintas librerias como Pandas, Matplotlib, Folium, etc.  Se agregará un análisis de cada uno de los gráficos y mapas elaborados.
- Conclusiones: A partir de los resultados obtenidos se concluirá si las hipótesis planteadas se cumplen o no se cumplen y se responderá con base en los gráficos y mapas las preguntas elaboradas.

#### Descarga y análisis de datos 

Se implementó un conjunto de funciones en Python para descargar, organizar y preparar el dataset del World Happiness Report. Se crearon las carpetas necesarias para almacenar los archivos, luego, por medio del API de Kaggle se descargó el dataset de interés, se realizó un análisis general de los datos. Seguidamente, se cargó el archivo, identificando automáticamente las columnas con la información necasaria para responder las preguntas e hipótesis planteadas. Se realizaron las visualizaciones correspondientes permitiendo el análisis de los datos y la generación de conclusiones. 

#### Análisis de resultados
Pregunta 1 (P1):
Pregunta 2 (P2):

Pregunta 3 (P3): ¿Puede la percepción de la corrupción de un país tener efectos negativos en la felicidad de sus habitantes?

Se realizó una correlación de Pearson para identificar si existe una correalción estadisticamente significativa que demuestre
que los niveles de corrupción tienen un efecto negativo en la felicidad de los habitantes de los países. 

                              Gráfico 3. Felicidad promedio según niveles de corrupción
<img width="800" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/28114810-3adb-472b-ae8b-0bbc887db0ab" />


Dicho análisis de correlación mostró un valor de p ≈ 2.76e-07, menor que 0.05, lo que indica que la relación observada es estadísticamente significativa y poco probable que se deba al azar.

El coeficiente de correlación de r ≈ -0.395 revela una relación negativa de magnitud moderada, lo que significa que a medida que aumenta la percepción de corrupción, disminuye el puntaje de felicidad promedio de los países.

La tendencia se mantiene incluso considerando la variación entre diferentes cuartiles de felicidad, confirmando que el efecto no es aislado de ciertos grupos de países.

##### Conclusión P3:
Se rechaaza la hipotesis nula ya que los resultados respaldan la hipótesis alternativa. La percepción de corrupción tiene
un impacto negativo en la felicidad de los habitantes, siendo un factor relevante para el bienestar social y económico de 
los países.


Pregunta 4 (P4): ¿Cuáles son los países más felices y qué factores explican esa felicidad?

Para conocer los países con mayor rango de felicidad se agregó una línea de código que muestra el top 10 de estos países, que se muestran a continuacuón:

<img width="813" height="525" alt="Figure_2" src="https://github.com/user-attachments/assets/6a17eed6-5770-427d-a65b-a845fce04de9" />
                              Figura X. Top 10 de países más felices


<img width="1256" height="596" alt="Figure_3" src="https://github.com/user-attachments/assets/420294d8-109f-4d6e-a31e-691f010e5e1c" />
                   Figura X. Mapa de distribución de países según rango de felicidad

                   
Como se puede observar Suiza, Islandia y Dinamarca lideran el ranking, lo que coincide con estudios previos sobre felicidad mundial.
Este patrón sugiere que sociedades con seguridad económica, baja corrupción y fuertes redes de apoyo social tienden a alcanzar mayores niveles de felicidad.


Factores con mayor influencia: Para identificar los factores que tienen una mayor influencia en la felicidad de los países se realizó el gráfico que se muestra a continuación.

<img width="1256" height="596" alt="Figure_4" src="https://github.com/user-attachments/assets/6419b1ad-ce84-4ffd-b527-b1ddfe01e1c5" />
                  Figura X. Gráfico araña de los factores que influyen en la felicidad de los países
                  
Como se puede observar en la Figura X el PIB per carpita es el que muestra valores mas cercanos a 1, seguido por la Familia la Esperanza de vida y la Libertad de expresión.

- PIB per cápita: Principal determinante de la felicidad, vinculado a recursos materiales, oportunidades económicas y estabilidad financiera.

- Esperanza de vida / salud: La calidad del sistema de salud y la longevidad influyen directamente en el bienestar.

- Apoyo social: Redes familiares y comunitarias fuertes incrementan la felicidad.

- Otros factores: Libertad individual y generosidad muestran relación positiva, aunque su efecto es menor en comparación con los anteriores.

##### Conclusión P4:

Se acepta la hipótesis alternativa que indica que los países con mayor felicidad son los que tienen un mayor valor de PIB per capita. No obstante, la felicidad en los países no depende únicamente de factores económicos, sino también de la calidad social y salud pública.
La combinación de recursos económicos, baja corrupción y redes de apoyo social constituye un patrón que explica por qué los países nórdicos se posicionan consistentemente en los primeros lugares del ranking de felicidad.

#### Bibliografía.

Global Burden of Disease Collaborative Network. (2025). Global burden of mental disorders in 204 countries and territories, 1990–2021: results from the Global Burden of Disease Study 2021. BMC Psychiatry, 25, Article — 06932. https://doi.org/10.1186/s12888-025-06932-y

Singhlo, A. P. (2023). World Happiness Report 2023 [Archivo de datos]. Kaggle. https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2023
