status = False

def get_status():
  return status

def change_status(new_status):
  global status
  status = new_status

def invert_status():
  global status
  status = not status