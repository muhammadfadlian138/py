import sys
import turtle
from pathlib import Path

from PIL import Image


source = Path(sys.argv[1])
output = Path(sys.argv[2])


# Disable commands that would normally wait for a GUI
turtle.done = lambda: None
turtle.mainloop = lambda: None
turtle.exitonclick = lambda *args, **kwargs: None


# Create fresh Turtle screen
screen = turtle.Screen()
screen.setup(600, 400)

# Hide the actual Tk window
root = screen.getcanvas().winfo_toplevel()
root.withdraw()


# Run student's program
code = source.read_text(encoding="utf-8")

namespace = {
    "__name__": "__main__",
    "__file__": str(source),
}

exec(compile(code, str(source), "exec"), namespace)


# Render
screen.update()

canvas = screen.getcanvas()

eps = output.with_suffix(".eps")

canvas.postscript(
    file=str(eps),
    colormode="color"
)

screen.bye()


# EPS → PNG
image = Image.open(eps)
image.save(output, "PNG")
image.close()

eps.unlink(missing_ok=True)
