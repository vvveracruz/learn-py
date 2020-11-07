#   7 Nov 2020
#
#   DESCRIPTION
#   A function that continously retrieves and prints text from
#   fruits.txt and can handle the txt file being deleted using python
#   standard modules.
#   -----------------------------------------------------------------

import time     # built in time module (written in C)
import os       # standard external os module (written in Python)

#   Checking where the standard modules are kept:
#   >>> import sys
#   >>> sys.prefix 
#       this will return a filepath
#   standard modules kept at: filepath/lib/Python{version}

while True:
    if os.path.exists( "fruits.txt" ):
        with open( "fruits.txt" ) as file:
            print( file.read() )
    else:
        print( "File does not exist." )
    time.sleep( 10 )
