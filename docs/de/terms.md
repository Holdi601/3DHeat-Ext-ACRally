---
title: "Bedingungen und Lizenz"
nav_order: 9
lang: "de"
source: terms.md
source_hash: "7278eb6ba813"
nav_exclude: true
search_exclude: true
---
# Bedingungen und Lizenz {#terms-and-licence}

## Die Inhalte des Spiels {#the-games-content}

Assetto Corsa Rally und seine Etappen gehören seinem Entwickler Kunos Simulazioni und seinem
Herausgeber 505 Games. 3DHeat AC Rally ist nicht mit Kunos Simulazioni oder 505 Games verbunden und
wird von ihnen nicht unterstützt. Assetto Corsa Rally und die zugehörigen Namen und Marken gehören
ihren Inhabern.

Dieses Werkzeug liefert nichts vom Spiel mit und lädt nichts herunter: keine Spielinhalte, keinen
Spielcode, keine DLLs. Es liest die Dateien der Kopie, die **du** installiert hast, auf deinem
Rechner, außerhalb des Spiels. Es verändert nichts im Spiel und spricht mit keinem Server. Eine Strecke, die es schreibt,
wird aus der Etappe des Spiels geschnitten und bleibt auf deinem Rechner, zum Analysieren deiner
eigenen Fahrten; bitte teile oder veröffentliche sie nicht.

Jeder Spiele-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei, eigenen Releases und eigenem Issue-Tracker. So lässt er sich für sich allein installieren, aktualisieren und pflegen - oder auf Wunsch eines Rechteinhabers zurückziehen -, ohne dass der Viewer oder die anderen Werkzeuge davon berührt werden.

Rechteinhaber: Bitte ein Issue unter [github.com/Holdi601/3DHeat-Ext-ACRally/issues](https://github.com/Holdi601/3DHeat-Ext-ACRally/issues) eröffnen - wir antworten schnell und entfernen auf Anfrage alles.

Die Regeln von 3DHeat GameFiles gelten hier unverändert
([Regeln und Lizenzen](https://holdi601.github.io/3DHeat-GameFiles/de/rules-and-licences.html)):

- **Keine Schlüssel: keine mitgeliefert, keine herausgelöst.** Keiner der Container des Spiels ist
  verschlüsselt; ein verschlüsselter IoStore-Container wird rundweg abgelehnt.
- **Deine eigenen Dateien.** Das Werkzeug liest die auf deinem Rechner installierten
  Spieldateien. Es lädt nie Spielinhalte herunter.
- **Die Ausgabe ist nicht zur Weitergabe bestimmt.** Behalte exportierte `.glb`-Dateien und die darin
  enthaltenen Texturen für deine eigene Analyse. Veröffentliche, teile oder verkaufe exportierte Strecken,
  Level, Modelle oder Texturen nicht. Die `.gitignore` des Repositorys hält Spieldateien, Exporte und
  Runden aus der Versionsverwaltung heraus.

## Oodle wird gefunden, nicht mitgeliefert {#oodle-is-found-not-bundled}

Oodle (RAD Game Tools, heute Epic) ist proprietär und hat keine weiterverteilbare Fassung.
`oo2core_*.dll` ist an das Produkt lizenziert, das sie ausliefert. 3DHeat GameFiles lädt deshalb eine
Bibliothek, die schon auf dem Rechner liegt, statt eine eigene mitzuführen, und dieses Werkzeug führt
ebenfalls keine mit
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/de/reader-oodle.html)).

## Die Formate {#the-formats}

Das Spiel basiert auf Unreal Engine 5. Seine Container und Pakete werden von den Unreal-Lesern von 3DHeat
GameFiles gelesen. Die Eigenschaftsdaten von Unreal 5 brauchen für jede Klasse eine Liste ihrer
Eigenschaften. Die Listen in `unversioned.py` von GameFiles enthalten **nur Namen und Typen**. Sie wurden aus den Unreal-Engine-
Headern abgeleitet, die Epic jedem mit verknüpftem Konto zur Verfügung stellt, und gegen die mitgelieferten
Daten geprüft. Es ist kein Engine-Quellcode enthalten oder nötig. Was dieses Werkzeug hinzufügt – wo eine
Etappe liegt, wie ihre Komponenten ihre Modelle platzieren, wie die Achsen einer Runde liegen – wurde aus dem
installierten Spiel erarbeitet ([Streckenexport](course-assetto-corsa-rally.md)).

## Lizenz und Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSE)).
Braucht 3DHeat GameFiles (MIT) und numpy (BSD-3-Clause); die Tests brauchen pytest (MIT). Siehe
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSES.md).
Für dieses Projekt geschrieben; aus keinem anderen Projekt wurde Code übernommen.
