import sys
import Application as App
import Config as conf

def main():
    try:
      if sys.argv[1].lower() == '--debug':
        conf.debug_mode = True
    except:
       pass

    App()

if __name__ == '__main__':
    main()
