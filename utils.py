import socket
from hashlib import md5

MAX_BYTES = 1 * 1000 * 1000

def checkIpv4(ip):
  try:
    socket.inet_pton(socket.AF_INET, ip)
    return True
  except socket.error:
    print(f"{ip} is not a valid IP")
    return False

def checkPort(port):
  try:
    return 1 <= int(port) <= 65535
  except:
    print(f"{port} is not a valid port")
    return False

def checkRequestSize(request):
  return not hasattr(request, "content_length") or request.content_length is None or request.content_length < MAX_BYTES

def device_to_hash(device):
  to_hash_str = f"{device['ip']},{device['port']}"
  return md5(str.encode(to_hash_str)).hexdigest()

def typecheck(obj, type_val):
  if isinstance(type_val, list):
    return obj in type_val
  if type_val == "rgb":
    return isinstance(obj, int) and 0<= obj <= 0xffffff
  if type_val == "boolean":
    return isinstance(obj, bool)
  if type_val == "string":
    return isinstance(obj, str)
  if type_val == "number":
    return isinstance(obj, int) or isinstance(obj, float)
  raise Exception
