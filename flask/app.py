from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/run")
def run():
    data = request.get_json()

    print("Received:", data)

    code = data.get("code", "")

    commands = []

    for line in code.splitlines():
        line = line.strip()

        if line.startswith("forward(") and line.endswith(")"):
            value = line[8:-1]

            try:
                distance = float(value)
                commands.append(["forward", distance])

            except ValueError:
                return jsonify({
                    "error": f"Invalid distance: {value}"
                }), 400

        elif line:
            return jsonify({
                "error": f"Unknown command: {line}"
            }), 400

    result = {
        "commands": commands
    }

    print("Sending:", result)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)