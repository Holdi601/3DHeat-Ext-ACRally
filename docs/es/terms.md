---
title: Condiciones y licencia
nav_order: 9
lang: "es"
source: terms.md
source_hash: "7278eb6ba813"
nav_exclude: true
search_exclude: true
---
# Condiciones y licencia {#terms-and-licence}

## El contenido del juego {#the-games-content}

Assetto Corsa Rally y sus escenarios pertenecen a su desarrollador, Kunos Simulazioni,
y a su distribuidor, 505 Games. 3DHeat AC Rally no está afiliado a Kunos Simulazioni ni a
505 Games, ni cuenta con su respaldo. Assetto Corsa Rally y los nombres y marcas relacionados
pertenecen a sus titulares.

Esta herramienta no incluye nada del juego ni descarga nada: ni recursos del juego, ni código
del juego, ni DLL. Lee los archivos de la copia que **tú** instalaste, en tu equipo, al margen
del juego. No cambia nada en el juego ni se comunica con ningún servidor. Un recorrido que escribe se recorta
del escenario del juego y se queda en tu equipo, para analizar tus propias vueltas; no lo
compartas ni lo publiques.

Cada lector de juego es un pequeño proyecto propio, con su propio archivo de licencia, sus propias versiones y su propio gestor de incidencias, de modo que puede instalarse, actualizarse, mantenerse - o retirarse a petición de un titular de derechos - por separado, sin afectar al visor ni a las demás herramientas.

Titulares de derechos: abran una incidencia en [github.com/Holdi601/3DHeat-Ext-ACRally/issues](https://github.com/Holdi601/3DHeat-Ext-ACRally/issues); respondemos rápido y retiramos lo que se nos pida.

Las normas de 3DHeat GameFiles se aplican aquí sin cambios
([Normas y licencias](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **Sin claves: ninguna incluida, ninguna recuperada.** Ninguno de los contenedores del juego está
  cifrado; un contenedor IoStore cifrado se rechaza sin más.
- **Tus archivos.** La herramienta lee los archivos del juego
  instalados en tu equipo. Nunca descarga contenido del juego.
- **La salida no es para redistribuir.** Guarda los `.glb` exportados, y las texturas
  que contienen, solo para tu propio análisis. No publiques, compartas ni vendas
  recorridos, niveles, modelos ni texturas exportados. El `.gitignore` del repositorio
  mantiene los archivos del juego, las exportaciones y las vueltas fuera del control de versiones.

## Oodle se encuentra, no se incluye {#oodle-is-found-not-bundled}

Oodle (RAD Game Tools, ahora Epic) es propietario y no tiene una versión redistribuible.
`oo2core_*.dll` está licenciado al producto que lo incluye. Por eso 3DHeat
GameFiles carga una biblioteca que ya está en el equipo en lugar de incluir una, y esta
herramienta tampoco incluye ninguna
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## Los formatos {#the-formats}

El juego usa Unreal Engine 5. Sus contenedores y paquetes los leen los lectores de Unreal
de 3DHeat GameFiles. Los datos de propiedades compilados de Unreal 5 necesitan la lista de propiedades de
cada clase. Las listas del `unversioned.py` de GameFiles son **solo nombres y tipos**. Se
derivaron de las cabeceras del motor Unreal que Epic pone a disposición de
cualquiera con una cuenta vinculada, y se comprobaron contra los datos incluidos. No
se incluye ni se necesita código fuente del motor. Lo que añade esta herramienta (dónde está un
escenario, cómo sus componentes colocan sus mallas, cómo se orientan los ejes de una vuelta) se
averiguó a partir del juego instalado ([Exportar el recorrido](course-assetto-corsa-rally.md)).

## Licencia y fuentes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSE)).
Necesita 3DHeat GameFiles (MIT), numpy (BSD-3-Clause); las pruebas necesitan pytest
(MIT). Véase
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSES.md).
Escrito para este proyecto; no se tomó código de ningún otro proyecto.
