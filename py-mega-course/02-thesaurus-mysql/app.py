#   Establishing a connection to remote database,
#   using mysql.connector package,
#   credentials provided in the course.

import mysql.connector
from difflib import get_close_matches

def getQueryResults( query = "SELECT * FROM Dictionary"):
    #   Connection object.
    con = mysql.connector.connect(
        user = "ardit700_student",
        password = "ardit700_student",
        host = "108.167.140.122",
        database = "ardit700_pm1database"
        )

    #   Cursor object used to navigate through the data.
    cursor = con.cursor()
    query = cursor.execute( query )
    results = cursor.fetchall()

    return results

def getWord():

    word = ''
    while word == '':
        word = input( '\nSelect word: ' )

    return word.lower()

def checkMatches( word, availableWords ):
    matches = get_close_matches( word, availableWords )
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
    word = getWord()
    expressionList = [ expression[0] for expression in getQueryResults( "SELECT Expression FROM Dictionary" ) ]

    if word in expressionList:
        pass
    elif word.title() in expressionList:
        word = word.title()
    elif word.upper() in expressionList:
        word = word.upper()
    else:
        matches = checkMatches( word, expressionList )
        while matches == None:
            print("It doesn't look like that is a word. Please try again.")
            word = getWord()
            matches = checkMatches( word, expressionList )
        word = matches[0]

    definition = [ result[1] for result in getQueryResults( "SELECT * FROM Dictionary WHERE Expression = '%s'" % word )]

    return formatDefinition( definition )

print( getDefinition() )
