#   7 Nov 2020
#
#   TASK
#   Create a first.txt file that contains the first 90 characters
#   of bears.txt
#   -------------------------------------------------------------

def my_solution( ):
    with open( "bear.txt", "r" ) as bears:
    bears_content = bears.read( )

    bears_trimmed = ''
    for i in range( 90 ):
        bears_trimmed += bears_content[i]

    with open( "first.txt", "w" ) as file:
        file.write( bears_trimmed )

def solution( ):
    with open("bear.txt") as file:
    content = file.read()

    with open("first.txt", "w") as file:
        file.write(content[:90])
