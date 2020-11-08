import json
from difflib import get_close_matches


def getDictionary( filepath = 'data.json' ):

    with open( filepath ) as file:
        return json.load( file )

def getWord():

    word = ''
    while word == '':
        word = input( 'Word: ' )

    return word.lower()

def checkMatches( word, data):
    matches = get_close_matches( word, data )
    if matches == []:
        return None
    else:
        answer = input( "Did you mean " + matches[0] + "? (Y/N) " )
        if answer.upper() == "Y":
            return matches
        else:
            return None

def getDefinition( word = '' ):
    data = getDictionary()
    word = getWord()

    matches = checkMatches( word, data )
    while matches == None:
        print("It doesn't look like that is a word. Please try again.")
        word = getWord()
        matches = checkMatches( word, data )

    word = matches[0]

    return "\n" + str(data[ word ]) + "\n\n"

print(getDefinition())
