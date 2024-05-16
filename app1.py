## Building url Dynamically
## Variable Rules and URL Building

from flask import Flask
app1 = Flask(__name__)

@app1.route('/')
def welcome():
    return "Welcome to our website!"

@app1.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the mark is ' + str(score)

@app1.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the mark is ' + str(score)

if __name__ == '__main__':
    app1.run(debug=True)
