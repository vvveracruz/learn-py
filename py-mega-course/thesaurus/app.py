import json
from difflib import get_close_matches

def getDictionary( filepath = 'data.json' ):

    with open( filepath ) as file:
        return json.load( file )

def getWord():

    word = ''
    while word == '':
        word = input( '\nSelect word: ' )

    return word.lower()

def checkMatches( word, data ):
    matches = get_close_matches( word, data.keys() )
    if matches == []:
        return None
    else:
        answer = input( "Did you mean " + matches[0] + "? (Y/N) " )
        if answer.upper() == "Y":
            return matches
        else:
            return None

def formatDefinition( defn ):
    if len(defn) == 1:
        msg = "\n" + str( defn[0]) + "\n"
    else:
        msg = "\nThis word has " + str( len(defn) ) + " meanings: \n"
        for i in range( len( defn ) ):
            msg += str(i+1) +'. ' + defn[ i ] + '\n'
    return msg

def getDefinition():
    data = getDictionary()
    word = getWord()

    if word in data.keys():
        return formatDefinition( data[ word ] )
    elif word.title() in data.keys():
        return formatDefinition( data[ word.title() ] )
    elif word.upper() in data.keys():
        return formatDefinition( data[ word.upper() ] )
    else:
        matches = checkMatches( word, data.keys() )
        while matches == None:
            print("It doesn't look like that is a word. Please try again.")
            word = getWord()
            matches = checkMatches( word, data )
        return formatDefinition( data[ matches[0] ] )


print(getDefinition())
