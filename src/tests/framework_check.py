from flask import Flask

app = Flask(__name__)

@app.route("/")
def feedback():
    return "<h1>Framework is working :)</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    