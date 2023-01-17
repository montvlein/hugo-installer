from distutils.core import setup
import py2exe

setup(
    windows=[{"script": "main.py", "icon_resources": [(1, "D:\Documentos\Trabajo-Desarrollo\practicas\python\hugo\static/favicon-32x32.ico")],
     "dest_base":"hugo_installer"}],
    options={
        "py2exe": {
            "packages": ["os", "ctypes", "sys", "tkinter", "urllib.request"],
            "includes": ["tkinter"],
            "excludes": ["tkinter"],
            "compressed": 1,
            "optimize": 2,
            "bundle_files": 3,
            "dll_excludes": ["MSVCP90.dll"],
            "dist_dir": "dist",
        }
    },
)
