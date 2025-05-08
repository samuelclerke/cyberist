import Modules.config as config
from Modules.cryptographer import cryptographer
from Modules.networks import networks

class application:
  def __init__(self):
      print('┌─────────────────────┐')
      print('│ Welcome to Cyberist │')
      print('└─────────────────────┘\n')

      if config.debug_mode:
         print("DEBUG MODE ACTIVATED.\n\n")
      else: 
         pass

      if not config.is_admin:
         print(' !! Please run program with admin/root privileges to access all features.')

      print('To access application help please type "help".')
      
      while True: 
         option = input('Enter Mode: ').strip().lower()
         if option == 'stop':
            break
         elif option == 'cryptographer':
            cryptographer()
         elif option == 'networks':
            networks()
         else:
            print('Invalid Input.\n')
