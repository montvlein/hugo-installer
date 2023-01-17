if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()

    import interface
    interface.create_interface(root, tk)
    from helper import is_admin
    import ctypes
    import sys

    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
        sys.exit()

    root.mainloop()