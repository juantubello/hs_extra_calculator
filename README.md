# Calculador de horas extra

_El programa es una simple aplicación desktop desarrollada en python, la cual tiene como proposito calcular las horas extra que trabajo por mes, de manera que yo
no tenga que realizar el calculo manualmente todos los meses. El proceso es sencillo, me descargo un excel con toda la informacion de mis horas al mes, este 
se sube directamente a la aplicacion y esta ma devuelve la cantidad de horas extra REALES trabajas y la plata a cobrar en base a la tarifa que se le indica._

## Importante 🚀

_Si estas buscando ejecutar/compilar el archivo.py, es necesario que sepas que la lógica esta diseñada en base a un formato de excel (el cual usa mi empresa), asi que 
te recomendaria que mires con detalle las funciones calulate_hs_extra y load_excel_data y las modifiques segun tus requerimientos antes de ejecutar/compilar._

### Pre-requisitos 📋

_Contar con [Python](https://www.python.org/) instalado y las librerias:_
 - `PANDAS`
 - `XLDR`
 - `PYINSTALLER`

### Instalación 🔧

_Para correr la aplicacion hay 2 formas, las cuales dependen exclusivamente si usas enviorements para tus desarrollos o
instalas las dependencias globalmente_

- Si es el primer caso [VirtualEnvironments](https://docs.python.org/3/tutorial/venv.html)  entras dentro del mismo y mediante `pip install` instalas las librerias 
indicadas en Pre-requisistos

- Si es el segundo caso, nuvamente usas `pip install` pero sin necesidad de entrar al ambiente, instalas las librerias mencionadas en Pre-requisitos de manera global

- Finalmente para ambos casos solo hay que correr el comando `python hs_extra.py` para que localmente levante la app

## Compilar 📦

_La aplicación fue codificada en LINUX pero no fue complilada en este, ya que mi S.O principal es Windows 10 y los binarios son distintos, asi que voy a dejar el comando
que utilice, pero este es valido unicamente para sistemas operativos windows._ 

Para compilar, creas una nueva carpeta, por ejemplo `horas_extra_files` y metes dentro el archivo `hs_extra.py` luego por CMD entras a la 
ruta de esta misma, corremos el comando:
- `pyinstaller --onefile --noconsole --hidden-import=xlrd  --hidden-import=pandas._libs.tslibs.timedelta hs_extra.py`

 y se van a generar varias carpetas, dentro de `/dist` esta el `.EXE` generado el cual levanta la app! muy sencillo 😊

## Autor ✒️

* **Juan Pablo Fernandez Tubello** 

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](https://github.com/juantubello/hs_extra_calculator/blob/main/LICENSE) para detalles
