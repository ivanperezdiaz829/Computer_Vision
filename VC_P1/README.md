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

<p style="text-indent: 2em;">Para realizar las tareas, primeramente se han de descargar una serie de paquetes y requisitos, para ello, y con el propósito de aislar las descargas de las dependencias para evitar incompatibilidades con otros paquetes, es necesario realizar el siguiente **Script** desde *Anaconda Prompt*.

```bash
conda create --name VC_P1 python=3.13.7 -y
conda activate VC_P1
pip install opencv-python
pip install matplotlib
conda install -n VC_P1 ipykernel --update-deps --force-reinstall -y
```

<p style="text-indent: 2em;">Una vez configurado el *enviroment* e instaladas las dependencias y paquetes a utilizar durante la práctica, se puede empezar a llevar a cabo las tareas.

## Tablero de Ajedrez

<p style="text-indent: 2em;">Para esta tarea, se ha hecho uso del paquete *numpy* para crear una imagen (fondo) con las dimensiones dadas por los campos *heigth* y *width*, tras esto, se crea un bloque de tamaño fijo y mediante un recorrido iterativo por filas y columnas para ir coloreando los bloques con el negro absoluto representable y con el blanco absoluto representable.

<p style="text-indent: 2em;">Una vez obtenida la imagen, mediante la librería *matplotlib* 