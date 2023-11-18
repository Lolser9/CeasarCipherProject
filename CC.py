"""
Author: All authors of the group involved
Assignment Title: Program 30 - Ceaser Cipher
Assignment Description: Write a program to implement the Caesar Cipher. 
                        Then develop and implement a graphical user 
                        interface (GUI) application using TKinter for 
                        this program.
Due Date: 12/05/23
Date Created: 11/13/23
Date Last Modified: 11/13/23
"""

# DA
shift_amount = 3

# Input
file_name = input("Please Enter A File Name: ")
print(file_name)
command = input("Please Enter A Command (encrypt or decrypt): ")
print(command)

# Process
if command != "encrypt" and command != "decrypt":
    print("Error: Bad Command.")

file = open(file_name, "a+")
file.seek(0)

lines = file.readlines()
file.close()

new_lines = list()

if len(lines) == 0:
    print("Error: File did NOT open.")
else:
    if command == "decrypt":
        for line in lines:
            new_line = ""
            for char in line:
                new_line += chr(ord(char) - shift_amount)
            new_lines.append(new_line)

        message = "\n".join(new_lines)
        print(message)

    if command == "encrypt":
        for line in lines:
            new_line = ""
            for char in line:
                new_line += chr(ord(char) + shift_amount)
            new_lines.append(new_line)

        message = "\n".join(new_lines)
        print(message)
