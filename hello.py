import sys

names = sys.argv[1:]

if '-h' in names:
    exit("usage: python hello.py [-h] [NAME [NAME ...]]")
elif '-v' in names:
    exit("advance hello beta")
elif '-l' in names:
    exit("license under WTFPL v2.0")

if not names:
    print("Hello, world!")

if '-s' in names:
    names.remove('-s')
    names.sort()

for name in names:
    print("Hi {}.".format(name))

