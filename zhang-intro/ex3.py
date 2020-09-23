import math

def two_a():
    '''
    A program that asks the ser for a float x_0 an prints the value of f(x) = x^3 - 3x + 1 at x_0
    '''
    x = float ( raw_input( "Please enter your value for x_0: " ) )
    print( x ** 3 - 3*x + 1 )

def two_b():
    '''
    A function that asks the user for their name, then prints "Hello `name`!"
    '''
    name = str ( raw_input( "What is your name? " ) )
    print( "Hello %s!" % name )

def two_c():
    '''
    A function that asks the user for an integer, and then displays the number of digits in the integer, and the logarithm of the integer
    '''
    n = int ( raw_input( "Choose an integer: " ) )

    logn = math.log(n)

    count = 0
    num = n
    while ( num > 0 ):
        num = num // 10
        count = count + 1

    print( "%d has %d digits." % (n, count))
    print( "The logarithm of %d is %.2f." % (n, logn))

def two_d():
    '''
    A function that asks the user for an integer, and then displays the number of digits in the integer to the power of 3.
    '''
    n = int ( raw_input( "Choose an integer: " ) )
    n3 = n ** 3

    count = 0
    num = n3
    while ( num > 0 ):
        num = num // 10
        count = count + 1

    print( "{}, which is {} to the power of three, has {} digits".format( n3, n, count ))

def two_e():
    '''
    A function which asks the user to input a string s and displays the following string: "s***s***s".
    '''
    s = str ( raw_input( "What is your motto? " ) )

    print( "{}***{}***{}".format(s, s, s ) )

def two_f():
    '''
    A function which asks the user for a string and displays a string that repeats the input string n times, where n is the length of the input string.
    '''
    s = str ( raw_input( "What is your motto? " ) )

    n = 0
    string = s
    while n < len(s) - 1:
        n += 1
        string = string + s

    print( string )

def centerString( s, border, lineLength ):
    '''
    A function used in three()
    '''
    if (len( s ) % 2) == 0:    #name is even

        padding = ( lineLength - 2 - len(s) ) / 2
        sLine = border + ' ' * padding + s + ' ' * padding + border + '\n'

    else:

        paddingLeft = int( math.floor( ( lineLength - 2 - len(s) ) / 2 ) )
        paddingRight = paddingLeft + 1
        sLine = border + ' ' * paddingLeft + s + ' ' * paddingRight + border + '\n'

    return sLine

def three():
    '''
    A function that asks the user for their name, and a short message under 50 characters, and displays it.
    '''
    name = str ( raw_input( "What is your name? " ) )
    message = str ( raw_input( "What is your message? " ) )

    lineLength = 40
    border = '*'

    fullLine = border * lineLength + '\n'
    emptyLine = border + ' ' * ( lineLength - 2 ) + border + '\n'

    nameLine = centerString( 'Hello '+ name, border, lineLength)

    if len( message ) < ( lineLength - 2 ):
        messageLine = centerString( message, border, lineLength )
    else:
        messageLine = getFormattedMessage( message, lineLength, border)
    print( fullLine + emptyLine + nameLine + emptyLine + messageLine + emptyLine + fullLine)

def getFormattedMessage( rawMessage, lineLength, border ):
    '''
    '''
    # INIT
    messageLength = lineLength - 2*len(border) - 2
    wordList = rawMessage.split(' ')
    formattedLine = ''
    formattedMessage = ''

    for word in wordList:
        if len(word) + len(formattedLine) + 1 >= messageLength:

            formattedLine = centerString( formattedLine, border, lineLength )
            formattedMessage = formattedMessage + formattedLine

            formattedLine = word

        else:

            formattedLine = formattedLine + ' ' + word

    formattedLine = centerString( formattedLine, border, lineLength )
    formattedMessage = formattedMessage + formattedLine

    return formattedMessage

def four():
    '''
    A program that asks for user input and performs conversions.
    '''
    choice = None
    choiceMessage = "What conversion do you need help with?\n\n1 - Celsius to Fahrenheit,\n2 - Fahrenheit to Celsius,\n3 - Meter to foot,\n4 - Foot to meter,\n5 - Acre to square meter,\n6 -  Square meter to acre,\n7 - Pound to kilogram,\n8 - Kilogram to pound conversion.\n\nEnter a digit from 1 to 8 here: "
    choiceError = "\nThat's not an option. Please enter a digit from 1 to 8 here: "

    choice = int( raw_input( choiceMessage ) )
    while True:
        if choice in range(8):
            break
        else:
            choice = int( raw_input( choiceError ) )

if __name__ == '__main__':
    four()
