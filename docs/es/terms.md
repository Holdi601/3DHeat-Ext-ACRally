---
title: Condiciones y licencia
nav_order: 9
lang: "es"
source: terms.md
source_hash: "d94bf4eca099"
nav_exclude: true
search_exclude: true
---
# Condiciones y licencia {#terms-and-licence}

## El contenido del juego {#the-games-content}

Assetto Corsa Rally y sus escenarios pertenecen a su desarrollador, Kunos Simulazioni,
y a su distribuidor, 505 Games, que no respaldan este proyecto. Esta herramienta no incluye nada
del juego ni descarga nada: lee los archivos de la copia que **tú** instalaste, en tu equipo,
al margen del juego. No cambia nada en el juego ni se comunica con ningún servidor. Un recorrido que
escribe es una derivada del escenario del juego: es tuyo para analizar tus propias vueltas, no para
compartirlo ni publicarlo. Usar la herramienta es decisión tuya, bajo las condiciones que aceptaste
para el juego.

Por eso es un paquete aparte: si los propietarios del juego alguna vez piden que se retire,
se retira sola, y el visor, GameFiles y las demás herramientas se quedan.

Las normas de 3DHeat GameFiles se aplican aquí sin cambios
([Normas y licencias](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **Sin claves: ninguna incluida, ninguna recuperada.** Ninguno de los contenedores del juego está
  cifrado; un contenedor IoStore cifrado se rechaza sin más.
- **Tus archivos, tu responsabilidad.** La herramienta lee los archivos del juego
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
cada clase. Las listas del `unversioned.py` de GameFiles son **solo nombres y tipos**,
hechos sobre el formato, como los que contiene un archivo de mapeo de interoperabilidad. Se
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
