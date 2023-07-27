from flask import Flask

app = Flask(__name__)

@app.route('/data')
def backend():
    return "This is some data from the backend service."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)