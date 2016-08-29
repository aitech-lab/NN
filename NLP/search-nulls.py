import sys

file = sys.argv[2]

print(repr(open(file, 'rb').read(2000))) # dump 1st 200 bytes of file
data = open(file, 'rb').read()
print(data.find('\x00'))
print(data.count('\x00'))
