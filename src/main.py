import sys
from Modules.application import application
import Modules.config as config

def main():
    try:
      if sys.argv[1].lower() == '--debug':
        config.debug_mode = True
    except:
       pass

    app = application()

if __name__ == '__main__':
    main()
