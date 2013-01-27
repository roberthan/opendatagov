from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test/')
@app.route('/test/<filter>')
def cal(name=''):
    return getTestSet(filter.replace('_',' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
