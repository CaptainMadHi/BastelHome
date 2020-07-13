status = False

def get_status():
  return {"status": status}

def change_status(new_status):
  global status
  status = new_status
  return {"status": status}

def invert_status():
  global status
  status = not status
  return {"status": status}
