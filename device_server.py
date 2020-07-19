from flask import Flask, request, Response, jsonify
from importlib import import_module
import requests
import sys
import subprocess
import threading
from device_types import DEVICE_TYPES


app = Flask(__name__)

MAIN_SERVER = None
IP = None
DEVICE_TYPE = None
DEVICE_NAME = None
PORT = None
DEVICE = None

device_lock = threading.Lock()

@app.route("/api/command/<command>", methods=["GET", "POST"])
def api_request(command):
  req_json = request.get_json()
  device_function = getattr(DEVICE, command)
  response_data = device_function(**req_json)
  if isinstance(response_data, tuple):
    return Response(response_data[0], mimetype=response_data[1])
  if isinstance(response_data, dict):
    return jsonify(response_data)
  return response_data

def setup(main_server, port, device_type, device_name):
  global MAIN_SERVER, IP, DEVICE_TYPE, PORT, DEVICE, DEVICE_NAME
  MAIN_SERVER = main_server
  DEVICE_TYPE = device_type
  PORT = int(port)
  ipbytes = subprocess.check_output("hostname -I", shell=True)
  IP = ipbytes.decode().strip()

  DEVICE = import_module(DEVICE_TYPE)
  DEVICE_NAME = device_name
  
  payload = {"ip": IP, "port": PORT, "device_type": DEVICE_TYPE, "device_name": DEVICE_NAME}
  requests.put(url=f"{MAIN_SERVER}/api/register", json=payload)

if __name__ == "__main__":
  try:
    setup(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    app.run(host="0.0.0.0", port=PORT, debug=False)
  except IndexError:
    print("Supply main server URL/IP:port, device type and port number")
  except ModuleNotFoundError:
    print(f"No module {sys.argv[1]} found")
  except requests.exceptions.ConnectionError:
    print("Main server not reachable") 