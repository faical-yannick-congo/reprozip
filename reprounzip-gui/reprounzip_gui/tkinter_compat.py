from __future__ import division, print_function, unicode_literals

import sys


PY3 = sys.version_info[0] == 3

if PY3:
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox

    askopenfilename = tkinter.filedialog.askopenfilename
    asksaveasfilename = tkinter.filedialog.asksaveasfilename
    showerror = tkinter.messagebox.showerror
else:
    import Tkinter as tk
    import tkFileDialog
    import tkMessageBox

    askopenfilename = tkFileDialog.askopenfilename
    asksaveasfilename = tkFileDialog.asksaveasfilename
    showerror = tkMessageBox.showerror


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

NORMAL = tk.NORMAL
DISABLED = tk.DISABLED
ACTIVE = tk.ACTIVE
HIDDEN = tk.HIDDEN
