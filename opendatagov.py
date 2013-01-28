from flask import Flask
from data_counter import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/tagcloud/')
@app.route('/tagcloud/<filter_text>')
def find(filter_text=''):
#    return 'Hello World'
    return getWords(filter_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
