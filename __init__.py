import os
import subprocess
import json
from .lib.colors import fg, bg
from .lib.styles import underline, bold, italic, inverse, hidden, strikethrough
from .lib.extras import rainbow, zebra, trap, freaky

if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "ansi_test.json")):
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "index.py")):
        subprocess.run(["python3", os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "index.py")])
    else:
        print(f"Error: {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests', 'index.py')} not found.")
else:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "ansi_test.json"), "r") as _:
        if not json.load(_).get("ansi_tested", False):
            if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "index.py")):
                subprocess.run(["python3", os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "index.py")])
            else:
                print(f"Error: {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests', 'index.py')} not found.")

__all__ = [
    "fg",
    "bg",
    "underline",
    "bold",
    "italic",
    "inverse",
    "hidden",
    "strikethrough",
    "rainbow",
    "zebra",
    "trap",
    "freaky"
]

__version__ = "0.1.0"
__author__ = "AlmightyNan"
