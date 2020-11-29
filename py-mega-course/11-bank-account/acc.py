class Account:
    def __init__( self, filepath ):
        self.filepath = filepath
        with open( filepath, 'r' ) as file:
            self.balance = float( file.read() )

    def withdraw( self, amount ):
        self.balance = self.balance - amount

    def deposit( self, amount):
        self.balance = self.balance + amount

    def commit( self ):
        with open( self.filepath, 'w' ) as file:
            file.write( str( self.balance ) )

class Checking( Account ):
    def __init__( self, filepath ):
        Account.__init__( self, filepath )

checking = Checking( './balance.txt' )
print( checking.balance )
checking.deposit(100)
print( checking.balance )
checking.commit()
