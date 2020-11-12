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
