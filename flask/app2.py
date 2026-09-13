from flask import Flask, render_template, send_file, abort, request, jsonify
from pathlib import Path
import turtle
import subprocess
import sys
import tempfile
import os

from PIL import Image

app = Flask(__name__)

# Where the student .py files live
SUBMISSIONS = Path.cwd()/"./showroom/"
RENDER_DIR = Path("/tmp/turtle-render")
RENDER_DIR.mkdir(exist_ok=True)

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

@app.get("/turtle/")
def turtle_viewer():
    # Find all Python files
    files = sorted(SUBMISSIONS.glob("*.py"))

    # Send filenames to index.html
    return render_template(
        "index2.html",
        files=files
    )

@app.get("/turtle/render/<filename>")
def render_turtle(filename):
	print("hello?")
	if "/" in filename or "\\" in filename:
		abort(400)

	source = SUBMISSIONS/filename

	# if not source.exists() or source.suffix != ".py":
	if not source.is_file() or source.suffix != ".py":
		abort(404)

	eps_file = RENDER_DIR / f"{source.stem}.eps"
	png_file = RENDER_DIR / f"{source.stem}.png"

	# output = RENDER_DIR / (source.stem + ".eps")
	output = RENDER_DIR / f"{source.stem}.png"


	try:
		result = subprocess.run(
			[
				sys.executable,
				"renderer.py",
				str(source),
				str(output)
			],
			capture_output=True,
			text=True,
			timeout=10
		)

		if result.returncode != 0:
			print("RENDERER ERROR:", flush=True)
			print(result.stdout, flush=True)
			print(result.stderr, flush=True)
			abort(500)

		return send_file(
			output,
			mimetype="image/png"
		)

		# Prevent student programs from opening a permanent Turtle window
		turtle.mainloop = lambda: None
		turtle.done = lambda: None
		turtle.exitonclick = lambda *args, **kwargs: None

	except subprocess.TimeoutExpired:
		print("Renderer timed out!", flush=True)
		abort(500)

		screen = turtle.Screen()
		screen.setup(600, 400)

		root = screen.getcanvas().winfo_toplevel()
		root.withdraw()

		# with open(source, "r", encoding="utf-8") as f:
			# code = f.read()

        # Read student's Python program
		code = source.read_text(encoding="utf-8")

		namespace = {
			"__name__": "__main__"
			, "__file__": str(source),
		}

		exec(
			compile(code, str(source), "exec")
			, namespace
		)

		screen.update()

		canvas = screen.getcanvas()

		canvas.postscript(
			file=str(output)
			, colormode="color"
		)

		screen.bye()

        # Convert EPS -> PNG
		image = Image.open(eps_file)
		image.save(png_file, "PNG")
		image.close()

		return send_file(
			output
			, mimetype="image/eps"
		)

	except Exception:
		print(f"Error rendering {filename}:", flush=True)
		import traceback
		traceback.print_exc()
	# except Exception as e:
		# print(f"Error rendering {filename}:")
		# print(e)
		try:
			turtle.bye()
		except:
			pass
		abort(500)

if __name__ == "__main__":
	app.run(
		host="0.0.0.0"
		, port=5000
		, debug=True
	)