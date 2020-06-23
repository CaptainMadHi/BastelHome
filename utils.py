import socket

MAX_BYTES = 1 * 1000 * 1000

def checkIpv4(ip):
  try:
    socket.inet_pton(socket.AF_INET, ip)
    return True
  except socket.error:
    return False

def checkPort(port):
  try:
    return 1 <= port <= 65535
  except:
    return False

def checkRequestSize(request):
  return not hasattr(request, "content_length") or request.content_length is None or request.content_length < MAX_BYTES