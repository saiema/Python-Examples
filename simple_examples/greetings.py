import sys
if len(sys.argv) != 2:
    print("Ey! You need to give me ONE argument!", file = sys.stderr)
    sys.exit(1)
print("Greetings {}".format(sys.argv[1]))
