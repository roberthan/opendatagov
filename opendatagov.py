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

@app.route('/keyword/')
@app.route('/keyword/<filter_text>')
def find(filter_text=''):
#    return 'Hello World'
    return getDetails(filter_text)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    response.headers.add('Access-Control-Max-Age', '1000')
    response.headers.add("Access-Control-Allow-Headers", '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
