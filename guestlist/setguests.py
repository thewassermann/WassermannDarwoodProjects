import sys
from eventfunctions import Guest

g = Guest()

g.set_first(sys.argv[1])
g.set_last(sys.argv[2])


g.write_to_guestlist()