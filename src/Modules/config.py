import ctypes, os
debug_mode = False

try:
  is_admin = os.getuid() == 0
except AttributeError:
  is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0