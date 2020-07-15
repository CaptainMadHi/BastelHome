from flask import Flask, request, abort, render_template, jsonify
import threading
import requests as requestslib
from device_types import DEVICE_TYPES
from utils import *
import traceback

app = Flask(__name__)

devices = {}
devices_lock = threading.Lock()

@app.route("/api/command/<device_id>/<command>", methods=["GET", "POST"])
def api_request(device_id, command):
  try:
    with devices_lock:
      device = devices[device_id]
  except KeyError:
    abort(404)
  try:
    if not checkRequestSize(request):
      abort(413)
    req_json = request.get_json() or {}
    device_type = DEVICE_TYPES[device["device_type"]]
    required_params = device_type[command]
    for param in required_params.keys():
      if not typecheck(req_json[param], required_params[param]):
        abort(400)
    for param in req_json.keys():
      if not typecheck(req_json[param], required_params[param]):
        abort(400)

    response = requestslib.request(url=f"http://{device['ip']}:{device['port']}/api/command/{command}", method=request.method, json=req_json)
    return response.content
  except KeyError:
    abort(400)

@app.route("/api/register", methods=["PUT"])
def register_device():
  global devices
  try:
    if not checkRequestSize(request):
      abort(413)
    device = request.get_json()
    if not (checkIpv4(device['ip']) and checkPort(device['port']) and device['device_type'] in DEVICE_TYPES): 
      abort(400)
    hash_str = device_to_hash(device)
    with devices_lock:
      devices[hash_str] = device
    return "OK\n"
  except KeyError:
    abort(400)

@app.route("/api/unregister", methods=["DELETE"])
def unregister_device():
  global devices
  try:
    if not checkRequestSize(request):
      abort(413)
    device = request.get_json()
    hash_str = device_to_hash(device)
    with devices_lock:
      del devices[hash_str]
    return "OK\n"
  except KeyError:
    abort(400)

@app.route("/api/device_types")
def get_device_types():
  return jsonify(DEVICE_TYPES)

@app.route("/api/devices")
def get_devices():
  allowed_keys = ["device_name", "device_type"]
  filtered_devices = { key: {inner_key: devices[key][inner_key] for inner_key in allowed_keys} for key in devices.keys() }
  return jsonify(filtered_devices)

@app.route("/")
def main_page():
  return render_template("index.html")

app.run(host="0.0.0.0", port=5000, debug=True)