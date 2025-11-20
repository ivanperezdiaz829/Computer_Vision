<!-- @import "design/style.css" -->

# **QUINTO CONJUNTO DE TAREAS A REALIZAR**

## ÍNDICE

- [Preparativos para las tareas](#preparativos-para-las-tareas)
- [Red neuronal para el clasificador por edades](#análisis-y-clasificación-de-monedas)
- [Aplicación del clasificador sobre un filtro](#modelo-clasificador-de-objetos-en-una-imagen)
- [Filtro de estrellas con parpadeo ocular](#fuentes-y-documentación)

La práctica consiste en crear dos filtros de imagen dependiendo de ciertas características, para el primero, se entrena una red neuronal para clasificar las caras en uno de los 3 grupos seleccionados (niño, medio, anciano), aunque en un futuro se podría aumentar a 5 grupos (niño, joven, medio, adulto, anciano) mejorando así el filtro.

Para el segundo filtro, consiste en obtener una característica facial en tiempo real para crear un efecto, en este caso, se ha usado el parpadeo ocular para hacer aparecer estrellas que van creciendo y salen "disparadas" en direcciones pseudoaleatorias.

## PREPARATIVOS PARA LA TAREA

Para la realización de los filtros y del entrenamiento de la red neuronal, y con el objetivo de no crear dependencias de paquetes con proyectos anteriores, se va a crear un nuevo environment de **python 3.11.5** usando **_Anaconda Prompt_**.

```bash
conda create --name VC_P5 python=3.11.5
conda activate VC_P5
```

De manera adicional, se han de instalar las dependencias necesarias para llevar a cabo la práctica haciendo uso del nuevo environment.

```bash
pip install mediapipe
pip install matplotlib
pip install imutils
pip install mtcnn
pip install scikit-learn
pip install scikit-image
pip install pandas 
pip install tqdm
```

## RED NEURONAL PARA EL CLASIFICADOR POR EDADES



## FILTRO DE ESTRELLAS

Este proyecto implementa un filtro visual que genera pequeñas estrellas animadas cada vez que el usuario parpadea frente a la webcam.
Se utiliza MediaPipe, que proporciona **468 puntos faciales (landmarks)** detectados en tiempo real, entre los cuales se incluye un conjunto muy detallado de puntos alrededor de los ojos. Estos landmarks no solo permiten obtener la posición geométrica del párpado superior e inferior, sino también determinar la apertura real del ojo fotograma a fotograma. Gracias al parámetro **refine_landmarks=True**, MediaPipe mejora aún más la precisión en áreas críticas como la pupila y los contornos oculares, algo fundamental cuando se quiere calcular una medida sensible como el **Eye Aspect Ratio (EAR)**.

El código, una vez recibidos los puntos de MediaPipe, traduce las coordenadas normalizadas al sistema de coordenadas de la imagen y selecciona un pequeño subconjunto de landmarks correspondiente a ambos ojos. Mediante la distancia euclidiana entre puntos verticales y horizontales se calcula el EAR, una métrica muy utilizada en la detección de parpadeos porque se basa en relaciones geométricas robustas frente a cambios de escala o distancia respecto a la cámara. Cuando este valor cae por debajo de un umbral durante varios fotogramas consecutivos, el sistema interpreta que ha ocurrido un parpadeo real.

Una vez detectado el parpadeo, el resto del programa se encarga de generar y animar las estrellitas. El movimiento de las estrellas parte del centro exacto de los ojos, obtenido a partir de los landmarks calculados en tiempo real, y el resultado es un pequeño efecto visual sincronizado con un evento facial real. El renderizado se realiza mediante OpenCV, que se encarga de mostrar el flujo de video, redimensionar la imagen de la estrella y mezclarla en el fotograma con transiciones graduales de transparencia.

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