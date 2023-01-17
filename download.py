import urllib.request
from tkinter import ttk

def render_download(url, file_path, root, tk):
    # Crear una barra de progreso
    progress = tk.ttk.Progressbar(root, length=200, mode="determinate", orient="horizontal")
    progress.grid(row=6, padx=10, pady=10, sticky="WE", columnspan=2)

    # Actualiza la barra de progreso
    def progress_callback(block_num, block_size, total_size):
        downloaded = block_num * block_size
        progress["value"] = downloaded
        progress.update()

    # Descargar el archivo
    def download(url, file_path):
        urllib.request.urlretrieve(url, file_path, reporthook=progress_callback)
        progress["value"] = 0

    download(url, file_path)