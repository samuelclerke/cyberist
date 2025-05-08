# Necessary Imports
import textwrap
import sys
# Custom Classes
from Modules.dnslookup import dnslookup
from Modules.ping import ping

class networks:
  def __init__(self):
    print('┌─────────────────┐')
    print('│ Networking Mode │')
    print('└─────────────────┘\n')

    while True:
      query: str = input("Enter Query: ").lower().lstrip()
      query: list = query.split()

      # Start chosen process, else repeat query
      match query[0]:
        case 'help' | '-h':
          self.helpFunc()
        case 'exit' | 'return' | 'back':
          return
        case 'quit' | 'stop':
          sys.exit()
        case 'dnslookup' | '-d':
          dnslookup()
        case 'ping' | '-p':
          ping()
        case _:
          print(f'UserInput : {query[0]} is unknown. Enter \'Help\' for help.')
          continue

  def helpFunc(self):
    print(textwrap.dedent("""
    Networks Menu Help
                          
    Options:
      DNS LOOKUP                  [ dnslookup, -d      ]
      Ping Network Test           [ ping, -p           ]
      Exit (go back)              [ exit, return, back ]
      Quit (end program)          [ quit, stop         ]
    
    """))

if __name__ == '__main__':
  networks = networks()