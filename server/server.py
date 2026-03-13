from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/update/check")
def check_update():
    version = request.args.get("version")

    if version != "1.1":
        return jsonify({
            "update": True,
            "version": "1.1",
            "url": "http://localhost:8080/patch/v1.1.zip"
        })
    else:
        return jsonify({
            "update": False
        })

app.run(port=8080)