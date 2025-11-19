conda create --name VC_P5 python=3.11.5
conda activate VC_P5
pip install opencv-python
pip install matplotlib
pip install imutils
pip install mtcnn
pip install tensorflow   
pip install deepface
pip install tf-keras
pip install cmake

# **FILTRO**

Este proyecto implementa un filtro visual que genera pequeñas estrellas animadas cada vez que el usuario parpadea frente a la webcam.
Se utiliza MediaPipe, que proporciona **468 puntos faciales (landmarks)** detectados en tiempo real, entre los cuales se incluye un conjunto muy detallado de puntos alrededor de los ojos. Estos landmarks no solo permiten obtener la posición geométrica del párpado superior e inferior, sino también determinar la apertura real del ojo fotograma a fotograma. Gracias al parámetro **refine_landmarks=True**, MediaPipe mejora aún más la precisión en áreas críticas como la pupila y los contornos oculares, algo fundamental cuando se quiere calcular una medida sensible como el **Eye Aspect Ratio (EAR)**.

El código, una vez recibidos los puntos de MediaPipe, traduce las coordenadas normalizadas al sistema de coordenadas de la imagen y selecciona un pequeño subconjunto de landmarks correspondiente a ambos ojos. Mediante la distancia euclidiana entre puntos verticales y horizontales se calcula el EAR, una métrica muy utilizada en la detección de parpadeos porque se basa en relaciones geométricas robustas frente a cambios de escala o distancia respecto a la cámara. Cuando este valor cae por debajo de un umbral durante varios fotogramas consecutivos, el sistema interpreta que ha ocurrido un parpadeo real.

Una vez detectado el parpadeo, el resto del programa se encarga de generar y animar las estrellitas. El movimiento de las estrellas parte del centro exacto de los ojos, obtenido a partir de los landmarks calculados en tiempo real, y el resultado es un pequeño efecto visual sincronizado con un evento facial real. El renderizado se realiza mediante OpenCV, que se encarga de mostrar el flujo de video, redimensionar la imagen de la estrella y mezclarla en el fotograma con transiciones graduales de transparencia.