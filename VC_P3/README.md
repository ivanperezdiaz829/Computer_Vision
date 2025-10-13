## Análisis y Clasificación de Monedas

En esta tarea se requería **individualizar la suma de las monedas** presentes en la imagen.

En primer lugar, se visualiza la imagen y se muestran los bordes de las monedas individuales. Al usuario se le pide que haga clic sobre la **moneda de referencia**, que es la de 10 céntimos.

Se calcula el radio en píxeles de esta moneda y se compara con su diámetro real para **obtener la escala de píxeles por milímetro ($\text{px}/\text{mm}$)**. Posteriormente, con esta información, se estima el valor de cada moneda detectada. Finalmente, se suman los valores y se imprime el resultado en pantalla.


## Funciones Clave y Preprocesamiento

En particular, en este código se definen tres funciones útiles y se realiza un preprocesamiento de la imagen.

### Funciones Útiles

* **`fit_circle_kasa(pts)`:** Para encontrar el círculo que **mejor se ajusta** a una serie de puntos del contorno.
* **`median_radius_from_center(center, contour)`:** Para calcular el radio utilizando la **mediana** de las distancias desde el centro, lo que lo hace más robusto a las imperfecciones del contorno.
* **`nms_candidates(cands, ...)`:** Útil porque si el mismo objeto (moneda) se detecta con dos contornos ligeramente diferentes (y, por lo tanto, dos candidatos), esta función mantiene solo el candidato con el radio mayor y **descarta aquellos superpuestos** que están demasiado cerca (Non-Maximum Suppression).

### Preprocesamiento de la Imagen

El preprocesamiento consiste en aplicar los siguientes pasos para mejorar la detección de bordes:

1.  **CLAHE (Contrast Limited Adaptive Histogram Equalization):** Algoritmo para **uniformizar la iluminación y el contraste** en las diversas áreas, compensando sombras o reflejos.
2.  **Filtro Bilateral:** **Remueve el ruido** manteniendo los bordes nítidos.
3.  **Desenfoque Gaussiano (Blur Gaussiano):** Un ligero desenfoque para **estabilizar** los subsiguientes algoritmos de detección de bordes.
4.  **Umbralización Adaptativa y Morfología:**
    * **`cv2.adaptiveThreshold`:** Crea una **imagen binaria** (blanco/negro) que resalta las regiones de las monedas. Es adaptativo, por lo que el umbral de luminosidad cambia según el área de la imagen.
    * **Operaciones Morfológicas (`cv2.morphologyEx`):** Se aplican operaciones de **cierre** (`MORPH_CLOSE`) para rellenar pequeños *gaps* o agujeros dentro de los contornos de las monedas, y de **apertura** (`MORPH_OPEN`) para remover pequeños ruidos.

La imagen resultante (`th_closed`) es una **máscara binaria** que idealmente muestra las monedas como manchas blancas y el resto como negro; sobre esta última se realizan las sucesivas operaciones para **encontrar los contornos**.


## Observaciones sobre Resultados

Al variar las imágenes de entrada del programa, observamos que:

* Con **"Monedas.jpg"**, los contornos de las monedas se detectan correctamente, y se asocian todos los valores correctos excepto por la moneda de 20 céntimos, que se clasifica como un euro (lo que indica un posible error de medición o clasificación en esa instancia).
![alt text](image.png)
* Con **"Img1"**, las monedas **no se detectan correctamente**, probablemente porque el soporte sobre el que se tomó la foto no es rígido y uniforme.
![alt text](image-1.png)
* Mientras que con **"Img4"**, el programa detecta la mayoría de las monedas, pero con algunos **falsos positivos**.
![alt text](image-2.png)

