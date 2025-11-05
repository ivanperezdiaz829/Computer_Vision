<!-- @import "design/style.css" -->

# **CUARTO CONJUNTO DE TAREAS A REALIZAR**

## Índice

- [Preparativos para las tareas](#preparativos-para-las-tareas)
- [Análisis y clasificación de monedas](#análisis-y-clasificación-de-monedas)
- [Modelo de clasificador de imágenes](#modelo-clasificador-de-objetos-en-una-imagen)
- [Fuentes y Documentación](#fuentes-y-documentación)

La práctica consiste en el entrenamiento de un dataset propio con matrículas de coches haciendo uso de YOLO que además posee detección de diferentes clases ya entrenadas (para el trabajo se van a usar las clases **"person"**, **"car"**, **"motorcycle"**, **"truck"**, **"bus"**).

Una vez entrenada la Red Neuronal, se va a testear la calidad de la detección del texto de las mismas haciendo uso de un **OCR** y de un **VLM** y comparar los resultados obtenidos entre ambos.

## Preparativos para la tarea

Para realizar el ejercicio en cuestión, es necesario crear un nuevo environmet de python dado que algunos de los paquetes necesarios pueden crear conflictos con las dependencias ya instaladas en el environment anterior. Para ello y haciendo uso del **Anaconda Prompt** se va a crear un nuevo environment de nombre **VC_P4**.

```bash
conda create --name VC_P4 python=3.9.5
conda activate VC_P4
```

De manera adicional, se han de instalar las dependencias necesarias para llevar a cabo la práctica haciendo uso del nuevo environment.

```bash
pip install ultralytics
pip install lapx
pip install pytesseract
pip install einops
pip install timm
pip install transformers
```

Como en el entrenamiento se va a hacer uso de una tarjeta gráfica NVIDIA (con CUDA) se va a instalar CUDAv11.6.

```bash
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
```

Con las dependencias instaladas, se procede a empezar a explicar la arquitectura del directorio de la práctica y la creación del *dataset* de las matrículas.

## Arquitectura del directorio

El directorio del proyecto contiene varios subdirectorios y ficheros que componen la información necesaria para la creación y correcto desarrollo de la práctica.

<h4 style="text-decoration: underline; font-weight: bold">Ficheros:</h4>

**[Exercises_P4.ipynb:](Exercises_P4.ipynb)** Es el notebook de python en donde se lleva a cabo el entrenamiento de la Red Neuronal, el procesado del vídeo para la detección de matrículas, personas y vehículos, el procesado con el **OCR** y la **VLM** para obtener la información de las matrículas y las comparaciones pertinentes.

**[data.yaml:](data.yaml)** Es el fichero que define las clases a aprender y las ubicaciones de las imágenes de entrenamiento, validación y test. Las imágenes y sus *labels* están subidas a una carpeta privada en línea, para acceder a ella, solicite permiso para acceder vía correo electrónico: ivanperezdiaz829@gmail.com

# SEGUIR PONIENDO EL RESTO DE COSAS

# EXPLICACIÓN DE IMÁGENES DE ENTRENAMIENTO

## Curva F1-Confianza:

Es una de las métricas más importantes para evaluar el modelo de detección de objetos entrenado y dice cuál es el mejor "umbral de confianza" a usar en el modelo.

<img src="/VC_P4/runs/train_custom/exp2/BoxF1_curve.png">

**Eje Y:** El valor va de 0.0 a 1.0 y es un equilibrio entre **precisión** (número de matrículas detectadas correctamente) y el **recall** (matrículas que hay en la imagen y han sido detectadas). El resultado obtenido de 0.92 es casi perfecto.

**Eje X:** La confianza va de 0.0 a 1.0 y es el umbral de seguridad que se le exige al modelo para que muestre una detección. Con una confianza baja (p.ej: 0.1) le dices al modelo que te muestre todo lo que creas que puede ser matrícula aunque solo esté seguro a un 10%, por otro lado, con una confuanza alta se le dice al modelo que solo te muestre las matrículas que esté completamente seguro de que lo son.

**Resultados y conclusión:** El texto en la leyenda tiene la respuesta más importante (**all classes 0.92 at 0.452). Significa que el modelo obtiene un rendimiento óptimo (0.92) cuando se usa un umbral de confianza de 0.452. El desplome del final de la gráfica es porque al pedirle mucho al modelo en cuanto a confianza, las detecciones decaen.

## Labels:

Esta gráfica analiza la composición del conjunto de datos a partir de los *labels*. No mide el rendimiento del modelo sion que da una radiografía de los datos que se han usado para entrenarlo.

<img src="/VC_P4/runs/train_custom/exp2/labels.jpg">

**Gráfica superior izquierda (Instances):** Es un gráfico de barras que cuenta cuántas instancias hay de cada clase (en este caso solo matrículas).

**Gráfica inferior izquierda (Ubicación x, y):** Es un mapa de calor de las posiciones centrales de todas las matrículas (posición normalizada). El color azul oscuro muestra donde se concentran la mayoría de las matrículas. En este caso, están fuertemente agrupadas en el centro de la imagen. Esto implica que el modelo será muy bueno encontrando matrículas en el centro de la imagen pero que podría tener dificultades para encontrar matrículas en los bordes de las mismas.

**Gráfica inferior derecha (Tamaño):** Es un mapa de calor del tamaño (ancho y alto) de las matrículas (normalizado). El hotspot (puntos más intensos) están pegados en laesquina inferior izquierda significando que la inmensa mayoría de las matrículas son pequeñas en realación con el tamaño total de la imagen. Esto implica que el modelo será experto en detectar matrículas pequeñas pero podría no generalizar tan bien si hay alguna matrícula muy grande o que ocupe toda la pantalla.

**Gráfica superior derecha (Boxes):** Es una superposición de todas las *bounding boxes* del dataset, centradas en el mismo punto para comparar formas. Se confirma que casi todas las cajas están agrupadas en el centro y que hay una variedad en los *aspect ratios* en cuanto a la anchura pero todas tienden a ser pequeñas.

















## Fuentes y Documentación

- **Internet:** Se ha utilizado internet para la búsqueda de información acerca de la segmentación y diferentes métricas y características para aplicar las diferentes técnicas ([SMACC: A System for Microplastics Automatic Counting and Classification](https://ieeexplore.ieee.org/document/8976153)) con el objetivo de mejorar la precisión del modelo ejecutado en la [tarea2](#tarea-2). Además, se han buscado los *"emojis"* para los mensajes de creación de imagenes en dicha tarea.

- **Inteligencia Artificial Generativa (ChatGPT, Gemini):** Se ha utilizado la IA para intentar mejorar la precisión del modelo de obtención de características (desempeño nulo/deficiente de los resultados obtenidos con la IA).

- **Enlaces:**
    - https://ieeexplore.ieee.org/document/8976153
    - https://learnopencv.com/otsu-thresholding-with-opencv/
    - https://chatgpt.com/
    - https://gemini.google.com
    - https://www.investopedia.com/terms/r/returnoninvestment.asp


Para más documentación referente a las tareas, véase el [Notebook](Exercises_P4.ipynb) asociado a la carpeta de la práctica en cuestión **(VC_P4)**.



