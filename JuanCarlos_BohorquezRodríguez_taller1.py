#!/usr/bin/env python
# coding: utf-8

# TALLER 1: CRÍTICA VISUALIZACIÓN DE DATOS

# 
# Profesora: Mónica Tatiana Gutierrez Ballen
# Juan Carlos Bohórquez Rodríguez Cod 2233159
# 
# Visualización basados en el framework de Tamara

# Las visualizaciones usadas fueron extraidas de los recursos proporcionados en el Macroproceso del Taller, link: https://www.nytimes.com/2020/06/10/learning/over-60-new-york-times-graphs-for-students-to-analyze.html

# Elegí esta visualizacion porque me llamó la atencion las cifras exorbitantes de dinero en gasto militar.

# Link visualizacion     https://www.nytimes.com/slideshow/2020/06/10/learning/graphs-charts-and-maps-from-three-years-of-whats-going-on-in-this-graph/s/MilitarySpendingLN.html

# ![image.png](attachment:image.png)
# 
# 
# 

# Framework visualización
# Qué? Por qué? Cómo?

# What ?
# Los datos que observamos son la cantidad en miles de millones de dolares que emplean los paises del mundo divididos en 8 paises y el resto del mundo en gasto militar.
# La información que deducimos es que solamente los Estados Unidos tiene un gasto de 596 miles de millones de dolares, mientras que si sumamos Gran Bretaña, Francia, Arabia Saudita, India, China, Rusia y Japon reuniriamos 567 miles de millones y el resto del mundo suma 514 miles de millones. Esta informacion nos trasmite una buena idea de quienes estan gastando militarmente mas dinero en el mundo.
# Los atributos observados son de tipo cuantitativo.
# 
# 
# 
# 
# 

# Why ?
# Acciones de alto nivel: analizar, descubrir la informacion presentada.

# How ?
# La codificacion esta relacionada con el tamaño de los circulos. No requiere interaccion.
# 

# Marca : Areas
#     

# Canal de color luminance (verde) y gris.
# Canal de area (size 2D).

# Reglas Generales:
# Cumple las reglas de Discriminabilidad ya que cada elemento es distinguible del otro, Separabilidad (some interference), Popout ya que el elemento "United States" se descaca facilmente de los otros.
# 
# 

# Mejoras posibles, en cuánto a marcas o canales, que le realizaría a la visualización: en el barplot de posicion horizontal es clara la proporcion de los datos con el tamaño de la barra, pero en cambio en el canal de area2D de los circulos no es proporcional el tamaño con el dato que está en el circulo, por esta razon mejoraría la proporcion de los circulos.
# Además usaria un canal de color para diferenciar cada pais de los 8 con un color diferente.
# Tambien parece que intentaron poner los circulos en el mapamundi en orden geográfico pero la verdad el tamaño de los circulos desvirtua el mapamundi.
# 

# In[ ]:





#                                                     

#                             

# Elegí la siguiente visualizacion porque nos muestra de manera gráfica el contagio del coronavirus con y sin contacto social.

# Link de visualizacion     https://www.nytimes.com/slideshow/2020/06/10/learning/graphs-charts-and-maps-from-three-years-of-whats-going-on-in-this-graph/s/CoronavirusTransmissionGraphLN.html

# Framework visualización Qué? Por qué? Cómo?

# What ? Los datos que observamos son la cantidad de contagios que puede exirtir desde un individuo infectado y con contacto socila comparado con un individuo que se aisla y no puede contagiar a las personas en su entorno social y esas personas a otras. Este grafico nos da una buena idea de la diferencia entre no tener contacto social y tenerlo siendo portador del virus.
# 

# What ? Tree

# Why ? Acciones de alto nivel: analizar e identificar la informacion y descubrir la informacion presentada. Ademas se debe comparar los dos gráficos (Query).

# How ? La codificacion esta relacionada el arbol. No requiere interaccion.

# Marca : lineas

# Canal de posicion vertical, canal de color.

# Reglas Generales: Cumple las reglas de Discriminabilidad porque las lineas e individuos son distinguibles, Separabilidad porque se ditinguen en posicion (fully separable), Poput porque un individuo distinto se destaca facilmente de muchos otros, tambien cumple la regla de Agrupación porque existen unas lineas de conección que trasmiten informacion de los individuos enlazados que forman un grupo distinguible.

# Mejoras posibles, en cuánto a marcas o canales, que le realizaría a la visualización: la visualizacion podria tener un mejor canal de color para distinguir mejor al grupo que no tiene contagio. Además el color de saturacion usado no me parece adecuado, yo no usaría saturacion si no canal de colores para cada linea de trasmision.  

# 

# Elegi esta visualizacion porque creo que tiene varias cosas por mejorar y ademas no es tan clara en su forma.

# Link visualizacion    https://www.nytimes.com/slideshow/2020/06/10/learning/graphs-charts-and-maps-from-three-years-of-whats-going-on-in-this-graph/s/DrugTrialsGraphLN.html

# Framework visualización Qué? Por qué? Cómo?
# 
# What ? La visualizacion que observamos nos muestra el porcentaje de medicamentos que se desaprueban despues de cada fase de investigacion hasta llegar a ser aprovados finalmente. El grafico es claro porque muestra cifras exactas.

# Why ? El usuario requiere entender bien el concepto de porcentaje, analizar las cifras e identificar el target.

# How ? No requiere interaccion del usuario. La codificacion es de "order".

# Marca: lineas y areas

# Canal: de posición horizontal, de color (azul y gris) y de canal tamaño area 2D y volumen 3D.

# Reglas Generales: Cumple las reglas de Discriminabilidad porque es ditinguible un nivel del otro, Popout aunque no es totalmente claro y tardamos en llegar al elemento "approved" un poco, No cumple la Ley de Weber ya que la percepcion de los datos es inexacta por la inclinacion de la visualizacion.

# Mejoras posibles, en cuánto a marcas o canales, que le realizaría a la visualización: la visualizacion podria mejorar en varios aspectos como canal de color ya que no usa si no un color, la parte de 3D es injustificada ya que trasmite informacion de profundidad que no es clara por falta de alineacion al igual que el barplot que tambien está desalineado, No cumple La Ley de Weber, la luminancia usada muestra un color muy debil que no es de facil lectura. Yo le mejoraria todos estos items y probablemente eligiría un barplot mas sencillo y en 2D que sea mas claro.

# In[ ]:




