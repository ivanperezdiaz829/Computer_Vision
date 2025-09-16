<!-- @import "design/style.css" -->

# **PRIMER CONJUNTO DE TAREAS A REALIZAR**

## Índice

- [Preparativos para las tareas](#preparativos-para-las-tareas)
- [Tablero de ajedrez](#tablero-de-ajedrez)
- [Imagen estilo Mondrian](#imagen-estilo-mondrian)
- [Utilización de las funciones de dibujo de OpenCV](#utilización-de-las-funciones-de-opencv)
- [Modificar el plano de una imagen](#modificar-el-plano-de-una-imagen)
- [Obtener el punto más oscuro y brillante de una imagen](#obtener-el-punto-más-oscuro-y-brillante-de-una-imagen)
- [Diseño Pop Art con la entrada de la cámara web](#diseño-pop-art-con-la-entrada-de-la-cámara-web)
- [Fuentes y Documentación](#fuentes-y-documentación)

Este primer conjunto de tareas a realizar consiste en la utilización y aprendizaje del uso del paquete **OpenCV**, el cuál a lo largo de las mismas, se va a utilizar para [crear imágenes](#utilización-de-las-funciones-de-dibujo-de-opencv), [editar planos de colores](#modificar-el-plano-de-una-imagen) y [entradas por la cámara web](#diseño-pop-art-con-la-entrada-de-la-cámara-web).

## Preparativos para las tareas

Para realizar las tareas, primeramente se han de descargar una serie de paquetes y requisitos, para ello, y con el propósito de aislar las descargas de las dependencias para evitar incompatibilidades con otros paquetes, es necesario realizar el siguiente **Script** desde *Anaconda Prompt*.

```bash
conda create --name VC_P1 python=3.13.7 -y
conda activate VC_P1
pip install opencv-python
pip install matplotlib
conda install -n VC_P1 ipykernel --update-deps --force-reinstall -y
```

Una vez configurado el *enviroment* e instaladas las dependencias y paquetes a utilizar durante la práctica, se puede empezar a llevar a cabo las tareas.

## Tablero de Ajedrez

Para esta tarea, se ha hecho uso del paquete *numpy* para crear una imagen (fondo) con las dimensiones dadas por los campos *heigth* y *width*, tras esto, se crea un bloque de tamaño fijo y mediante un recorrido iterativo por filas y columnas para ir coloreando los bloques con el negro absoluto representable y con el blanco absoluto representable.

Una vez obtenida la imagen, mediante la librería *matplotlib* se muestra el plot resultante en escala de grises y tras esta, se imprime un texto con las dimensiones y canales utilizados para la realización del tablero.

## Imagen estilo Mondrian

Esta tarea consiste en crear una imagen estilo [Mondrian](https://estudio-grafico.blogspot.com/2021/02/estilo-mondrian.html), para ello, se ha realizado una imagen vacía con fondo negro de manera similar a la tarea anterior, tras esto, se han puesto cuadros de manera manual poniendo las coordenadas, tamaño y color (o la mezcla de varios canales para obtener variaciones).

Los recuadros creados dentro de la imagen se extienden desde la parte periférica izquierda hasta la inferior derecha, no obstante, se ha decidido situar un gran cuadrado en la parte superior derecha imitando el estilo deseado. Se muestra la imagen de manera similar a la tarea anterior pero sin definir la escala de grises.

## Utilización de las funciones de OpenCV

En esta tarea, mediante el uso del framework *OpenCV* se va a crear una imagen de 0, es el caso de la práctica, se ha optado por la creación de la bandera de Canarias utilizando el método *.rectangle* para las franjas de la bandera y el método *.putText* para escribir en las coordenadas insertadas cómo inputs la palabra **Canarias**.

Por último, haciendo uso de la función de *matplotlib* llamada *.xticks* e *.yticks* se ha creado una función con nombre *delete_ticks* para que el plot no aparezca con las marcas en los ejes. Se muestra la imagen igual que en la tarea anterior.

## Modificar el plano de una imagen

La tarea consiste en cargar una [imagen](Resources/Imagen.jpg) y cambiarle el plano de color, en este caso, se ha decidido utilizar los canales R, G, B (Red, Green, Blue) en escala de grises y mostrar cada imagen en un formato de filas. Para ello, se ha creado un método llamado *color_channel* al cuál se le pasan como parámetros el color, el texto a poner en la imagen y la posición que ocupa en el formato de salida.

Por último, se muestra otra imagen con los tres planos de color juntos, si se ha realizado correctamente, dicha imagen deberá ser igual a la [original](Resources/Imagen.jpg).

Resaltar que el método *.imread* lee la imagen de manera que los canales se ordenan en B, G, R, por lo que para mostrar la imagen con los planos juntos se realiza una conversión a R, G, B.

## Obtener el punto más oscuro y brillante de una imagen

Esta tarea consiste en obtener de una [imagen](Resources/Imagen.jpg) el punto más brillante y oscura de la misma, para ello se lee en escala de grises y mediante el método *minMaxLoc* de obtienen los mínimos y máximos locales.

Una vez obtenidos los mínimos y máximos, haciendo uso del método *.circle* se crea un círculo sobre la imagen en el la localización del mínimo (verde) y del máximo (rojo), tras esto se muestra el plot con una leyenda explicando el código de color, además de quitar las marcas cómo en la tarea anterior y mostrar por último, las coordenadas e intensidad de color del punto más brillante y del punto más oscuro.

## Diseño Pop Art con la entrada de la cámara web

En esta tarea se va a hacer uso de la entrada de la cámara web del dispositivo en el cuál se ejecute el código, consiste en utilizar la entrada para crear una imagen con diseño [Pop Art](https://es.wikipedia.org/wiki/Arte_pop).

Para la entrada de la cámara se utiliza un método llamado *.VideoCapture* que pilla la entrada de la cámara por defecto (no se controla el caso de que falle pero devolvería None en dicho caso), tras esto se lee continuamente la entrada de imagenes y los pone cómo frame.

Una vez realizado lo anterior, se define un frame con un ancho y una altura determinadas y tras esto, 9 subframes que lo van a componer (3x3) con las dimensiones pertinentes.

Para crear las variantes de color, se utiliza un método llamado *.applyColorMap* con los subframes y un *COLORMAP* asociado. Ya creadas las variantes de color, se juntan por filas y por último, se crea el collage por columnas usando las 3 filas.

Se muestra de manera similar a las tareas anteriores.

Para salir de la ventana se espera a que se pulse la tecla Esc.

## Fuentes y Documentación

- **Internet:** Se ha utilizado internet para la búsqueda de información relativa a los estilos y dieseños de las imágenes a realizar en las tareas, por ejemplo, el tamaño de una tablero de [ajedrez](https://www.chess.com/es/article/view/dimensiones-del-tablero) (8x8), información del estilo [Mondrian](https://estudio-grafico.blogspot.com/2021/02/estilo-mondrian.html) y del estilo [Pop Art](https://es.wikipedia.org/wiki/Arte_pop).

- **Inteligencia Artificial Generativa (ChatGPT):** Se ha utilizado para obtener un listado de métodos y funciones de **OpenCV**, así como para revisar posibles fallos en la realñización de las tareas ["Modificar el plano de una imagen"](#modificar-el-plano-de-una-imagen) y ["Diseño Pop Art con la entrada de la cámara web"](#diseño-pop-art-con-la-entrada-de-la-cámara-web).

- **Enlaces:**
    - https://estudio-grafico.blogspot.com/2021/02/estilo-mondrian.html
    - https://es.wikipedia.org/wiki/Arte_pop
    - https://chatgpt.com
    - https://www.chess.com/es/article/view/dimensiones-del-tablero

### **--- Iván Pérez Díaz ---**