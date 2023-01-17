def create_interface(root, tk):
    from tkinter import PhotoImage

    root.title("Install Hugo on Windows")
    root.config(bg = '#353740')
    favicon = PhotoImage(file="D:/Documentos/Trabajo-Desarrollo/practicas/python/hugo/static/favicon-32x32.png")
    root.iconphoto(True, favicon)
    root.columnconfigure(0, weight=1)

    # Agregar imagen HUGO a la izquierda
    img = PhotoImage(file="D:/Documentos/Trabajo-Desarrollo/practicas/python/hugo/static/hugo-logo.gif")
    img = img.subsample(15)
    root.img = img
    img_label = tk.Label(root, image=img, bg = '#353740')
    img_label.grid(row=0, column=0, padx=10, pady=10)

    # Agregar checkboxes para Go y Git debajo del texto de bienvenida
    descripcion = tk.Label(root, text="Although not required in all cases, Git and Go are often used when working with Hugo.", bg = '#353740', fg='#fff', wraplength=300)
    descripcion.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    from helper import is_install, version

    is_go_installed = is_install("go")
    if is_go_installed:
        local_version = version("go")

    go_installer = tk.BooleanVar(value=not is_go_installed)
    desc = f"Golang 1.19.5 ({local_version} is installed)" if is_go_installed else "Golang 1.19.5"
    go_check = tk.Checkbutton(root, text=desc, variable=go_installer)
    go_check.configure(relief="groove", bg = '#353740', fg='#fff', selectcolor="#353740")
    go_check.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    is_git_installed = is_install("git")
    if is_git_installed:
        local_version = version("git")

    git_installer = tk.BooleanVar(value=not is_git_installed)
    desc = f"Git 2.39.0.2 ({local_version} is installed)" if is_git_installed else "Git 2.39.0.2"
    git_check = tk.Checkbutton(root, text=desc, variable=git_installer)
    git_check.configure(relief="groove", bg = '#353740', fg='#fff', selectcolor="#353740")
    git_check.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    extended_hugo = tk.IntVar(value=0)
    extended_check = tk.Checkbutton(root, text="Hugo Extended", variable=extended_hugo)
    extended_check.configure(relief="groove", bg = '#353740', fg='#fff', selectcolor="#353740")
    extended_check.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def on_submit():
        go = go_installer.get()
        git = git_installer.get()
        extended = extended_hugo.get()
        import installer
        installer.install(root, tk, go, git, extended)

    submit_button = tk.Button(root, text="Instalar", command=on_submit)
    submit_button.configure(width=10, height=2, relief='solid', fg='green', bg='white')
    submit_button.grid(row=7, column=0, padx=10, pady=10, sticky="E")