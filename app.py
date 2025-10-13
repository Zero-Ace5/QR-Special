from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/health')
def health_check():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True)
