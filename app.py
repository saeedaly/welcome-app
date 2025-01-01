
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Web Page</h1><p>This is a simple web page created with Python and Flask.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)