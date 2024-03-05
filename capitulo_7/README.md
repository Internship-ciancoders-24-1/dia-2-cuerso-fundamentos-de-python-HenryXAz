# Herramientas y recursos de desarrollo para python

## PyPI
Es un repositorio de librerías disponibles para los desarrolladores, contiene todo tipo de herramientas que los desarrolladores pueden utilizar para poder agilizar y mejorar el código que escriben.

## PIP
Se trata de un programa de linea de comandos que nos permite descargar e instalar los recursos disponibles en PyPI. Para instalar pip en linux se debe de tener instalado python y ejecutar el siguiente comando:

En Debian y derivados:
```bash
sudo apt install python3-pip
```

En RHEL y derivados:
```bash
sudo dnf install python3-pip
```

Para poder instalar librerías con pip se debe ejecutar el siguiente comando:
```bash
pip install < nombre de libreria >
```

## Entornos virtuales
Debido a que los proyectos en python suelen manejar distintas versiones del lenguaje y de librerías, regularmente se suele trabajar con entornos virtuales que consisten en entornos aislados donde podemos instalar librerías y versiones de python en las versiones que necesitemos.

Para usar entornos virtuales se debe instalar virtualenv con pip con el siguiente comando:

```bash
pip install virtualenv
```

Para iniciar un entorno virtual se debe de ejecutar el siguiente comando:
```bash
virtualenv --python=<version de python> venv
```

Para activar el entorno virtual debemos de ejecutar el siguiente comando:
```bash
source venv/bin/activate
```

Sabremos que estamos dentro del entorno virtual cuando veamos en el prompt de nuestra linea de comandos la palabra env dentro de paréntesis de la siguiente manera:

```bash
(env)
```

Pip tiene un comando llamado freeze que lista las librerías que tenemos instaladas y sus respectivas versiones. Podemos aprovechar esta característica combinandola con la opción de instalar librerías a través de un documento de texto denominado requirements.txt que posee el comando pip install, veamos como podemos hacerlo:

Escribimos en un documento denomiado requirements.txt la salida del comando pip freeze

```bash
pip freeze > requirements.txt
```
Cuando deseemos instalar las dependencias de nuestro proyecto ejecutaremos el siguiente comando

```bash
pip install -r requirements.txt
```