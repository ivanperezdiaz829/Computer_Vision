<!-- @import "design/style.css" -->

# **CUARTO CONJUNTO DE TAREAS A REALIZAR**

## ÍNDICE

- [Preparativos para las tareas](#preparativos-para-las-tareas)
- [Análisis y clasificación de monedas](#análisis-y-clasificación-de-monedas)
- [Modelo de clasificador de imágenes](#modelo-clasificador-de-objetos-en-una-imagen)
- [Fuentes y Documentación](#fuentes-y-documentación)

La práctica consiste en el entrenamiento de un dataset propio con matrículas de coches haciendo uso de YOLO que además posee detección de diferentes clases ya entrenadas (para el trabajo se van a usar las clases **"person"**, **"car"**, **"motorcycle"**, **"truck"**, **"bus"**).

Una vez entrenada la Red Neuronal, se va a testear la calidad de la detección del texto de las mismas haciendo uso de un **OCR** y de un **VLM** y comparar los resultados obtenidos entre ambos.

## PREPARATIVOS PARA LA TAREA

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

## ARQUITECTURA DEL DIRECTORIO

El directorio del proyecto contiene varios subdirectorios y ficheros que componen la información necesaria para la creación y correcto desarrollo de la práctica.

<h4 style="text-decoration: underline; font-weight: bold">Ficheros:</h4>

**[Exercises_P4.ipynb:](Exercises_P4.ipynb)** Es el notebook de python en donde se lleva a cabo el entrenamiento de la Red Neuronal, el procesado del vídeo para la detección de matrículas, personas y vehículos, el procesado con el **OCR** y la **VLM** para obtener la información de las matrículas y las comparaciones pertinentes.

**[data.yaml:](data.yaml)** Es el fichero que define las clases a aprender y las ubicaciones de las imágenes de entrenamiento, validación y test. Las imágenes y sus *labels* están subidas a una carpeta privada en línea, para acceder a ella, solicite permiso para acceder vía correo electrónico: ivanperezdiaz829@gmail.com

**[json_to_YOLO.py:](json_to_YOLO.py)** Al usar **labelme** para el etiquetado, el formato de salida de dichas etiquetas es JSON, por lo tanto, para convertir dicha salida al formato **YOLO** se ha creado este fichero que no es más que un *script* para transformar formatos.

**[comprobar.py:](comprobar.py)** Es un pequeño *script* para comprobar que todas las imágenes del dataset poseen su label correspondiente.

<h4 style="text-decoration: underline; font-weight: bold">Directorios:</h4>

**[Resources:](/VC_P4/Resources/)** Es el directorio en donde se ubican los videos de prueba para testear el modelo de detección de matrículas así como la detección de personas y vehículas y la obtención de las matrículas mediante el uso de OCR y VLM.

**[out:](/VC_P4/out/)** Es el directorio en donde se ubican los resultados de las diferentes pruebas sobre las imágenes del dataset y sobre los videos de test.

**[runs:](/VC_P4/runs/)** Es el directorio en donde se ubican todos los gráficos y resultados del entrenamiento del modelo.

# RESULTADOS DEL POST-ENTRENAMIENTO DEL MODELO

## Curva F1-Confianza:

Es una de las métricas más importantes para evaluar el modelo de detección de objetos entrenado y dice cuál es el mejor "umbral de confianza" a usar en el modelo.

<img src="/VC_P4/runs/train_custom/exp2/BoxF1_curve.png">

**Eje Y:** El valor va de 0.0 a 1.0 y es un equilibrio entre **precisión** (número de matrículas detectadas correctamente) y el **recall** (matrículas que hay en la imagen y han sido detectadas). El resultado obtenido de 0.92 es casi perfecto.

**Eje X:** La confianza va de 0.0 a 1.0 y es el umbral de seguridad que se le exige al modelo para que muestre una detección. Con una confianza baja (p.ej: 0.1) le dices al modelo que te muestre todo lo que creas que puede ser matrícula aunque solo esté seguro a un 10%, por otro lado, con una confuanza alta se le dice al modelo que solo te muestre las matrículas que esté completamente seguro de que lo son.

**Resultados y conclusión:** El texto en la leyenda tiene la respuesta más importante (**all classes 0.92 at 0.452). Significa que el modelo obtiene un rendimiento óptimo (0.92) cuando se usa un umbral de confianza de 0.452. El desplome del final de la gráfica es porque al pedirle mucho al modelo en cuanto a confianza, las detecciones decaen.

## Curva Precisión de Confianza:

Es la gráfica que define qué tan exactas son las detecciones del modelo a medida que aumenta el umbral de confianza.

<img src="/VC_P4/runs/train_custom/exp2/BoxP_curve.png">

**Eje Y:** Representa la precisión y mide la calidad de las detecciones del modelo.

**Eje X:** Es la confianza, es decir, el umbral de seguridad que se le exige al modelo.

**Resultados y conclusión:** Los resultados ubicados en la leyenda de la imagen significan que el modelo alcanza una precisión perfecta cuando se estable un umbral de confianza al 75.2%. A diferencia de la gráfica anterior, esta es importante si el objetivo es que nunca hayan falsos positivos aunque signifique que pierda detecciones.

## Curva de Precisión-Recall:

Es la gráfica más importante ya quer resume el rendimiento completo del modelo en una sola imagen y da la métrica mAP (la más importante de todas).

<img src="/VC_P4/runs/train_custom/exp2/BoxPR_curve.png">

**Eje Y:** Es la precisión y mide la calidad de las detecciones, es decir, cuántas matrículas detectó y eran correctas. Evitar falsos positivos

**Eje X:** Es el *recall* o *exhaustividad* y mide la cantidad de detecciones. Evitar falsos negativos.

**Resultados y conclusión:** El texto de la leyenda significa lo siguiente:
- **mAP (Mean Average Precision):** Es la métrica estándar de oro para los modelos de detección de objetos. Es el área bajo la curva.
- **0.922:** El modelo posee un mAP del 92.2% lo cual es un resultado excelente.
- **@0.5:** Esto se refiere al umbral de IoU (Intersección sobre Unión). Significa que una detección solo se consideró correcta si la caja predicha por el modelo se supoerponía en un 50% o más con la caja del *label*.

## Curva de Recall-Confianza:

Es la gráfica que muestra qué tan exhaustivo es el modelo (porcentaje de matrículas reales que es capaz de encontrar) a diferentes niveles de confianza.

<img src="/VC_P4/runs/train_custom/exp2/BoxR_curve.png">

**Eje Y:** Es el *recall* y mide la cantidad de de matrículas reales encontradas por el modelo.

**Eje X:** Es la confianza, es decir, el umbral de seguridad que se le exige al modelo.

**Resultados y conslusión:** Los resultados visibles en la leyenda muestran que el modelo es capaz de alcanzar el 90% de las matrículas totales del conjunto de pruebas, es decir, hay un 10% de matrículas que el modelo nunca va a detectar.

## Matriz de confusión:

Son las detecciones tanto reales como falsas, es decir, muestra la cantidad de verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.

<img src="/VC_P4/runs/train_custom/exp2/confusion_matrix.png">

## Labels:

Esta gráfica analiza la composición del conjunto de datos a partir de los *labels*. No mide el rendimiento del modelo sion que da una radiografía de los datos que se han usado para entrenarlo.

<img src="/VC_P4/runs/train_custom/exp2/labels.jpg">

**Gráfica superior izquierda (Instances):** Es un gráfico de barras que cuenta cuántas instancias hay de cada clase (en este caso solo matrículas).

**Gráfica inferior izquierda (Ubicación x, y):** Es un mapa de calor de las posiciones centrales de todas las matrículas (posición normalizada). El color azul oscuro muestra donde se concentran la mayoría de las matrículas. En este caso, están fuertemente agrupadas en el centro de la imagen. Esto implica que el modelo será muy bueno encontrando matrículas en el centro de la imagen pero que podría tener dificultades para encontrar matrículas en los bordes de las mismas.

**Gráfica inferior derecha (Tamaño):** Es un mapa de calor del tamaño (ancho y alto) de las matrículas (normalizado). El hotspot (puntos más intensos) están pegados en laesquina inferior izquierda significando que la inmensa mayoría de las matrículas son pequeñas en realación con el tamaño total de la imagen. Esto implica que el modelo será experto en detectar matrículas pequeñas pero podría no generalizar tan bien si hay alguna matrícula muy grande o que ocupe toda la pantalla.

**Gráfica superior derecha (Boxes):** Es una superposición de todas las *bounding boxes* del dataset, centradas en el mismo punto para comparar formas. Se confirma que casi todas las cajas están agrupadas en el centro y que hay una variedad en los *aspect ratios* en cuanto a la anchura pero todas tienden a ser pequeñas.

## RESULTADOS EN VÍDEO CON OCR

Para poner a prueba el modelo entrenado para la detección de matrículas se carga tanto el modelo mencionado, como el modelo preentrenado de yolo llamado yolo11l.pt en el que se ubican las clases (entre otras) de personas, coches, camiones, buses y motos. Mencionadas clases se cargan y cada pocos frames del vídeo se ejecuta cargan los modelos con un tracking para ver el seguimiento.

En el vídeo se muestra en color verde las clases detectadas por el modelo preentrenado de YOLO, no obstante, en rojo se pueden ver las matrículas captadas por el modelo entrenado y encima la detección OCR que se obtiene haciendo uso de easyOCR.

<h4 style="text-weight: bold; text-decoration: underline">Enlace al vídeo:</h4>

[![Ver en YouTube](https://img.youtube.com/vi/VpSJ_z0vR0M/0.jpg)](https://youtu.be/VpSJ_z0vR0M)

## RESULTADOS EN VÍDEO CON VLM

De forma similar a la anterior, se va a poner a prueba el modelo entrenado para la detección de matrículas, juntándolo con el modelo preentrenado de YOLO pero haciendo uso de la detección de texto mediante una VLM.

<h4 style="text-weight: bold; text-decoration: underline">Enlace al vídeo:</h4>

[![Ver en YouTube](https://img.youtube.com/vi/v2JkFrb3D7o/0.jpg)](https://youtu.be/v2JkFrb3D7o)

## VLM VS OCR CON IMÁGENES ESTÁTICAS

Para comparar la calidad y precisión entre la detección de texto obtenida mediante OCR y VLM, se procesan las mismas 8 imágenes estáticas y se comparan los resultados (si se detecta la matrícula correctamente o no) a partir de dos ficheros CSV generados ([ocr_results.csv](/VC_P4/out/images_OCR/ocr_results.csv) y [vlm_results.csv](/VC_P4/out/images_VLM/vlm_results.csv)).


Algunas de las imágenes obtenidas después del tratamiento son las siguientes:

<h4 style="text-weight: bold; text-decoration: underline">Imagenes procesadas con OCR:</h4>

<img src="/VC_P4/out/images_OCR/0116GPD_processed.jpg">
<img src="/VC_P4/out/images_OCR/0463HVT_processed.jpeg">
<img src="/VC_P4/out/images_OCR/0116HGV_processed.jpg">

<h4 style="text-weight: bold; text-decoration: underline">Imagenes procesadas con VLM:</h4>

<img src="/VC_P4/out/images_VLM/0116GPD_processed.jpg">
<img src="/VC_P4/out/images_VLM/0463HVT_processed.jpeg">
<img src="/VC_P4/out/images_VLM/0116HGV_processed.jpg">

Los resultados tras las comparaciones son los siguientes:

```raw
--- Reporte de Comparación EasyOCR vs. VLM ---
Total de imágenes comparadas: 8

--- Porcentaje de Acierto General ---
EasyOCR: 25.00% (2/8)
VLM:     87.50% (7/8)

--- Análisis Detallado (Head-to-Head) ---
Imágenes donde AMBOS acertaron: 2
Imágenes donde AMBOS fallaron:  1
---------------------------------------------
Imágenes donde SÓLO EasyOCR acertó: 0
Imágenes where SÓLO VLM acertó:     5

--- Ejemplos donde VLM ganó (OCR falló, VLM acertó) ---
       filename ground_truth texto_ocr     texto_vlm
3   0290KWT.jpg      0290KWT      0290       0290KWT
4   0303BML.jpg      0303BML   BML0303       0303BML
5  0415JVS.jpeg      0415JVS   JVS0415       0415JVS
6   0416MLX.jpg      0416MLX       NaN       0416MLX
7  0463HVT.jpeg      0463HVT  0463HVTE  FIAT0463HVTE
```

## FUENTES Y DOCUMENTACIÓN

- **Internet:** Se ha utilizado internet para obtener información y documentación tanto de YOLO, como de *labelme* y de los OCR y las VLM.

- **Inteligencia Artificial Generativa (ChatGPT, Gemini):** Se ha utilizado la IA para la realización de los *scripts* de comprobación de *labels* y de transformación de formato JSON a YOLO.

- **Enlaces:**
    - https://huggingface.co/microsoft/Florence-2-large
    - https://github.com/JaidedAI/EasyOCR
    - https://pytorch.org/get-started/locally
    - https://chatgpt.com/
    - https://gemini.google.com
    - https://www.investopedia.com/terms/r/returnoninvestment.asp

Para más documentación referente a las tareas, véase el [Notebook](Exercises_P4.ipynb) asociado a la carpeta de la práctica en cuestión **(VC_P4)**.



