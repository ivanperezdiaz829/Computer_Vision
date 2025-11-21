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

Como primer paso para realizar el clasificador por imágenes, se tiene la creación/descarga y preparación del dataset a utilizar, en el caso de la práctica, se ha usado un dataset de imágenes públicas de caras de personas llamado [UTKFace](https://susanqq.github.io/UTKFace/), en el cuál todas las imágenes tienen un formato tal que: `[age]_[gender]_[race]_[date&time].jpg`.

Para el clasificador solo será necesario el primer campo de la edad, por ello y para simplificar el proyecto se van a dividir los campos de edad en 3 subgrupos:

- **Joven:** Caras de personas de entre 0 a 29 años, ambos incluidos.
- **Medio:** Caras de personas de entre 30 a 59 años, ambos incluidos.
- **Anciano:** Caras de personas de 60< años, el 60 incluido.

Para dicha clasificación y preparación, el primer fragmento de código tras los imports busca la carpeta descargada [UTKFace](https://susanqq.github.io/UTKFace/) y, filtrando por edad, crea un nuevo directorio llamado **organized_data** en donde se mezclan las imágenes y se guardan un 70% en una carpeta de entrenamiento (*"train"*), un 15% en una carpeta de validación (*"validation"*) y el resto en una carpeta de tests (*"test"*). Este directorio se crea dentro del proyecto en donde se ejecute, pero para el entrenamiento y posteriores códigos, se lee la información desde una URL que habrá que modificar dependiendo del equipo.

De manera adicional, la carpeta **organized_data** ya creada se puede encontrar accediendo al siguiente [enlace](https://drive.google.com/drive/folders/1FqaiOvJAYazT6YZ-WHdQGrJQ_ESN1zZg?usp=drive_link).

Para el entrenamiento de la red neuronal se hace uso de **PyTorch**, realizando un entrenamiento dinámico de dos etapas con **_TransferLearning_** y haciendo uso de **ResNet50**.

Como primer paso del entrenamiento, se busca un dispositivo GPU con CUDA (acelera enormemente la velocidad de entrenamiento comparado con la CPU) y se definen los hiperparámetros para el entrenamiento (tamaño de la imagen y tamaño del lote), además de la ruta de datos.

Tras lo anterior, se preparan los datos para que la red aprenda mejor y sea más robusta. Para ello se realizan las siguientes transformaciones.

- `Resize((224, 224))`: Redimensiona las imágenes al tamaño esperado por la red.

- `RandomHorizontalFlip()`: Es un **_Data Augmentation_** que voltea aleatoriamente de manera horizontal algunas imágenes de entrenamiento, duplicando así de manera artificial el conjunto de datos y reduciendo el **_Overfitting_**.

- `ToTensor()`: Convierte las imágenes (0-255 píxeles) a tensores de **PyTorch** (0-1 en aritmética flotante).

- `Normalize()`: Es una estandarización, resta la media y divide por la desviación estándar utilizando los valores específicos del dataset `ImageNet (mean=[0.485...], std=[0.229...])`. Esto es fundamental para el **_Transfer Learning_**.

Por último en cuanto a la preparación, comentar que los DataLoaders son los encargados de suministrar los datos a la GPU en lotes a la vez que los mezcla para evitar el **_Overfitting_**.

Para el entrenamiento en sí, se utiliza la técnica ya comentada **_Trasnfer Learning_** con una **ResNet50** Pre-entrenada, congelando la última capa original de que clasificaba 1000 objetos de *ImageNet* y se reemplaza por la arquitectura creada para el clasificador de edades que contiene lo siguiente:

- `Linear(2048, 256)`: Reduce la complejidad de una capa a otra.

- `ReLU()`: Es la función de activación.

- `Dropout(0, 4)`: Apaga aleatoriamente el 40% de las neuronas en cada pasada de entrenamiento evitando que las neuronas dependan demasiado unas de otras (hay que tener cuidad con los valores, si son muy altos la red se puede volver "tonta").

- `Linear(256, 3)`: Última capa con los 3 subgrupos de edad mencionados anteriormente.

El entrenamiento dinámico dividido en 2 partes consiste en lo siguiente:

FASE1: Entrenamiento de la cabeza:

- **Objetivo:** Entrenar solo las capas nuevas (finales) para que aprendan a interpretar las características que extrae la ResNet congelada.

- **Configuración:** Realiza 15 épocas haciendo uso del optimizador **AdamW** y con una tasa de aprendizaje de 0.001.

FASE2: Ajuste fino (*Fine-Tuning*):

- **Objetivo:** Pule toda la red para que se especialice en detectar caras y edades, ajustando ligeramente las capas profundas de la ResNet.

- **Configuración:** Realiza 50 épocas con toda la red descongelada, haciendo uso del optimizador **AdamW** y con una tasa de aprendizaje muy baja.

Adicionalmente, comentar que existe un *Early Stopping* de 15 épocas por si el modelo deja de mejorar.

Ya entrenada la red, en la siguiente traza de código se generan unos gráficos acerca del propio entrenamiento.

<h4 style="font-weight: bold; text-decoration: underline">Precisión del entrenamiento:</h4>

<img src="/VC_P5/train_results/training_accuracy_plot.png">

<h4 style="font-weight: bold; text-decoration: underline">Historial de pérdida del entrenamiento:</h4>

<img src="/VC_P5/train_results/training_loss_plot.png">

De estos gráficos se puede deducir que la primera etapa fue completamente exitosa pero en la segunda empezó a hacer overfitting llegando incluso al *Early Stopping* y consiguiendo un máximo de 84.02% de precisión.

## APLICACIÓN DEL CLASIFICADOR SOBRE UN FILTRO

El filtro a crear con el clasificador se basa en un .png de un [bebé](/VC_P5/filters/bebe.png) en el caso de clasificar como *Joven*, un [bigote](/VC_P5/filters/medio.png) en el caso de clasificar como *Medio* y un [anciano](/VC_P5/filters/anciano.png) en caso de clasficar como *Anciano*.

Para aplicar el filtro se hace uso de **MediaPipe** y del modelo previamente entrenado. Y mediante los 6 puntos obtenidos del modelo ligero de `FaceDetection` se elige el lugar exacto en donde se quiere colocar el .png.

Los 6 puntos son:

- Ojo derecho
- Ojo izquierdo
- Nariz (punta)
- Boca (centro)
- Oreja derecha
- Oreja izquierda

La lógica del procesamiento de los filtros es la siguiente:

- **CASO MEDIO, BIGOTE:**

  - Toma el landmark de la nariz y de la boca y calcula el punto medio entre ellos. Se estima el tamaño del bigote como un 50% del ancho total de la cara.

- **CASO JOVEN Y ANCIANO, FRENTE:**

  - Toma los landmarks de los ojos y calcula el punto medio y después se desplaza restando desde la línea de los ojos un 40% a la altura de la cara para colocarlo en la frente.

<h4 style="font-weight: bold; text-decoration: underline">Prueba con imagen que activa filtro de niño:</h4> 

(Se ha utilizado una imagen de anciano para no poner explícitamente un niño del dataset, adicionalmente se aprecia como el modelo puede fallar como en el caso de la imagen)

<img src="/VC_P5/Simple_filter_test/output_results/output_img_142.png">

<h4 style="font-weight: bold; text-decoration: underline">Prueba con imagen que activa filtro de medio:</h4>

<img src="/VC_P5/Simple_filter_test/output_results/output_img_621.png">

<h4 style="font-weight: bold; text-decoration: underline">Prueba con imagen que activa filtro de anciano:</h4>

<img src="/VC_P5/Simple_filter_test/output_results/output_img_281.png">

También hay una traza de código en el fichero [Exercises_P5](/VC_P5/Exercises_P5.ipynb) en donde se puede aplicar en vez de a una imagen estática, a un vídeo en tiempo real.

<h4 style="font-weight: bold; text-decoration: underline">Filtro aplicado en tiempo real:</h4>

![Filtro_Tiempo_Real_Age]()

## FILTRO DE ESTRELLAS

En este apartado se implementa un filtro visual que genera pequeñas estrellas animadas cada vez que el usuario parpadea frente a la webcam.

Se utiliza **_MediaPipe_**, que proporciona **468 puntos faciales (landmarks)** detectados en tiempo real, entre los cuales se incluye un conjunto muy detallado de puntos alrededor de los ojos. Estos landmarks no solo permiten obtener la posición geométrica del párpado superior e inferior, sino también determinar la apertura real del ojo fotograma a fotograma. 

Gracias al parámetro `refine_landmarks=True`, **_MediaPipe_** mejora aún más la precisión en áreas críticas como la pupila y los contornos oculares, algo fundamental cuando se quiere calcular una medida sensible como el **Eye Aspect Ratio (EAR)**.

En la traza de código, una vez recibidos los puntos de **_MediaPipe_**, se traducen las coordenadas normalizadas al sistema de coordenadas de la imagen y selecciona un pequeño subconjunto de landmarks correspondiente a ambos ojos.
 
Haciendo uso de la distancia euclidiana entre puntos verticales y horizontales se calcula el `EAR` que es una métrica muy utilizada en la detección de parpadeos basada en relaciones geométricas robustas frente a cambios de escala o distancia respecto a la cámara. Cuando este valor cae por debajo de un umbral durante varios fotogramas consecutivos, el sistema interpreta que ha ocurrido un parpadeo real.

Una vez detectado el parpadeo, el resto del programa se encarga de generar y animar las *"estrellitas"*. El movimiento de las estrellas parte del centro exacto de los ojos, obtenido a partir de los landmarks calculados en tiempo real, y el resultado es un pequeño efecto visual sincronizado con un evento facial real. El renderizado se realiza mediante **OpenCV**, que es el encargado de mostrar el flujo de video, redimensionar la imagen de la estrella y mezclarla en el fotograma con transiciones graduales de transparencia.

<h4 style="font-weight: bold; text-decoration: underline">Filtro aplicado en tiempo real:</h4>

![Filtro_Tiempo_Real_Stars]()

## FUENTES Y DOCUMENTACIÓN

- **Internet:** Se ha utilizado internet para buscar posibles ideas para realizar los filtros, así como datasets para el entrenamiento de la red neuronal clasificadora por edades.

- **Inteligencia Artificial Generativa (ChatGPT, Gemini):** Se ha utilizado para obtener el modelo de imágenes estáticas a partir del modelo de video creado para el filtro que utiliza la red neuronal clasificadora de caras por edad.

- **Enlaces:**
    - https://huggingface.co/microsoft/Florence-2-large
    - https://github.com/JaidedAI/EasyOCR
    - https://pytorch.org/get-started/locally
    - https://chatgpt.com/
    - https://gemini.google.com
    - https://www.investopedia.com/terms/r/returnoninvestment.asp

Para más documentación referente a las tareas, véase el [Notebook](Exercises_P5.ipynb) asociado a la carpeta de la práctica en cuestión **(VC_P5)**.