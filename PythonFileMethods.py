__author__ = 'Pneumatic'
string = "what's up?"
file = open("file.txt", "w")  # create a new file called file.txt if it doesn't exists already
# file.close()  # close the connection to file
# file.flush()  # flushes the internal buffer, python flushed when .close() is called as well
file.fileno()
file.isatty()  # Returns True if the file is connected to a tty(-like, computer terminal) device, else False
# returns the integer file descriptor thats used by the underlying implementation to request I/O operations from the os
# file.read(10) Reads at most size bytes from the file (less if the read hits End-Of-File before obtaining size bytes)
# file.readline(10)  # Reads one entire line from the file. A trailing newline character is kept in the string
# file.readlines() Reads until EOF using readline() and return a list with the lines. If sizehint argument is present
# instead of reading up to EOF, whole lines totalling approximately sizehint bytes are read.
file.seek(0, 0)  # Sets the file's current position, SYNTAX file.seek(offset[, whence])
file.tell()  # returns the files current position
file.truncate()  # Truncates the file's size. If the size argument is present, file is truncated to (at most) that size
file.write(string)  # writes variable string to the file
file.writelines(string)  # Writes sequence of strings to the file. The sequence is any iterable object producing strings