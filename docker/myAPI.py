from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/endpoint", methods=["get"])
def get_data():
    return (jsonify({"message": "recived"} ),200)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
