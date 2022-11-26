import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.turtle("Hello, " + sys.argv[1])