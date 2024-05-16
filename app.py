from flask import Flask
## WSGI Application
app = Flask(__name__)

@app.route('/') # decorator
def welcome():
    return "Welcome to my website!"

# can add any amount of define functions

if __name__=="__main__":
    app.run(debug = True) # debug = True, automatically update any changes in the .py file
