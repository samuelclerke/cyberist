import Config as Conf
import Cryptographer as Crypt
from Networks import Networks

class Application:
  def __init__(self):
      print('┌─────────────────────┐')
      print('│ Welcome to Cyberist │')
      print('└─────────────────────┘\n')

      if Conf.debug_mode:
         print("DEBUG MODE ACTIVATED.\n\n")
      else: 
         pass

      if not Conf.is_admin:
         print(' !! Please run program with admin/root privileges to access all features.')

      print('To access application help please type "help".')
      
      while True: 
         option = input('Enter Mode: ').strip().lower()
         if option == 'stop':
            break
         elif option == 'cryptographer':
            Crypt()
         elif option == 'networks':
            Networks()
         else:
            print('Invalid Input.\n')
