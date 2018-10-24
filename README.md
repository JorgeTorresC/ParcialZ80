
# Z80 parcial1

_La idea principal de este proyecto radica en la creación de un emulador del procesador Z80 y su
lenguaje ensamblador, para esto se ha venido llevando una minucioso proceso de investigación respecto
procesador._
_Acá va un párrafo que describa lo que es el proyecto_

## Comenzando

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos

_Para este proyecto solo necesitaremos Python 3.x y Tkinter que es el moduloa para interfaces graficas por defecto de Python si no cuenta con él puede instalarlo para su S.O. sudo pacman -S tk_

_Para Manjaro, se puede buscar directamente en los repositorios de AUR_

_Para ubuntu_
```
sudo apt-get install python-tk
```


### Instrucciones

_Inicialmente debe clonar el proyecto o descargarlo._

_Se recomienda ejecutar el programa desde consola._

```
python GUI.py
```
_Esto despliega la GUI donde podremos ejecutar comandos y ver como actua el procesador._

_Tanto el modulos ALZ80.py y el Z80CPU.py tambien se puede probar de manera independiente_
_Para esto solo es necesario ejecutar el comando:_

```
python ALZ80.py
```

_El repositorio cuenta con pruebas para este modulo así que para ver mejor como funciona el modulo ALZ80 solo seria
ir al final del fichero y descomentar ejecutar el comando_

```
python ALZ80.py < TestALZ80.in
```

_Donde TestALZ80.in y TestALZ80_2.in Son ficheros con lenguaje ensamblador del Z80._

_Para las pruebas en Z80CPU solo sera encesario descomentar la parte llamada "Ejercicios"
y ejecutar el comando:_

```
python Z80CPU.py
```

## Ejecutando las pruebas ⚙️

_Inicialmente tenemos los archivo TestALZ80 y TestALZ80_2 para darnos una idea de los
comandos que Recibe el programa, pero si con esto no queda claro, tambien podemos
remitirnos a:_
  * [Curso ensamblador Z80](https://wiki.speccy.org/cursos/ensamblador/lenguaje_1)

_En este link encontraremos muchos ejemplos del lenguaje y gran parte del proyecto se baso en ese curso._


## Deployment 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Python](https://docs.python.org/3/library/)
* [Tkinter](https://docs.python.org/2/library/tkinter.html)


## Autores ✒️


* **Daniel Caita** -  [dacaitac](https://github.com/dacaitac)
* **Jorge Torres** -  [JorgeTorresC](https://github.com/JorgeTorresC/)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto.
