from flask import Flask, request, abort
from hashlib import md5
import threading
import requests as requestslib
from utils import *

app = Flask(__name__)

device_types = {}
devices = {}
devices_lock = threading.Lock()

@app.route("/test", methods=["GET", "POST"])
def test():
  return "ok\n"

@app.route("/")
def hello_world():
  #TODO actually write a main view
  return "Hello World"

@app.route("/api/command/<device_id>", methods=["GET", "POST"])
def api_request(device_id):
  try:
    device = None
    with devices_lock:
      device = devices[device_id]
    if not checkRequestSize(request): abort(413)
    response = requestslib.request(url=f"{device['ip']}:{device['port']}/api/command", method=request.method, data=request.get_data())
    return response.content
  except KeyError:
    abort(404)


@app.route("/api/register", methods=["PUT"])
def register_device():
  global devices
  try:
    if not checkRequestSize(request): abort(413)
    device = request.get_json()
    if not (checkIpv4(device['ip']) and checkPort(device['port']) and device['device_type'] in device_types): abort(400)
    to_hash_str = f"{device['ip']},{device['port']},{device['device_type']}"
    hash_str = md5(str.encode(to_hash_str)).hexdigest()
    with devices_lock:
      devices[hash_str] = device
  except KeyError:
    abort(400)

@app.route("/api/unregister")
def unregister_device():
  global devices
  try:
    if not checkRequestSize(request): abort(413)
    device = request.get_json()
    to_hash_str = f"{device['ip']},{device['port']},{device['device_type']}"
    hash_str = md5(str.encode(to_hash_str)).hexdigest()
    with devices_lock:
      del devices[hash_str]
  except KeyError:
    abort(400)

def setup():
  global device_types
  #TODO setup device_types config -> dict

setup()
app.run(host="0.0.0.0", port=5000, debug=True)