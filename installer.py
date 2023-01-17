import os
import subprocess
from download import render_download
from tkinter import messagebox

def install(root, tk, go, git, extended):
    if go:
        file_name = "go1.19.5.windows-amd64.msi"
        url = f"https://go.dev/dl/{file_name}"
        render_download(url, file_name, root, tk)
        os.system(f"msiexec.exe /i {file_name} /norestart")
    if git:
        file_name = "Git-2.39.0.2-64-bit.exe"
        url = f"https://github.com/git-for-windows/git/releases/download/v2.39.0.windows.2/{file_name}"
        render_download(url, file_name, root, tk)
        subprocess.run(file_name)
    if extended:
        subprocess.run(["go", "install", "-tags", "extended", "github.com/gohugoio/hugo@latest"])
    else:
        subprocess.run(["go", "install", "github.com/gohugoio/hugo@latest"])
    messagebox.showinfo("Instalador", "Instalación completada!")
    root.destroy()