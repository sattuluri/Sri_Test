#bin/usr/python

import sys 
import re

a =sys.argv[1]
path = re.compile('(www\.[A-Z|a-z]+\.[A-Z|a-z][A-Z|a-z]\.gov)')
result = path.match(a)
print result
