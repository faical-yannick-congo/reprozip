from __future__ import division, print_function, unicode_literals

from reprounzip.utils import PY3


if PY3:
    import tkinter as tk
else:
    import Tkinter as tk


Tk = tk.Tk

Button = tk.Button
Frame = tk.Frame
Label = tk.Label
LabelFrame = tk.LabelFrame
OptionMenu = tk.OptionMenu
Toplevel = tk.Toplevel

Grid = tk.Grid

StringVar = tk.StringVar

N, S, W, E = tk.N, tk.S, tk.W, tk.E
NONE, X, Y, BOTH = tk.NONE, tk.X, tk.Y, tk.BOTH
LEFT, TOP, RIGHT, BOTTOM = tk.LEFT, tk.TOP, tk.RIGHT, tk.BOTTOM
