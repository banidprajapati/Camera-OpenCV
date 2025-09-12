import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main

def entry_point():
    if hasattr(main, 'main'):
        main.main()
    else:
        pass

if __name__ == "__main__":
    entry_point()
