# pip y entornos virtuales


## Resumen del Curso

</details>

<details markdown="3"><summary><span style="background-color: #ffe7e0">Link a git hub</span></summary>

***

<span style="color: #3388bb">

### Este curso es practico por lo que la mayor parte del contenido estara en github.
</span>

[**Link**](https://github.com/MariadlRosa-1224/Aprendiendo-entornos-virtuales-con-python)

Solo seran escritos en las demas secciones las clases con conceptos de interes.

</details>

***

<details markdown="3"><summary><span style="background-color: #ffe7e0">Instalando python en mac</span></summary>



<span style="color: #3388bb">

### Verificar que python easte instalado
</span>
```sh
**python** o **python3**

**exit()** 
```
<span style="color: #3388bb">

### instalar herramientas de codigo
</span>

```sh
sudo xcode-select --install

sudo xcode-select --reset
```

<span style="color: #3388bb">

### Instalar python
</span>

**brew install python3**



</details>

***

<details markdown="3"><summary><span style="background-color: #ffe7e0">enstensiones necesarias de vscode</span></summary>


<span style="color: #3388bb">

###  extensiones necesarias de vscode
</span>

**python (de microsoft)** 
**WSL (solo windows)**



</details>

***

<details markdown="3"><summary><span style="background-color: #ffe7e0">Git Stuff</span></summary>



<span style="color: #3388bb">

### Cosas interesantes
</span>

**gitignore.io:** Pagina que te crea un gitignore personalizado

</details>

***
<details markdown="2"><summary><span style="color: #bb5599">Pip y entornos virtuales</span> </summary>

<span style="color: #bb5599">

## Pip y entornos virtuales
</span>

<details markdown="3"><summary><span style="background-color: #ffe7e0">que es pip</span></summary>

|❓ Pregunta 1 - Pregunta 2|
|:-----:|

<span style="color: #3388bb">

### Gestor de paquetes de python
</span>

🎁 **Paquetes de python:** Son codigo que ha sido guardado ser usados en problemas que ya han sido resueltos

[**pypi**](https://pypi.org/) Pagina web que contiene todos los paquetes existentes de python para buscarlos y obtener el comando para descargarlo

<span style="color: #3388bb">

### como usar librerias
</span>

**pip** Comando del gestor de paquetes de python

```sh
pip3 install matplotlib 
```

**ver librerias descargadas**

```sh
pip3 freeze
```

|🗣️ Explicacion en palabras propias del tema|
|:-----:|


</details>

<details markdown="3"><summary><span style="background-color: #ffe7e0">Graficas en python con pip</span></summary>


|🗣️ En esta clase. se mostro un programa en el que se creo para crear graficas. Se mostro como pasar este proyecto a un formato local y como usar la libreria intalada en la clase anterior dentro de un proyecto local. Asi como el como leer errores basicos. |
|:-----:|

</details>

***

<details markdown="3"><summary><span style="background-color: #ffe7e0">Que es y como usar un ambiente virtual</span></summary>

|❓Que problemas puede crear el no crear un ambiente virtual? - Como manejamos un ambiente virtual?|
|:-----:|

<span style="color: #3388bb">

### Cual es el problema de tener librerias generales en toda la computadora
</span>

💥 **Los programas pueden chocar:** Muchos proyectos necesitan librerias diferentes y diferentes versiones de estas librerias, tener librerias instaladas de forma general causa que hayan **conflictos entre ellas** y. **generen errores**



![Screenshot 2024-01-01 at 12.54.00 PM.png](../_resources/Screenshot%202024-01-01%20at%2012.54.00 PM.png)

**Muchos proyectos usan diferentes versiones de la misma libreria:** Matplotlib es una libreria ampliamente usada que tiene versiones de la misma 

![Screenshot 2024-01-01 at 1.04.05 PM.png](../_resources/Screenshot%202024-01-01%20at%201.04.05 PM.png)

Pero las versiones mas viejas siguen disponibles, esto es por compatibilidad, proyectos mas viejos suelen necesitar versiones mas viejas.

**descargar una version de matplotlib desinstala otra:** Tal como se dice, 

<span style="color: #3388bb">

### Ambientes virtuales
</span>

🎁 **Encapsulacion de Modulos:** Cada modelo es encapsulado y atado a un proyecto individal, permtiendo que cada proyecto tenga dependencias independientes entre si.



![Screenshot 2024-01-01 at 1.01.05 PM.png](../_resources/Screenshot%202024-01-01%20at%201.01.05 PM.png)


**como usar un ambiente virtual:**

Verificar donde esta python y pip

```sh
    which python3

    which pip3
```

Si estas en linus o wsl debes instalar 

```sh
    sudo apt install -y python3-venv
```

	Con [virtualenv](https://www.llipe.com/2017/03/25/usar-entornos-virtuales-python-virtualenv-instalar-scipy-macos/) (util para todos los OS, pero especialmente para mac)

```sh
	pip3 install virtualenv

```

Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

```sh
    python3 -m venv env
```

	Con virtualenv

	```sh
	virtualenv -p python3 env
	```


Activar el ambiente
```sh
    source env/bin/activate
```

Salir del ambiente virtual

```sh

    deactivate
```

Borrar ambiente virtual
```sh
	python remove [env_name]
```

Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo

```sh
    pip3 install matplotlib==3.5.0
```

Verificar las instalaciones

```sh
    pip3 freeze
```





|🗣️ Los entornos virtuales nos permiten trabajar con multiples versiones de distintas librerias. En esta clase se nos enseno a como istalarlas.|
|:-----:|

</details>

***

<details markdown="3"><summary><span style="background-color: #ffe7e0">Requirements.txt</span></summary>

|❓ Como podemos automatizar la descarga de multiples librerias?|
|:-----:|

<span style="color: #3388bb">

### Requirements.txt
</span>

**Que es?:**Archivo que gestiona todas las dependencias y en que versiones se necesitan.

Generar el archivo con el siguiente comando

```sh
    pip3 freeze > requirements.txt
```

Revisar lo que hay dentro del archivo

```sh
    cat requirements.txt
```

Instalar las dependencias necesarias para contribuir más rápido en proyectos

```sh
    pip3 install -r requirements.txt
```


|🗣️ Requirements.txt es un archivo que nos sirve para descargar con un unico comando todas las librerias que usa un proyecto, util para trabajos en equipos|
|:-----:|

</details>

***

</details>


<details markdown="2"><summary><span style="color: #bb5599">Lecciones practicas</span> </summary>

<span style="color: #bb5599">

## Lecciones practicas
</span>

<details markdown="3"><summary><span style="background-color: #ffe7e0">Pandas</span></summary>

|❓ Que puede hacer pandas? - Que documentacion hay para la ciencia de datos|
|:-----:|

<span style="color: #3388bb">

### pandas
</span>

**Que es:** Es una de las librerias mas utilizadas en python. Una herramiena para el analisis y la manipulacion de datos.

**instalacion:**
```sh
pip3 install pandas
```


<span style="color: #3388bb">

###  Usos de pandas
</span>

📆 **analisis de datos tabulares** Los llamado dataframes, pandas ouede explorarlos, limpiarlos y procesarlos.

📚**Leer archivos de multiples formatos:** CSV, Excel, JSON, SQL ...

🤖 **calculo de estadistica y visualuzacion de datos:**


|🗣️ En casi todo lo relacionado con analisis y procesamiento de datos, pandas es una buena opcion para procesar datos, con una interfaz robuzta y una enorme comunidad detras.|
|:-----:|


</details>

<details markdown="3"><summary><span style="background-color: #ffe7e0">FastAPI para webservers</span></summary>

|❓ Como funciona un servidor web en python? |
|:-----:|

<span style="color: #3388bb">

### FastAPI
</span>

**Que es fastAPI** Es un framework de Python para crear aplicaciones web rápidas y seguras. Utiliza OpenAPI para definir la interfaz de la aplicación y proporciona un conjunto de herramientas para validar y documentar la API de manera automática.

**Que es Uvicorn** Es un servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento para ejecutar aplicaciones ASGI como FastAPI.
	

**librerias necesarias:**

	- [uvicorn](https://www.uvicorn.org/)

```sh
pip install "uvicorn[stamdar]" 
```

	- [FastAPI](https://fastapi.tiangolo.com/)

```sh
pip install fastapi
```

**En el codigo y la documentacion:** Encontramos el funcionamiento basico de la aplicacion, como hacer que empiece a funcionar. asi como el archivo codigo-curso/web-server/main.py


<span style="color: #3388bb">

### HTML con fastAPI
</span>

**[Es posible abrir distintos tipos de archivos usando fast.api:](https://fastapi.tiangolo.com/advanced/custom-response/#html-response)** El codigo es el siguente:

	- Para html

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
```

	- Para otros tipos de archivos

```python
from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(some_file_path)



```


|🗣️ Fast API nos permite hacer webservers de forma sencilla, esta leccion nos explicaba el uso de esta herramienta de forma basica y como colocar codigo html en la aplicacion|
|:-----:|

</details>

***

</details>


<details markdown="2"><summary><span style="color: #bb5599">Docker</span> </summary>

<span style="color: #bb5599">

## Docker
</span>

<details markdown="3"><summary><span style="background-color: #ffe7e0">Que es docker</span></summary>

|❓ Como funciona docker - Cuales son sus usos cotidianos.|
|:-----:|

<span style="color: #3388bb">

### Docker
</span>

**Que es docker?:** Es una herramienta que al igual que pip, nos ayuda a aislar entornos. A diferencia de pip tambien aisla en entorno de ejecucion de python.

**Para que se usa:** 
- Esta enfocado al momento en el que nuestro proyecto va a salir a produccion. En el que ya no solo debemos aislar las dependencia sino la ejecucion de python, cuya version puede llegar a variar de acuerdo al proyecto.

- Facilitar el desplegar una aplicacion a la nube

**Como lo hace** Con **contenedores.**

<span style="color: #3388bb">

### Instalacion
</span>

**Tener rosseta actualizado** Esto es lo que permita a aplicaciones intell correr en macs m# 

```sh
softwareupdate --install-rosetta 
```
**[seguir instrucciones de pagina web](https://docs.docker.com/desktop/install/mac-install/)**

|🗣️ Docker es una herramienta que facilita la salida a produccion de aplicaciones en la nube gracias a que aisla distintos entornos de desarrollo a las necesidades del proyecto.|
|:-----:|


</details>


<details markdown="3"><summary><span style="background-color: #ffe7e0">dockerizando aplicaciones</span></summary>

|❓ Como funciona docker - Como puede uno aislar proyectos?|
|:-----:|

<span style="color: #3388bb">

### Uso
</span>

**Archivos Dockerfie y docker-compose.yml:** En su interior contienen el codigo necesario para abrir un docker

- Dockerfile

```
FROM python:3.8

WORKDIR /app
COPY requirementes.txt /app/requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirementes.txt

COPY . /app/

CMD bash -c "while true; do sleep 1; done"

Archivo docker-compose-yml

services:
  app-csv:
    build: 
      context: .
      dockerfile: Dockerfile

```

- docker-compose.yml

```
services:
  app-csv:
    build: 
      context: .
      dockerfile: Dockerfile
```


**build de docker en terminal**

Contruir las imagenes de los servicios que previamente fueron definidos en docker-compose. yml
```sh
docker-compose build
```


Ver el estaso de los servicios definidos en docker-compose.yml, si corren o estan detenidos, y otra info de interes
```sh
sudo docker compose ps
```


Inicia los servicios en docker-compose, -d es para que se ejecute en el background
```sh
sudo docker compose up -d

```
Ejecuta una terminal dentro del contenedor especificado, este caso "app-csv, permite varias tareas en el contenedor
```sh
sudo docker compose exec app-csv bash
```

Detiene y elimina los contenedores, redes y volumenes creados con el comando "docker-compose-up"
```sh
sudo docker-compose down
```
Sale del contenedor
```sh
exit
```

<span style="color: #3388bb">

### Docker en el dia a dia
</span>

**Como enlazar el codigo al docker:** La verdad, es mas simple de lo que parece, solo es una linea de codigo extra en el docker-compose.yml

```
services:
  app-csv:
    build: 
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
```
Ahora simplemente basta con hacer el codigo y guardarlo.

**Dockerizar servicios web:** Es el uso mas usual de docker, y para hacerlo solo se requiere un par de lineas extra.


- Dockerfile

```
FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

```



- docker-compose.yml
```
version: "2"
services:
  web-server:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    ports:
     - '8080:80'
```

|🗣️ Esta leccion explica el codigo que uno utiliza con tal de que un contenedor docker sea iniciado y su uso mas fundamental|
|:-----:|

</details>



***

</details>






