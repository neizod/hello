import sys

names = sys.argv[1:]

if not names:
    print("Hello, world!")

if '-s' in names:
    names.remove('-s')
    names.sort()

for name in names:
    print("Hi {}.".format(name))

