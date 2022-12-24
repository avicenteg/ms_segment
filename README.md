# Detección de nuevas lesiones en Esclerosis Múltiple en estudios longitudinales de resonancia magnética

## Autor
+ Adrián Vicente Gómez

## Antecedentes
La esclerosis múltiple (EM) es una enfermedad crónica autoinmune que se caracteriza por la aparición de lesiones desmielinizantes apreciables en imágenes de resonancia magnética (MRI).
El trabajo contenido en este repositiorio es el desarrollo de un sistema de detección en estudios longitudinales de nuevas lesiones de EM basado en redes neuronales. Para ello se utilizan imágenes de resonancia estructurales previamente procesadas para entrenar una red convolucional del tipo U-Net que permite generar máscaras que muestren los cambios entre la imagen base y la de seguimiento.

## Descripción
En el repositorio se encuentra:
+ scripts --> Contiene los scripts que se han usado para realizar el entrenamiento de la red.
+ scripts/mapping.txt contiene el mapeo entre las imágenes iniciales (no se incluyen en el repositorio) y las usadas para entrenar.
+ ms_segmentation --> contiene todo lo necesario para lanzar un docker con una aplicación web que permite obtener la máscara de un paciente.
