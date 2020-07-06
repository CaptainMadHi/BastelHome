from flask import Flask, request
from importlib import import_module
import requests
import sys

app = Flask(__name__)

MAIN_SERVER = None
DEVICE_TYPE = None
PORT = None

@app.route("/api/command", methods=["GET", "POST"])
def api_request():
  pass

def presetup(main_server, device_type, port):
  global MAIN_SERVER; DEVICE_TYPE, PORT
  MAIN_SERVER = main_server
  DEVICE_TYPE = device_type
  PORT = port
  
  payload = {"ip": None, "port": PORT, "device_type": DEVICE_TYPE}
  requests.put(url=f"{MAIN_SERVER}/api/register", json=payload)

if __name__ == "__main__":
  try:
    setup(sys.argv[1], sys.argv[2], sys.argv[3])
    app.run(host="0.0.0.0", port=PORT)
  except IndexError:
    print("Supply main server URL/IP:port, device type and port number")
  except ModuleNotFoundError:
    print(f"No module {sys.argv[1]} found")
  except requests.exceptions.ConnectionError:
    print("Main server not reachable") 