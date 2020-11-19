#   7 Nov 2020
#
#   DESCRIPTION
#   A function that continously retrieves data from
#   fruits.txt and can handle the txt file being deleted. Using
#   pandas.
#   -----------------------------------------------------------------

import time     #   built in lib
import os       #   standard lib
import pandas   #   third party lib


filepath = "temps_today.csv"

while True:
    if os.path.exists( filepath ):
        data = pandas.read_csv( filepath )
        print( data.mean() )
    else:
        print( "File does not exist." )
    time.sleep( 10 )
