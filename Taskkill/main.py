import tkinter as tk
from tkinter import filedialog as fd
import psutil
import time
import signal

root = tk.Tk()
root.withdraw()

def handler(signum, frame):
    print('What are you, mentally weak?')

signal.signal(signal.SIGINT, handler)

temp = open("Taskkill/blacklist.txt")
programs = temp.read().splitlines()

print(programs)

choice = input("Do you want to blacklist a program? (y/n) ")
if choice == "y":
    program_path = fd.askopenfilename(filetypes=[("Program", "*.exe")])
    program_name = program_path.split("/")[-1]
    programs.append(program_name)
    temp = open("blacklist.txt", "w")
    for program in programs:
        temp.write(program + "\n")
    temp.close()
    print(f"Added {program_name} to the blacklist")

while True:
    for program in psutil.process_iter():
        if program.name() in programs:
            program.kill()
            print(f"Killing {program.name()}")
    time.sleep(1)
