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

# DA
shifter = 3


def encryptor(lines, shift):
    new_lines = list()

    for line in lines:
        new_line = ""
        for char in line:
            try:
                new_line += chr(ord(char) + shift)
            except ValueError:
                return "Unable to encrypt/decrypt"
        new_lines.append(new_line)

    return "\n".join(new_lines)


def file_exists(file_name):
    try:
        f = open(file_name, "r")
        f.close()
        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    # Input
    file_name = input("Please Enter A File Name: ")
    print(file_name)
    command = input("Please Enter A Command (encrypt or decrypt): ")
    print(command)

    # Process
    if command != "encrypt" and command != "decrypt":
        print("Error: Bad Command.")

    if file_exists(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            # Output
            print("Error: File did NOT open.")
        else:
            if command == "decrypt":
                # Output
                print(encryptor(lines, shifter * (-1)))
            if command == "encrypt":
                # Output
                print(encryptor(lines, shifter))
    else:
        # Output
        print("Error: File did NOT open.")

# Assumptions
# User enters a file that exists
