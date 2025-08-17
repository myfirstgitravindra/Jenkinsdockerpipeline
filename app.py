from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # Renders templates/index.html
    return render_template("index.html")

@app.route("/data")
def data():
    # Example JSON data the page fetches
    return jsonify({
        "status": "ok",
        "message": "Hello from Flask!",
        "items": [
            {"id": 1, "name": "Alpha"},
            {"id": 2, "name": "Bravo"},
            {"id": 3, "name": "Charlie"}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Ensure this matches your Docker port mapping
