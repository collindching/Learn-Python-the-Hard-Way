from sys import argv
## this returns True if a file exists based on its name as an argument
from os.path import exists

script, from_file, to_file = argv

open(to_file,'w').write(open(from_file,'r').read())
