<!-- @import "design/style.css" -->

# **PRIMER CONJUNTO DE TAREAS A REALIZAR**

## Índice

- [Preparativos para las tareas](#preparativos-para-las-tareas)
- [Tablero de ajedrez](#tablero-de-ajedrez)
- [Imagen estilo Mondrian](#imagen-estilo-mondrian)
- [Utilización de las funciones de dibujo de OpenCV](#utilización-de-las-funciones-de-dibujo-de-opencv)
- [Modificar el plano de una imagen](#modificar-el-plano-de-una-imagen)
- [Obtener punto más oscuro y brillante de una imagen](#obtener-punto-más-oscuro-y-brillante-de-una-imagen)
- [Diseño Pop Art con la entrada de la cámara web](#diseño-pop-art-con-la-entrada-de-la-cámara-web)
- [Fuentes y Documentación](#fuentes-y-documentacion)

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

La tarea consiste en cargar una [imagen](Resources/Imagen.png) 

