"""Test input from command line"""
import sys

if len(sys.argv) != 4: #3 + 1 (the command!)
    print("Dear user, I was expecting three parameters. You gave me ", len(sys.argv)-1)
    sys.exit(1)
else:
    for i in range(0, len(sys.argv)):
        print("Param {}: {} ({})".format(i, sys.argv[i], type(sys.argv[i])))
