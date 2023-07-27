from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def frontend():
    try:
        response = requests.get('http://backend:3001/data')
        return f"Frontend received data: {response.text}"
    except requests.exceptions.RequestException as e:
        print(f"Error calling backend: {e}")
        return "Error fetching data from the backend.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)