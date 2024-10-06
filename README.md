# WasteX: Optimización de Selección de Rellenos Sanitarios
WasteX es una herramienta desarrollada en Python para resolver problemas de optimización relacionados con la selección de rellenos sanitarios. El programa toma en cuenta diversos factores, como la densidad de residuos y la tasa de crecimiento, con el objetivo de minimizar las distancias recorridas por los camiones de recolección de basura y habilitar un máximo de 3 rellenos sanitarios. Este proyecto es una interfaz gráfica desarrollada con la biblioteca `Tkinter` para visualizar y optimizar la selección de rellenos sanitarios. 
## Características
- Minimización de kilómetros recorridos por los camiones.
- Consideración de densidad de residuos y tasa de crecimiento.
- Restricción en el número máximo de rellenos sanitarios habilitados.
- Visualización de mapas con coordenadas geográficas.
- Selección optimizada de localización de rellenos sanitarios.
- Interfaz interactiva con botones para controlar el comportamiento de la leyenda y los objetos visualizados.
- Dos mapas disponibles para la visualización de resultados.
## Archivos principales
- `main.py`: Archivo principal que ejecuta la interfaz gráfica.
- `Toneladas y Distancia.xlsx`: Archivo Excel que contiene las distancias entre los municipios y los rellenos sanitarios.
- `algoritmo_distancias.py`: Contiene el algoritmo que calcula las distancias óptimas para seleccionar los rellenos sanitarios.
- **Salida**: Una tupla con los números correspondientes a los tres rellenos sanitarios óptimos.
- `Longitudes_Tabla.xlsx`: Archivo Excel que contiene las coordenadas geográficas en formato grados, minutos y segundos.
- `conversion_grados.py`: Funciones que convierten las coordenadas geográficas.
- **Salida**: Una lista con las coordenadas convertidas a grados decimales, junto con las distancias relativas calculadas.
## Descripción del Código
El programa utiliza las siguientes funciones principales:
- **fun_algoritmo()**: Devuelve las mejores localizaciones para la habilitación de rellenos sanitarios en función de la minimización de distancias.
- **grados_fun()**: Convierte las coordenadas geográficas a un formato adecuado para la visualización en el mapa.
- **command_button_legend()**: Controla el comportamiento de la leyenda en la interfaz gráfica.
- **minim_fun()**: Calcula las localizaciones óptimas utilizando el algoritmo y actualiza el mapa en consecuencia.
## Estructura de la Interfaz
- La interfaz gráfica está compuesta por un `Canvas` que muestra el mapa base con las coordenadas geográficas de los posibles rellenos sanitarios.
- Los botones en la leyenda permiten interactuar con los puntos en el mapa, cambiando sus colores según su estado.
- Un botón de "Calcular localización óptima" ejecuta el algoritmo para destacar los mejores rellenos sanitarios.
## Requisitos
- `pandas`: Para manipular y leer los datos del archivo Excel.
