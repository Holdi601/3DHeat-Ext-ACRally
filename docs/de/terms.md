---
title: "Bedingungen und Lizenz"
nav_order: 9
lang: "de"
source: terms.md
source_hash: "d94bf4eca099"
nav_exclude: true
search_exclude: true
---
# Bedingungen und Lizenz {#terms-and-licence}

## Die Inhalte des Spiels {#the-games-content}

Assetto Corsa Rally und seine Etappen gehören seinem Entwickler Kunos Simulazioni und seinem
Herausgeber 505 Games, die dieses Projekt nicht unterstützen. Dieses Werkzeug liefert nichts vom Spiel
mit und lädt nichts herunter: Es liest die Dateien der Kopie, **die du** installiert hast, auf deinem
Rechner, außerhalb des Spiels. Es verändert das Spiel nicht und spricht mit keinem Server. Eine Strecke,
die es schreibt, ist eine Ableitung der Etappe des Spiels: Sie ist dafür da, deine eigenen Fahrten zu
analysieren, nicht zum Teilen oder Veröffentlichen. Ob du das Werkzeug benutzt, ist deine Entscheidung,
unter den Bedingungen, die du für das Spiel akzeptiert hast.

Deshalb ist es ein eigenes Paket: Wenn die Eigentümer des Spiels je verlangen, dass es verschwindet, geht
es allein, und der Viewer, GameFiles und die anderen Werkzeuge bleiben.

Die Regeln von 3DHeat GameFiles gelten hier unverändert
([Regeln und Lizenzen](https://holdi601.github.io/3DHeat-GameFiles/de/rules-and-licences.html)):

- **Keine Schlüssel: keine mitgeliefert, keine herausgelöst.** Keiner der Container des Spiels ist
  verschlüsselt; ein verschlüsselter IoStore-Container wird rundweg abgelehnt.
- **Deine eigenen Dateien, deine Verantwortung.** Das Werkzeug liest die auf deinem Rechner installierten
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
Eigenschaften. Die Listen in `unversioned.py` von GameFiles enthalten **nur Namen und Typen**, Fakten über
das Format, so wie eine Interoperabilitäts-Zuordnungsdatei sie enthält. Sie wurden aus den Unreal-Engine-
Headern abgeleitet, die Epic jedem mit verknüpftem Konto zur Verfügung stellt, und gegen die mitgelieferten
Daten geprüft. Es ist kein Engine-Quellcode enthalten oder nötig. Was dieses Werkzeug hinzufügt – wo eine
Etappe liegt, wie ihre Komponenten ihre Modelle platzieren, wie die Achsen einer Runde liegen – wurde aus dem
installierten Spiel erarbeitet ([Streckenexport](course-assetto-corsa-rally.md)).

## Lizenz und Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSE)).
Braucht 3DHeat GameFiles (MIT) und numpy (BSD-3-Clause); die Tests brauchen pytest (MIT). Siehe
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSES.md).
Für dieses Projekt geschrieben; aus keinem anderen Projekt wurde Code übernommen.
