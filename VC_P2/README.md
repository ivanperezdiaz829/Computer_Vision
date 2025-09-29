## Número máximo de píxeles blancos

La tarea consiste en cargar una imagen y aplicar el detector de bordes Canny para obtener un resultado binario (bordes en blanco y fondo en negro).
Posteriormente, se cuentan los píxeles blancos presentes en cada fila de la imagen y se identifica cuál es la fila con mayor número de bordes.
Con este valor máximo, se seleccionan todas las filas que tienen al menos el 90% de dicho número de píxeles blancos.
Finalmente, se muestran tres resultados: la imagen de Canny, la imagen original con las filas destacadas en rojo y un gráfico con el porcentaje de píxeles blancos por fila.

## Interactive Motion Art
La inspiración del proyecto viene de tres fuentes: 
My little piece of privacy, que plantea la captura de la presencia de las personas y la generación de una respuesta visual; 
Messa di voce, que explora la manipulación de colores y planos de imagen para crear efectos artísticos; 
Virtual air guitar, que propone la interacción en tiempo real con los movimientos del espectador frente a la cámara. 
El concepto consiste en una instalación donde la cámara capta a la persona en tiempo real, detecta movimientos o cambios en la escena y genera un efecto visual dinámico basado en los bordes, colores y diferencias entre frames, creando una especie de “pintura en tiempo real” que refleja la interacción del espectador con el espacio. El código convierte los frames a escala de grises, aplica suavizado Gaussiano para reducir el ruido, calcula los bordes mediante el filtro Sobel y detecta movimiento comparando el frame actual con el anterior. En la ventana principal, Demostrador Interactivo, las zonas con movimiento se colorean en rojo y se superponen los bordes Sobel para generar un efecto visual artístico. La ventana Movimiento muestra únicamente la máscara binaria del movimiento detectado entre frames consecutivos, mientras que la ventana Fondo presenta el modelo del fondo estimado por el background subtractor, permitiendo diferenciar claramente los objetos móviles del fondo estático. La ejecución se realiza en tiempo real y finaliza al pulsar la tecla ESC, liberando todos los recursos de la cámara.