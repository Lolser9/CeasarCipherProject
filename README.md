# CeasarCipherProject
Hello! 

This is my code that passes McCreary's test. Keep in mind I have to print the file_name and command in order for it to pass 

This is a very rough draft. No functions or anything like that yet.

It doesn't use any external modules like os or pathlib, (if we can use those, let me know)

I also used a method for reading in the file not explicitly mentioned in books.
I call open("file", "a+")

Here's what a+ does

``a+''  Open for reading and writing.  The file is created if it does not
         exist. The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.

I also have to call file.seek(0) to read from the beginning of the file

The problem is Zybooks doesn't cover switching modes or .seek(0) whatsoever

If you have any ideas, feel free to hmu
