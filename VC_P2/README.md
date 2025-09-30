<!-- @import "design/style.css" -->

# **SEGUNDO CONJUNTO DE TAREAS A REALIZAR**

## Índice

- [Preparativos para las tareas](#preparativos-para-las-tareas)
- [Número máximo de píxeles blancos](#número-máximo-de-píxeles-blancos)
- [Umbralizado de imagen a 8 bits](#umbralizado-de-imagen-a-8-bits)
- [Modos de captura por WebCam](#modos-de-captura-por-webcam)
- [Interactive motion art](#interactive-motion-art)
- [Fuentes y Documentación](#fuentes-y-documentación)

Este segundo conjunto de tareas consiste en hacer uso de las técnicas de **[Sobel](https://scispace.com/pdf/edge-detection-by-modified-otsu-method-167ccq2st7.pdf)** con **[Otsu](https://learnopencv.com/otsu-thresholding-with-opencv/)** y de **[Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)** para obtener los bordes de las imágenes para tratar con ellas tanto en vídeo capturado por la WebCam como para mostrar información obtenida a partir de una [imagen](../VC_P2/Resources/mandril.jpg).

## Preparativos para las tareas

Para la realización de las siguientes tareas, se va a utilizar el mismo *enviroment* de Python llamado VC_P1 creado en el [primer conjunto de tareas](../VC_P1/Exercises_P1.ipynb), la única dependencia adicional que se ha de descargar es la que viene dada por el paquete **Pillow**.

```bash
pip install Pillow
```

Adicionalmente, se va a cargar la [imagen](../VC_P2/Resources/mandril.jpg) a utilizar en las posteriores tareas, de forma que no sea necesario cargarla en cada uno de los ejercicios en donde se requiera su uso.

Por último antes de empezar, se van a inicializar todos los paquetes requeridos para la correcta ejecución de los ejercicios.

```python
import cv2  
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

image = cv2.imread('Resources/mandril.jpg') 

if image is not None:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure()
    plt.axis("off")
    plt.imshow(image_rgb) 
    plt.show()
    heigth, width = image.shape[:2]
    print(f'La imagen tiene un tamaño de {width}x{heigth} pixeles')
else: 
    print('Imagen no encontrada')
```

Para las tareas también va a ser de gran utilidad poseer la imagen en escala de grises, por lo tanto, se va a obtener la misma.

```python
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.axis("off")
plt.imshow(gray_img, cmap='gray') 
plt.show()
```

Realizado lo anterior, se procede a empezar con las tareas que conforman la práctica.

## Número máximo de píxeles blancos

La tarea consiste en cargar una imagen y aplicar el detector de bordes **[Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)** para obtener un resultado binario (bordes en blanco y fondo en negro).

Posteriormente, se cuentan los píxeles blancos presentes en cada fila de la imagen y se identifica cuál es la fila con mayor número de bordes. Con este valor máximo, se seleccionan todas las filas que tienen al menos el 90% de dicho número de píxeles blancos.

Finalmente, se muestran tres resultados: la imagen **[Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)**, la [imagen original](../VC_P2/Resources/mandril.jpg) con las filas destacadas en rojo y un gráfico con el porcentaje de píxeles blancos por fila.

## Umbralizado de imagen a 8 bits

Se va a aplicar un umbralizado de la imagen del [mandril](../VC_P2/Resources/mandril.jpg) tras pasarla a escala de grises y posteriormente, se va a realizar el conteo por filas y columnas. Adicionalmente, se va a mostrar el dato del valor máximo de las filas y columnas, además de determinar las mismas que tengan un valor por encima del 90% del máximo.

Por último, se usa la imagen del [mandril](../VC_P2/Resources/mandril.jpg) para mostrar las filas y columnas obtenidas tras realizar lo anterior mencionado usando la técnica de **[Sobel](https://scispace.com/pdf/edge-detection-by-modified-otsu-method-167ccq2st7.pdf)** y la técnica de **[Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)**.

La técnica del **[Sobel](https://scispace.com/pdf/edge-detection-by-modified-otsu-method-167ccq2st7.pdf)** consiste en detectar bordes más continuos y gruesos ya que calcula la magnitud del gradiente en todas las partes, a esto se le aplica el umbral **[Otsu](https://learnopencv.com/otsu-thresholding-with-opencv/)** el cual suele conservar bastantas transiciones de intensidad. 

Entre sus características destacan:

- Tiende a incluir bordes suaves y ruido (aunque no siempre son relevantes).

- Tanto las filas como las columnas seleccionadas abarcan zonas más amplias que, por ejemplo, la técina Canny, esto es porque hay más píxeles por encima del umbral.

La técnica **[Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)**, a comparación de la anterior, detecta bordes mucho más delgados y definidos ya que no solo incluye el gradiente sino también una supresión de histéresis con dos umbrales y de máximos.

Entre sus características destacan:

- Es más selectivo, descartando transiciones débiles y ruido.

- Las filas y columnas seleccionadas suelen ser menos numerosas pero más precisas y se alinean más con los contornos más claros de la imagen.

## Modos de captura por WebCam

En esta tarea se propone un demostrador de los modos de detección de bordes aplicados en la tarea anterior, en este caso, se va a aplicar en las imágenes recogidas a través de la WebCam. Adicionalmente, se han aplicado diferentes modos de imagen adicionales. Los modos de imagen implementados son:

- **"o", original:** Es el modo de imagen por defecto que le entra a la WebCam.

- **"e", espejo:** Le da la vuelta a la imagen en el eje X, mostrando así la visión real que tiene una persona sobre la imagen.

- **"g", gris:** La imagen original que recibe como entrada la WebCam se pone en escala de grises.

- **"c", canny:** Convierte la imagen de entrada en una escala de blancos y grises para depsués de umbralizarla mostrar únicamente los bordes detectados.

- **"y", canny filas y columnas:** Usando el método para la obtención de las filas y columnas de modo canny creado para la tarea anterior, se aplica pero a la imagen de entrada de la WebCam.

- **"s", sobel:** Convierte la imagen de entrada en una escala de blancos y grises para después de umbralizarla mostrar únicamente los bordes detectados.

- **"x", sobel filas y columnas:** Usando el método para la obtención de filas y columnas de modo sobel creado para la tarea anterior, se aplica a la imagen de entrada de la WebCam.

- **"f", substracción de fondo:** Usando una cámara fija se construye un fondo sin demasiado movimiento y en cada iteración de la captura de fotogramas se compara si un pixel ha cambiado de estado y lo pone en blanco.

Para cambiar los modos de visualización, se ha de pulsar por teclado las teclas mecionadas en el menú de opciones que se printea al ejecutar el script inferior.

## Interactive Motion Art

La inspiración del proyecto viene de tres fuentes: 

- [My little piece of privacy](https://www.niklasroy.com/project/88/my-little-piece-of-privacy), que plantea la captura de la presencia de las personas y la generación de una respuesta visual; 

- [Messa di voce](https://youtu.be/GfoqiyB1ndE?feature=shared), que explora la manipulación de colores y planos de imagen para crear efectos artísticos; 

- [Virtual air guitar](https://youtu.be/FIAmyoEpV5c?feature=shared), que propone la interacción en tiempo real con los movimientos del espectador frente a la cámara. 

El concepto consiste en una instalación donde la cámara capta a la persona en tiempo real, detecta movimientos o cambios en la escena y genera un efecto visual dinámico basado en los bordes, colores y diferencias entre frames, creando una especie de *“pintura en tiempo real”* que refleja la interacción del espectador con el espacio. 

El código convierte los frames a escala de grises, aplica suavizado Gaussiano para reducir el ruido, calcula los bordes mediante el filtro **[Sobel](https://scispace.com/pdf/edge-detection-by-modified-otsu-method-167ccq2st7.pdf)** y detecta movimiento comparando el frame actual con el anterior. En la ventana principal, *Demostrador Interactivo*, las zonas con movimiento se colorean en rojo y se superponen los bordes **[Sobel](https://scispace.com/pdf/edge-detection-by-modified-otsu-method-167ccq2st7.pdf)** para generar un efecto visual artístico. La ventana *Movimiento* muestra únicamente la máscara binaria del movimiento detectado entre frames consecutivos, mientras que la ventana *Fondo* presenta el modelo del fondo estimado por el background subtractor, permitiendo diferenciar claramente los objetos móviles del fondo estático. La ejecución se realiza en tiempo real y finaliza al pulsar la tecla ESC, liberando todos los recursos de la cámara.

## Fuentes y Documentación

- **Internet:** Se ha utilizado internet para la búsqueda de información relativa al funcionamiento de la estrategia de **[Sobel](https://scispace.com/pdf/edge-detection-by-modified-otsu-method-167ccq2st7.pdf)**, aplicando también el **[Otsu](https://learnopencv.com/otsu-thresholding-with-opencv/)** y la estrategia de **[Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)**. Adicionalmente, para la última tarea se ha tomado inspiración de los vídeos: [My little piece of privacy](https://www.niklasroy.com/project/88/my-little-piece-of-privacy), [Messa di voce](https://youtu.be/GfoqiyB1ndE?feature=shared) y [Virtual air guitar](https://youtu.be/FIAmyoEpV5c?feature=shared).

- **Inteligencia Artificial Generativa (ChatGPT):** Se ha utilizado la IA generativa para refactorizar el código de la [tarea 2](#umbralizado-de-imagen-a-8-bits) para convertirlo en una función con el objetivo de poder implementarla de manera simple como un modo adicional en la [tarea 3](#modos-de-captura-por-webcam).

- **Enlaces:**
    - https://scispace.com/pdf/edge-detection-by-modified-otsu-method-167ccq2st7.pdf
    - https://learnopencv.com/otsu-thresholding-with-opencv/
    - https://chatgpt.com/
    - https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
    - https://www.niklasroy.com/project/88/my-little-piece-of-privacy
    - https://youtu.be/GfoqiyB1ndE?feature=shared
    - https://youtu.be/FIAmyoEpV5c?feature=shared

Para ver el resultado y código de las tareas, véase el [Notebook](./Exercises_P2.ipynb) asociado a la carpeta de la práctica en cuestión **(VC_P2)**.
