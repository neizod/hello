import sys

names = sys.argv[1:]

if '-h' in names:
    exit("usage: python hello.py [-h] [NAME [NAME ...]]")

if not names:
    print("Hello, world!")

for name in names:
    print("Hi {}.".format(name))

