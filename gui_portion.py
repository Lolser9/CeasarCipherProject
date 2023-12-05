"""
Author: Ezzah Din, Advika Govindarajan, Jaedon Ibarrola, Lukas John,
        Dillon Kumordzie, Caitlyn McLain, Jake Melone, William Payne
Assignment Title: Program 30 - Ceaser Cipher
Assignment Description: Write a program to implement the Caesar Cipher. 
                        Then develop and implement a graphical user 
                        interface (GUI) application using TKinter for 
                        this program.
Due Date: 12/05/23
Date Created: 12/05/23
Date Last Modified: 12/05/23
"""

import tkinter as tk
from tkinter import DISABLED, Entry, Toplevel
from tkinter.scrolledtext import ScrolledText
import CC

# Create Window
window = tk.Tk()
window.title("Encryption Management System")

window_width = 600
window_height = 800

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Don't allow resize
window.resizable(False, False)


# Title
label = tk.Label(
    window,
    text="Welcome to Encryption Management System",
    font=("Helvetica", 22),
    bg="green",
    fg="yellow",
)
label.place(x=0, y=0, width=600, height=60)

# Textboxes
message_label = tk.Label(window, text="File Name:", font=("Helvetica", 15))
message_label.place(x=25, y=100)

file_text = Entry(window, width=30, justify="left")
file_text.place(x=130, y=106)

message_label = tk.Label(window, text="Type:", font=("Helvetica", 15))
message_label.place(x=330, y=100)

type_text = Entry(window, width=30, justify="left")
type_text.place(x=400, y=106)

message_label = tk.Label(window, text="User ID:", font=("Helvetica", 15))
message_label.place(x=45, y=150)

user_id = Entry(window, width=30, justify="left")
user_id.place(x=130, y=156)

message_label = tk.Label(window, text="Date:", font=("Helvetica", 15))
message_label.place(x=330, y=150)

date_text = Entry(window, width=30, justify="left")
date_text.place(x=400, y=156)

#############
message_label = tk.Label(window, text="Shift", font=("Helvetica", 15))
message_label.place(x=333, y=200)

shift_text = Entry(window, width=4, justify="center")
shift_text.place(x=342, y=238)
shift_text.insert(1, "3")

message_label = tk.Label(window, text="Original Text:")
message_label.place(x=270, y=400)

before_text = ScrolledText(window, width=50, height=10)
before_text.place(x=100, y=425)

message_label = tk.Label(window, text="Altered Text:")
message_label.place(x=270, y=595)

after_text = ScrolledText(window, width=50, height=10)
after_text.place(x=100, y=620)


# Button Functions
def get_file(file_name):
    if CC.file_exists(file_name):
        f = open(file_name)
        lines = f.readlines()
        f.close()

        contents = ""
        for line in lines:
            contents += line

        before_text.delete("1.0", "end")
        before_text.insert("1.0", contents)

        # Success
        label = tk.Label(
            window,
            text="File opened successfully.",
            font=("Helvetica", 22),
            bg="green",
            fg="yellow",
        )

        label.place(x=0, y=355, width=600)
    else:
        # Failure
        label = tk.Label(
            window,
            text="File doesn't exist",
            font=("Helvetica", 22),
            bg="red",
            fg="yellow",
        )

        label.place(x=0, y=355, width=600)


def open_popup(file_name):
    if CC.file_exists(file_name):
        f = open(file_name)
        lines = f.readlines()
        f.close()

        contents = ""
        for line in lines:
            contents += line

        top = Toplevel(window)
        top.geometry("400x400")
        top.title("Display Text")
        top.resizable(False, False)

        popup_text = ScrolledText(top, width=50, height=25)
        popup_text.place(x=0, y=0)
        popup_text.insert("1.0", contents)
        popup_text.config(state=DISABLED)

        # Success
        label = tk.Label(
            window,
            text="File opened successfully.",
            font=("Helvetica", 22),
            bg="green",
            fg="yellow",
        )

        label.place(x=0, y=355, width=600)
    else:
        # Failure
        label = tk.Label(
            window,
            text="File doesn't exist",
            font=("Helvetica", 22),
            bg="red",
            fg="yellow",
        )

        label.place(x=0, y=355, width=600)


def encrypt():
    after_text.delete("1.0", "end")

    after_text.insert(
        "1.0",
        CC.encryptor(
            before_text.get("1.0", "end").splitlines(),
            int(shift_text.get()),
        ),
    )


def decrypt():
    after_text.delete("1.0", "end")

    after_text.insert(
        "1.0",
        CC.encryptor(
            before_text.get("1.0", "end").splitlines(),
            int(shift_text.get()) * -1,
        ),
    )


# Buttons
file_button = tk.Button(
    window,
    text="Open File",
    width=10,
    height=3,
    command=lambda: get_file(file_text.get() + "" + type_text.get()),
    fg="green",
)
file_button.place(x=40, y=200)

display_button = tk.Button(
    window,
    text="Display Contents",
    width=25,
    height=3,
    command=lambda: open_popup(file_text.get() + "" + type_text.get()),
    fg="green",
)
display_button.place(x=130, y=200)

encrypt_button = tk.Button(
    window,
    text="Encrypt",
    width=12,
    height=3,
    command=lambda: encrypt(),
    fg="red",
)
encrypt_button.place(x=400, y=200)

decrypt_button = tk.Button(
    window, text="Decrypt", width=12, height=3, command=lambda: decrypt(), fg="red"
)
decrypt_button.place(x=490, y=200)

exit_button = tk.Button(
    window, text="Exit", width=40, height=3, command=lambda: window.quit()
)
exit_button.place(x=160, y=280)

window.mainloop()
