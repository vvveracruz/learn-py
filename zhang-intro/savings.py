def run():
    '''
    '''
    print( "[Savings Calculator]" )

    rate = float ( raw_input( "Please enter the interest rate: " ) )
    years = int ( raw_input( "Please enter the number of years: " ) )
    init = float ( raw_input( "Please enter the initial sum of money: $" ) )
    final = init * ( 1.0 + rate ) ** years

    print( "After %d years, the savings will be $%.2f" % ( years, final ) )

if __name__ == '__main__':
    run()
