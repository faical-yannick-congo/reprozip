from __future__ import division, print_function, unicode_literals

from reprounzip_gui import tkinter_compat as tk


class MainWindow(object):
    def __init__(self, root):
        self.window = root

        # Form to select paths
        form = tk.Frame(self.window)
        tk.Grid.columnconfigure(form, 1, weight=1)
        tk.Label(form, text="Unpacked directory:") \
            .grid(row=0, column=0, sticky=tk.W)
        tk.Button(form, text="(unselected)") \
            .grid(row=0, column=1, sticky=tk.W + tk.E)
        tk.Button(form, text="Unpack a .RPZ file...", command=self.unpack) \
            .grid(row=1, column=0, columnspan=2, sticky=tk.E)
        form.pack(fill=tk.BOTH)

        # Spacer
        tk.LabelFrame(self.window).pack(fill=tk.BOTH)

        # Buttons
        buttons = tk.Frame(self.window)

        unpack = tk.Button(buttons, text="Unpack", command=self.unpack)
        unpack.pack(side=tk.RIGHT)

        destroy = tk.Button(buttons, text="Destroy", command=self.destroy)
        destroy.pack(side=tk.RIGHT)

        buttons.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def unpack(self):
        unpacked_path = UnpackDialog.unpack(self.window)
        if unpacked_path is not None:
            print("UNPACKED: %r" % unpacked_path)
            # TODO

    def destroy(self):
        # TODO
        print("DESTROY")
        self.window.destroy()


class UnpackDialog(object):
    unpacked_path = None

    def __init__(self, parent):
        self.window = tk.Toplevel()

        tk.Label(self.window, text="File to unpack:") \
            .grid(row=0, column=0, sticky=tk.W)
        tk.Button(self.window, text="(unselected)") \
            .grid(row=0, column=1, sticky=tk.W + tk.E)
        tk.Label(self.window, text="Unpacker to use:") \
            .grid(row=1, column=0, sticky=tk.W)
        self.unpacker = tk.StringVar(self.window)
        self.unpacker.set('directory')
        tk.OptionMenu(self.window, self.unpacker,
                      'directory', 'chroot', 'docker', 'vagrant') \
            .grid(row=1, column=1, sticky=tk.W + tk.E)
        tk.Button(self.window, text="Unpack", command=self._unpack) \
            .grid(row=2, column=0, columnspan=2, sticky=tk.E)

        self.window.transient(parent)
        self.window.grab_set()
        self.window.wait_window(self.window)

    def _unpack(self):
        # TODO
        self.unpack_path = '/tmp'

    @classmethod
    def unpack(cls, parent):
        dialog = cls(parent)
        return dialog.unpacked_path


def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
