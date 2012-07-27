import sys

names = sys.argv[1:]

if not names:
    print("Hello, world!")

for name in names:
    print("Hi {}.".format(name))

