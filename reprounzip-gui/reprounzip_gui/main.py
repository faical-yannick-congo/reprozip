from __future__ import division, print_function, unicode_literals

from reprounzip_gui import tkinter_compat as tk


class MainWindow(object):
    def __init__(self, root):
        self.root = root

        # Form to select paths
        form = tk.Frame(root)
        tk.Grid.columnconfigure(form, 1, weight=1)

        lf = tk.Label(form, text="File to unpack:")
        lf.grid(row=0, column=0, sticky=tk.W)

        bf = tk.Button(form, text="(unselected)")
        bf.grid(row=0, column=1, sticky=tk.W + tk.E)

        lt = tk.Label(form, text="Target:")
        lt.grid(row=1, column=0, sticky=tk.W)

        bt = tk.Button(form, text="(unselected)")
        bt.grid(row=1, column=1, sticky=tk.W + tk.E)

        form.pack(fill=tk.BOTH)

        # Spacer
        tk.LabelFrame(root).pack(fill=tk.BOTH)

        # Buttons
        buttons = tk.Frame(root)

        unpack = tk.Button(buttons, text="Unpack", command=self.unpack)
        unpack.pack(side=tk.RIGHT)

        destroy = tk.Button(buttons, text="Destroy", command=self.destroy)
        destroy.pack(side=tk.RIGHT)

        buttons.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def unpack(self):
        print("UNPACK")

    def destroy(self):
        print("DESTROY")
        self.root.destroy()


def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
