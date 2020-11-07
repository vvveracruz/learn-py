#   7 Nov 2020
#
#   TASK
#   Define a function that gets a single character and a
#   filepath as parameters and returns the number of occurences
#   of that character in a the file.
#   --------------------------------------------------------------

def my_solution( character, filepath ):
    with open( filepath ) as file:
        content = file.read()

    count = 0

    for i in range( len( content ) ):
        if content[i] == character:
            count += 1
        else:
            pass

    return count

def solution( character, filepath="bear.txt" ):
    file = open(filepath)
    content = file.read()
    return content.count(character)
