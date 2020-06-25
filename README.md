# RasPi Smarthome
### by Mahdi and Oskar

## Installation

Just run `sh install.sh`

## Device Definition

Wir sollten eine zentrale Weise haben, wie wir Gerätearten definieren. Also zB eine config Datei, in der alle Gerätearten mit einem eindeutigen Namen bezeichnet sind. Außerdem, welche Aktionen man auf denen ausführen kann und welche zusätzlichen Argumente diese Aktionen benötigen.

## Device ids

Jedes Gerät sollte eine eigene ID bekommen, die unabhängig von der Art des Geräts und der Art der Erreichbarkeit ist. Im einfachsten Fall einfach durchnummerieren. Dann kann man in einer weiteren config eine Zuordnung machen mit ID -> (IP,Port) und ID -> Geräteart.

Hier könnte man später eine automatische Device recognition definieren, wodurch das nicht mehr händisch eingetragen werden muss. 

## API

Jedes Gerät sollte eine GET Methode implementieren, die den aktuellen Status des Geräts wiedergibt. Für die Lampe wäre das zB ob sie gerade aus ist oder in welchen der vordefinierten Modi sie versetzt wurde. Für die Kamera wäre das der Kamerastream oder nur die Adresse vom Kamerastream, je nachdem wie die Implementierung da läuft.

Außerdem kann jedes Gerät Aktionen implementieren, die man auf ihm ausführen kann. Definiert in der device definition config. Diese können dann über eine POST Methode aufgerufen werden, wobei der Name der Aktion und die notwendigen Argumente im POST Body sind.

## Website

Diese kann mithilfe der device id Liste und der device config automatisch generiert werden. Die device id Liste sagt einem, welche devices es gibt und welcher Art sie sind. Dadurch können neue devices einfach in die Liste auf der Website aufgenommen werden. Die device config definiert die Aktionen und deren Argumente, die dann als Buttons mit Inputs auf der Seite stehen können.
