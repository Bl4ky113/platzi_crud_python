# Curso Práctico de Python: Creacion de un CRUD

Start: 06/06/22 | 14:15
End: ...

Requirements:
- Python Advanced - Medium
- Basic Backend 
- OOP in Python
- Bash Terminal Commands and Knowledge

Sesions: 
1. 06/06/22 | 14:15 - 16:45
2. 06/09/22 | 15:00 - 

## Super-Repaso Python

Python es un lenguaje de programacion sencillo y de simple syntaxis.

Lo instalaremos desde los Repositorios de cualquier Linux, 
ya que es super popular y necesario hoy en día.

Se ejecuta en la terminal con python3 o python, depende si tiene alias.
Podemos descargar paquetes y modulos de python para nuestros proyectos,
pero para descargar unos paquetes y aislar un proyecto, podemos usar el modulo 
de virtual enviroments:
python3 -m venv venv
Generalmente estos se llaman igual, Virtual ENViroments

En python hay diferentes tipos de datos:
- ints: numeros enteros
- float: numeros fraccionarios
- string: cadena de texto
- bool: booleano

Tambien tiene estructuras de texto cómo:
- List: lista expandible de datos
- Tuple: lista inmutable de datos
- Sets: Conjunto organizado de datos
- Dictionaries: Hashmap de datos

Se pueden declarar funciones con funct y 
se pueden hacer decoradores de estas, metaprogramacion
usando syntetic sugar @decorador.

Hay highorder functions que nos permite hacer una function a una estructura de
datos, la cual generalmente va a ser inline functions usando lambda args: codigo.

Python es un lenguaje orientado a Objetos, podemos declarar una clase de estos 
usando Class, donde se van a guardar propiedades y metodos. Genralmente para 
hacer algo privado o asegurado, se usa __ y _ respectivamente. 
Los objetos tienen metodos predeterminados cómo __init__ __iter__ __str__ y otros.
Los cuales estan diseñados para reaccionar al ser usados por una buildin function de 
python, como:
- str(): convierte a str
- init(): cuando se crea una instacia de un object
- iter(): init cuando se intenta iterar por el object
- next(): paso a paso de que hacer cuando se itera por el object

Los iteradores se pueden hacer y usar usando for, el cual nos 
va a permitir iterar a lo largo de un rango de numeros, o los datos de 
una estructura de datos. O si tenemos un obj especial con iterador, atravez 
de eso.

While ejecutara el código que tiene hasta que una condicion no sea verdadera, la 
cual es definida junto a este.

Funcionalidad logica de python se usa condificonales con if y elif, esle para el 
caso que ningua se cumpla. Estas pueden usar diferentes operadores relacionales entre 
dos elementos o logicos entre uno o dos relaciones, generalmente negandola o verificando 
el valor de las otras. 

## Que es la Programacion

Viene de las ciencias de computacion, la cual es un conjunto de Matemáticas, Ingenería y Ciencia. 
Y con la habilidad más importante, resolver problemas con una serie de pasos que estos estrucutras en 
los que:
- toman inputs
- envian outputs
- realizar Operaciones matematicas
- ejecutan condicinales
- Repeticiones de estructuras

## Porque programar en Python

- Syntaxis clara
- Amigable para iniciadores
- Gran comunidad
- Facilidad de usar
- Conjuntos de Librerias más grandes
- Gran popularidad mundial
- Gran uso en la Industria 

## El Proyecto del Curso (Presentacion)

El proyecto va a ser una aplicacion para la terminal que usa python, 
el tema principal va a ser manejar una empresa,
platzi para ejemplo, la cual puede manejar:
- clientes:
	- list
	- create
- ventas:
	- list
	- create
- reportes: 
- setup:
- --help con cada sub comando

## Gooddamit

El curso tiene una buena parte de enseñanza de python, no es solo practica. 
Pero es enseñanza desde 0.

Estoy viendo más bien el curso con ojos de critico, ya que se buena parte de lo que 
se necesita para el curso.

## Iterar elementos + index

Para iterar en una lista y no tener que crear una variable extra 
para tener el index de cada elemento, podemos usar enumetare y la estructura de 
datos. Nos dara una tupla de index y valor, entonces debemos poner dos variables 
al iterar.

## Click Module

Click es un modulo y libreria de python que nos permite hacer diferentes Command
Line Interfaces. Que se basa principalmente en decoradores de nuestros methods y 
functions.

Su nombre viene de:
- Command
- Line 
- Interface
- Creation 
- Kit

Con click podemos definir diferentes estructuras de comandos, como si fuera git. 
En el cual simplemente un comando sencillo que ejecuta un script, o un grupo que 
tiene diferentes acciones, usando el decorador: @click.group()
Y en cada grupo podemos definir sus comandos, con: @"grupo".command()
Para poder compartir datos o contexto entre estos, podemos usar
el decorador: @click.pass_context, el cual pasara a los args un 
obj ctx. El cual tiene un .obj, que es donde definimos el contexto o los 
datos. Los cuales tienen el estado o contexto de la ejecucion actual 
del comando.

Desde la clase de Click, he estado bastante más contento con la clase, ya que de hecho me esta haciendo 
trabajar en un CRUD y me esta dando bases para trabajar con otros. 
En general las notas serían de click, pero creo que se puede dedicar y hacer 
mejores notas en otro curso o proyecto.

