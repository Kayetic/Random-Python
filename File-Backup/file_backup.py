import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import shutil
import platform
import time

root = tk.Tk()
root.withdraw()

# function to move files
def move_files(file_name, source, destination):
    try:
        shutil.move(source + "/" + file_name, destination)
        print("File moved successfully")
    except shutil.Error as e:
        print("Error: %s" % e)

# function to copy files
def copy_files(file_name, source, destination):
    try:
        shutil.copy(source + "/" + file_name, destination)
        print("File copied successfully")
    except shutil.Error as e:
        print("Error: %s" % e)

### Main ###
while True:
    os.system("cls") if 'Windows' in platform.system() else os.system("clear")
    choice = input("""
[1] Move files
[2] Copy files
[3] Exit
>>> """)
    if choice == "1":
        mb.showinfo("Move files", "Will move only the contents of the folder to the destination")
        source = fd.askdirectory(title="Select source directory")
        destination = fd.askdirectory(title="Select destination directory")
        for file in os.listdir(source):
            move_files(file, source, destination)
    elif choice == "2":
        mb.showinfo("Copy files", "Will copy only the contents of the folder to the destination")
        source = fd.askdirectory(title="Select source directory")
        destination = fd.askdirectory(title="Select destination directory")
        for file in os.listdir(source):
            copy_files(file, source, destination)
    elif choice == "3":
        print("Exiting...")
        time.sleep(0.35)
        break
    else:
        mb.showerror("Error", "Invalid choice")
        continue
