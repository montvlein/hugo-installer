import ctypes
import subprocess

def is_admin():
     try:
         return ctypes.windll.shell32.IsUserAnAdmin()
     except:
         return False

def is_install(program):
    command = "--version" if program == "git" else "version"
    try:
        subprocess.run([program, command])
        return True
    except FileNotFoundError:
        return False

def version(program):
    command = "--version" if program == "git" else "version"
    result = subprocess.run([program, command], capture_output=True, text=True)
    return result.stdout