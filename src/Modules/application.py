import Modules.config as config
from Modules.cryptographer import cryptographer
from Modules.dnslookup import dnslookup

class application:
  def __init__(self):
      if config.debug_mode:
         print("DEBUG MODE ACTIVATED.\n\n")
      else: 
         pass
      
      while True: 
         option = input('Enter Mode: ').strip().lower()
         if option == 'stop':
            break
         elif option == 'cryptographer':
            crypt = cryptographer()
         elif option == 'dnslookup':
            dnsl = dnslookup()
         else:
            print('Invalid Input.\n')
