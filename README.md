# RasPi Smarthome
### by Mahdi and Oskar

## Installation

Just run `sh install.sh`

## Architecture

Es gibt einen main_server. Dieser verwaltet alle device_server, welche sich bei ihm anmelden. Er ist außerdem der Webserver für Clients. Um den Status von devices abzurufen oder zu ändern, richtet der client seine Anfragen an main_server, welcher als Relay zu dem gewünschten device_server fungiert. Der Client kennt dabei nicht die IP der device_server, sondern nur einen Hash, welcher devices identifiziert. Auf diese Weise kann der main_server auch offen zum Internet betrieben werden, solange er sich im gleichen LAN wie die devices befindet.

## Device registration

Jedes device im Netzwerk meldet sich beim Starten seines Servers beim main_server per Aufruf von `/api/register` mit seiner IP, Port, device_type, device_name config. Per Hashwert wird dieses Gerät beim main_server gespeichert. Beim Beenden des device_servers meldet sich das device per `/api/unregister` wieder ab.

## API

Anfragen an devices werden an `/api/command/{device_id}/{command}` gerichtet. Jedes device hat eine Reihe von commands, die es implementieren kann. Einer dieser commands muss ein GET command mit dem Namen `get` sein, welcher einfach nur den aktuellen Status des device abfragt. Alle anderen commands sind PUT commands, sie verändern also etwas am Status des Geräts. Alle commands können Parameter annehmen, welche im vorhinein definiert sind. Diese werden bei einer Anfrage per JSON übergeben. Der main_server überprüft Anfragen auf ihre Gültigkeit anhand von `device_types.py`.

## Device Definition

In der `device_types.py` sind alle Arten von devices in einem dict definiert:
```python
{
  "device_name 1": {
    "command_name 1": {
      "param 1": "boolean|string|number",
      "param 2": "boolean|string|number"
    },
    "command_name 2": {}
  },
  ...
}
```

## Website

Die Website ist mit dem JS Framework Vue geschrieben. Sie ist geschachtelt aufgebaut, um beliebige devices von beliebigen device_types mit beliebigen commands anzeigen zu können. Neue device commands müssen nur serverseitig implementiert werden. Im Frontend muss für neue device_types nur eine view Komponente hinzugefügt werden, welche den Status des device sinnvoll anzeigt.

### Website Deployment
Man benötigt npm, den node package manager zum installieren der für den build genutzten js packages
```
curl -L https://raw.githubusercontent.com/tj/n/master/bin/n -o n
bash n lts
```

Sobald man npm hat, kann man die Website builden
```
cd frontend
npm install
npm run build
```

Dann einfach flask anwerfen und fertig
```
python server.py
```

