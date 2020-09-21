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
    name = "myName3"
    message = "this is a message definitely under 50 characters"

    lineLength = 40
    border = '*'

    fullLine = border * lineLength + '\n'
    emptyLine = border + ' ' * ( lineLength - 2 ) + border + '\n'

    nameLine = centerString( 'Hello '+ name, border, lineLength)

    if len( message ) < ( lineLength - 2 ):
        messageLine = centerString( message, border, lineLength )
    else:
        messageLine = "TBD"
    print( fullLine + emptyLine + nameLine + emptyLine + messageLine + emptyLine + fullLine)

if __name__ == '__main__':
    message = "this is a message definitely under 50 characters"
    lineLength = 40

    messageSplit = message.split(' ')

    messageL1 = ''
    messageL2 = ''
    trimmedArray = []
    i = 0
    while len(messageL1) < lineLength:
        trimmedArray.append( messageSplit[i] )
        print(trimmedArray)
        messageL1 = ' '.join(trimmedArray)
        i += 1

    print(messageL1)
    txt = 'hello how are you'
    new = txt.split(' ')
    new2 = ' '.join(new)
    print(len(['a','b','c']))
