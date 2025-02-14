from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":  # Fixed the typo here
    app.run(debug=True, port=8000)  # Corrected the syntax for the debug argument
