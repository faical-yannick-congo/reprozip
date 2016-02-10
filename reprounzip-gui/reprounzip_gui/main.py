from __future__ import division, print_function, unicode_literals

import os

from reprounzip_gui import tkinter_compat as tk
from reprounzip_gui import rpuz_interface
from reprounzip_gui.rpuz_interface import ReprounzipError


class MainWindow(object):
    def __init__(self, root):
        self._pack_filename = None

        self.window = root

        # Form to select paths
        form = tk.Frame(self.window)
        tk.Grid.columnconfigure(form, 1, weight=1)
        tk.Label(form, text="Unpacked directory:") \
            .grid(row=0, column=0, sticky=tk.W)
        self._pack_button = tk.Button(form, text="(unselected)")
        self._pack_button.grid(row=0, column=1, sticky=tk.W + tk.E)
        tk.Button(form, text="Unpack a .RPZ file...", command=self.unpack) \
            .grid(row=1, column=0, columnspan=2, sticky=tk.E)
        form.pack(fill=tk.BOTH)

        # Spacer
        tk.LabelFrame(self.window, border=0).pack(fill=tk.BOTH, expand=1)

        tk.Label(self.window, text="[ files will be here ]").pack()

        # Spacer
        tk.LabelFrame(self.window, border=0).pack(fill=tk.BOTH, expand=1)

        tk.Label(self.window, text="[ runs will be here ]").pack()

        # Spacer
        tk.LabelFrame(self.window, border=0).pack(fill=tk.BOTH, expand=1)

        # Buttons
        buttons = tk.Frame(self.window)

        unpack = tk.Button(buttons, text="Unpack", command=self.unpack)
        unpack.pack(side=tk.RIGHT)

        destroy = tk.Button(buttons, text="Destroy", command=self.destroy)
        destroy.pack(side=tk.RIGHT)

        buttons.pack(side=tk.BOTTOM, fill=tk.X)

    def unpack(self):
        self._pack_filename = UnpackDialog.unpack(self.window)
        if self._pack_filename is not None:
            self._pack_button['text'] = self._pack_filename
            # TODO: Activate some buttons
        else:
            self._pack_button['text'] = "(unselected)"
            # TODO: Deactivate buttons

    def destroy(self):
        # TODO
        print("DESTROY")


class UnpackDialog(object):
    def __init__(self, parent):
        self.unpacked_path = None
        self._pack_filename = None
        self._destination_filename = None

        self.window = tk.Toplevel()

        # Form to select paths
        tk.Grid.columnconfigure(self.window, 1, weight=1)
        tk.Label(self.window, text="File to unpack:") \
            .grid(row=0, column=0, sticky=tk.W)
        self._pack_button = tk.Button(self.window, text="(unselected)",
                                      command=self._select_pack)
        self._pack_button.grid(row=0, column=1, sticky=tk.W + tk.E)
        tk.Label(self.window, text="Unpacker to use:") \
            .grid(row=1, column=0, sticky=tk.W)
        self._unpacker = tk.StringVar(self.window)
        self._unpacker.set('directory')
        tk.OptionMenu(self.window, self._unpacker,
                      'directory', 'chroot', 'docker', 'vagrant') \
            .grid(row=1, column=1, sticky=tk.E)
        tk.Label(self.window, text="Destination directory:") \
            .grid(row=2, column=0, sticky=tk.W)
        self._destination_button = tk.Button(self.window, text="(unselected)",
                                             command=self._select_destination)
        self._destination_button.grid(row=2, column=1, sticky=tk.W + tk.E)

        # Spacer
        tk.LabelFrame(self.window).grid(row=3)
        tk.Grid.rowconfigure(self.window, 3, weight=1)

        # Button
        self._unpack_button = tk.Button(self.window, text="Unpack",
                                        state=tk.DISABLED,
                                        command=self._unpack)
        self._unpack_button.grid(row=3, column=0, columnspan=2, sticky=tk.E)

        # Run as modal dialog
        self.window.transient(parent)
        self.window.grab_set()
        self.window.wait_window(self.window)

    def _select_pack(self):
        self._pack_filename = tk.askopenfilename() or None
        if self._pack_filename is not None:
            self._pack_button['text'] = self._pack_filename
            if self._destination_filename is not None:
                self._unpack_button['state'] = tk.NORMAL

    def _select_destination(self):
        self._destination_filename = tk.asksaveasfilename() or None
        if self._destination_filename is not None:
            if os.path.exists(self._destination_filename):
                tk.showerror("Error", "This filename already exists")
                self._destination_filename = None
            else:
                self._destination_button['text'] = self._destination_filename
                if self._pack_filename is not None:
                    self._unpack_button['state'] = tk.NORMAL

    def _unpack(self):
        if not (self._pack_filename and self._destination_filename):
            return

        try:
            self.unpack_path = rpuz_interface.unpack(
                self._pack_filename,
                self._destination_filename,
                self._unpacker.get())
        except ReprounzipError as e:
            tk.showerror("Error while unpacking", e)
        else:
            self.window.destroy()

    @classmethod
    def unpack(cls, parent):
        dialog = cls(parent)
        return dialog.unpacked_path


def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
