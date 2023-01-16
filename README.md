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

## Instalación
Los pasos para instalar el presente repositorio son:

1. Descargue el repositorio en un dispositivo con distribución Linux (preferiblemente Ubuntu).
```
git clone https://github.com/avicenteg/ms_segment.git
```
2. A continuación, descargue el [siguiente zip](https://drive.google.com/file/d/1shSCdZ1aDm5O6V1Dwn2imrtWAE3zxkuJ/view?usp=sharing)  que contiene los modelos que no pueden ser incluidos por limites de tamaño de GitHub. Este link solo podrá ser abierto haciendo uso de cuentas con el dominio uoc.edu. 

3. En el directorio local del repositorio copiar el zip descargado en el directorio /ms_segmentation/model/nnUNet_trained_models/nnUNet/3d_fullres/Task501_MS_segmentation  y ejecutar: 

```
unzip models.zip
```
4. Una vez descomprimido el fichero, volver al directorio /ms_segmentation/, previamente a arrancar la aplicación, se debe disponer de una instalación de Docker con el plugin de compose. Se podrá instalar con el siguiente comando: 
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
5. Con la instalación completada, ejecutar el comando:
```
docker compose up
```
Esto arrancará la aplicación web que podrá ser visitada en la dirección <http://localhost:8000> desde cualquier navegador.

Es necesario que el equipo en el que se instale tenga habilitados los drivers de NVIDIA para usar CUDA si se quiere hacer uso de la tarjeta gráfica.