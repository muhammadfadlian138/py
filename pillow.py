#!/usr/bin/env python3

import sys
import os
import tkinter
from PIL import Image
import turtle


def render(input_file, output_file):

    # Create the Turtle screen
    screen = turtle.Screen()

    # Hide the actual Tk window
    root = screen.getcanvas().winfo_toplevel()
    root.withdraw()

    # Make sure Turtle doesn't wait for GUI interaction
    turtle.mainloop = lambda: None
    turtle.done = lambda: None
    turtle.exitonclick = lambda *args, **kwargs: None

    # Read student's program
    with open(input_file, "r", encoding="utf-8") as f:
        code = f.read()

    # Execute the student's Turtle program
    namespace = {
        "__name__": "__main__",
        "__file__": os.path.abspath(input_file),
    }

    exec(compile(code, input_file, "exec"), namespace)

    # Make sure all drawing operations are completed
    screen.update()

    # Get the underlying Tk canvas
    canvas = screen.getcanvas()

    # Export canvas as PostScript
    ps_file = output_file + ".ps"

    canvas.postscript(
        file=ps_file,
        colormode="color"
    )

    # Convert PostScript → PNG
    image = Image.open(ps_file)
    image.save(output_file, "PNG")

    # Clean up
    image.close()

    os.remove(ps_file)

    try:
        screen.bye()
    except:
        pass

    print(f"Created: {output_file}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python render_turtle.py student.py")
        print()
        print("Or:")
        print("  python render_turtle.py student.py output.png")
        sys.exit(1)

    input_file = sys.argv[1]

    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        output_file = os.path.splitext(input_file)[0] + ".png"

    render(input_file, output_file)