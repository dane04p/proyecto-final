#Análisis de Reporte Mundial de Felicidad (World Happiness Report)

##Proyecto final Técnico Básico en Python

##Primer entrega

###Justificación de elección del dataset

<p>
Para el siguiente proyecto se eligió el dataset: Reporte Mundial de Felicidad. Esto debido a que es una base de datos robusta que contiene información real de aproximadamente 155 países al rededor del mundo.

La cual a través de su contenido permite acceder a distintas variables como lo son: el puntaje de felicidad, el PIB per cápita, apoyo social o familia, la esperanza de vida entre otros.

Indicadores que al correlacionarlos contra el puntaje de felicidad pueden brindar información de mucho valor para el desarollo social, político y psicológico de una nación. Lo que lo convierte en un tema de gran interés en la actualidad, en un mundo que presenta un aumento importante en la cantidad de enfermedades mentales (Global Burden of Disease Study, 2021).

Por lo que además de ser información muy versatil para la elaboración de distintos tipos de visualizaciones, también permite explorar diferentes escenarios y conocer por ejemplo cuáles son los principales indicadores que influyen en la felicidad de las personas, la lista de los paíces más felices e identificar que variable es la que tiene mayor impacto en dichas estadísticas.
</p>

###Plan de Análisis

####Preguntas de Investigación
<p>
A través del presente análisis se pretenden responder las siguientes preguntas:

**1.**	¿Cuáles son los 3 principales factores que influyen en el puntaje de felicidad de un país?
**2.**	¿Existe una relación directa entre un mayor puntaje de felicidad y una mayor esperanza de vida?
**3.**	¿Puede la percepción de la corrupción de un país tener efectos negativos en la felicidad de sus habitantes?
**4.**	¿Cuáles son los países más felices dentro de la base de datos y qué factores explican esa felicidad?
</p>

####Hipótesis iniciales
<p>
Con el objetivo de elaborar una base a partir de la cual comenzar a generar relaciones entre la variables y lograr comprender mejor los resultados, se planteó una hipótesis inicial para cada una de las preguntas que se desea contestar. Las cuales se enumeran a continuación:

1. Los 3 indicadores con mayor influencia en el puntaje de felicidad de un país son: El PIB per capita, el apoyo social y la esperanza de vida.
2. Sí existe una relación directa entre la esperanza de vida y el puntaje felicidad. Lo que quiere decir que a mayor felicidad mayor esperanza de vida y visceversa.
3. Sí, a mayor desconfianza en el gobierno menor puntaje de felicidad tendrá dicho país.
4. Los países más felices de la base de datos son los que presentan un mayor PIB per capita.
</p>

####Ejemplo de visualizaciones a utilizar
<p>
Para generar un análisis completo de la información y lograr responder las preguntas planteadas se crearán distintas visualizaciones.

Una de ellas es la elaboración de un ***diagrama de correlación***, donde al comparar el puntaje de felicidad versus la demás variables se podrá observar cuál de estas presenta una mayor influencia ya sea positiva o negativa en la felicidad de las personas.

Para la segunda hipótesis se generará un ***gráfico de dispersión*** que muestre cómo es el comportamiento entre la esperanza de vida y la percepción de felicidad, tratando de indentificar una tendencia positiva entre estos.  Este punto se podrá reforzar por medio de un ***gráfico lineal*** donde además se visualice el comportamiento de ambas variables a través del tiempo y la existencia de posibles patrones.

Por otro lado, con ***gráficos de barras*** se compararán las variables de percepción de la corrupción versus el grado de felicidad, lo que permitirá entender si estas se encuentran directamente relacionadas y si el crecimiento de una provoca la disminución de la otra.

Finalmente, se pretende realizar un ***mapa geográfico*** donde a través de la coloración de los países se logre observar cuál es el orden de felicidad de estos. Y por medio de un ***gráfico radar*** determinar cuales son los factores que tienen una mayor influencia en dicha felicidad. Logrando determinar así si el factor número 1 es el PIB per capita tal como se esperaba.
</p>

####Metodología

Para la ejecución del proyecto final se divide la metodología en x pasos:
- Descarga y análisis de los datos: Se creará un código en Python que permita al usuario descargar, limpiar y realizar una exploración rápida de los tipos de datos y comportamiento de las variables.
- Desarrollo de hipótesis: A partir de la información encontrada se determinarán las preguntas que se desean responder y se plantearán las hipótesis iniciales sobre las cuales basar el análisis.
- Elaboración de visualizaciones: Se probará si las visualizaciones planteadas brindan los resultados esperados por medio de la utilización de distintas librerias como Pandas, Matplotlib, Folium, etc.  Se agregará un análisis de cada uno de los gráficos y mapas elaborados.
- Conclusiones: A partir de los resultados obtenidos se concluirá si las hipótesis planteadas se cumplen o no se cumplen y se responderá con base en los gráficos y mapas las preguntas elaboradas.