from flask import Flask, render_template

app = Flask( __name__ )

@app.route( '/' )
def Home():
    return render_template( 'home.html' )

@app.route('/about/')
def About():
    return "This is the about section!"

if __name__ == "__main__":
    app.run( debug = True )
