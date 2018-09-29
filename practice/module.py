
import sys
import importlib
abc = importlib.import_module("generator")
if __name__ == '__main__':
    print sys.path
    for x in abc.fab(10):
        print x

