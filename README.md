# Tercera_Preentrega
Proyecto Página Web

En este proyecto creé una página con 3 modelos, cada modelo tiene su propio formulario para poder adicionar información a la BD.
a su vez, un formulario para poder buscar información de la base de datos.

-INICIO
para poder utilizar este proyecto en otro ordenador, lo primero que hay que hacer es modificar la ubicación de la carpeta "templates" en el archivo Tercera_Preentrega > proyecto_pagina_web > setting.py. 
Una vez modificada la hubicación de dicha carpeta, se podrá correr el servidor.

PÁGINA WEB
En la página de inicio podremos ver una barra con diferentes botones que nos redireccionarán a distintas URLs (INICIO, URBAN, CROSSOVER, DEPORTIVO)

en cada URL (excepto la de "inicio"), enlistará los datos que se encuentran en cada modelo de la BD (cada modelo, corresponde al nombre de la URL) 
debajo de cada lista, aparecerá un botón para agregar un nuevo dato a la BD, el cual se alistará en dicha página una vez agregado.

BUSQUEDA POR GET
para buscar un dato de la BD, hay que escribir la siguiente URL http://127.0.0.1:8000/coderapp/buscar_urban/?modelo="modelo a buscar"
dicho "modelo a buscar" será un modelo de Auto correspondiente a un modelo de auto cargado previamente en la URL urban.