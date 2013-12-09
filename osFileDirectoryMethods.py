__author__ = 'Pneumatic'
import os
import stat

dst = "C:\\Users\TERRY\Documents"
ret = os.access("foo.txt", os.F_OK)  # check to see if the file exists using os.F_OK
print("F_OK - return value %s" % ret)  # print value of ret either true or false, % is just for formatting

ret = os.access("foo.txt", os.R_OK)  # check to see if the file has readability
print("R_OK - return value %s" % ret)  # print value of ret either true or false, % is just for formatting

ret = os.access("foo.txt", os.W_OK)  # check to see if the file has writability
print("W_OK - return value %s" % ret)  # print value of ret either true or false, % is just for formatting

ret = os.access("foo.txt", os.X_OK)  # check to see if the  path can be executed.
print("X_OK - return value %s" % ret)  # print value of ret either true or false, % is just for formatting
# os.chdir() Change the current working directory to directory specified
# Assuming /tmp/foo.txt exists,
os.chmod("foo.txt", stat.S_IXGRP)  # Set a file execute by the group
os.chmod("foo.txt", stat.S_IWOTH)  # Set a file write by others
fd2 = 100
path = "foo.txt"
dst = "C:\\Users\TERRY\Documents\\foo.txt"
# stat.S_ISUID: Set user ID on execution.
# stat.S_ISGID: Set group ID on execution.\
# stat.S_ENFMT: Record locking enforced.
# stat.S_ISVTX: Save text image after execution.
# stat.S_IREAD: Read by owner.
# stat.S_IWRITE: Write by owner.
# stat.S_IEXEC: Execute by owner.
# stat.S_IRWXU: Read, write, and execute by owner.
# stat.S_IRUSR: Read by owner.
# stat.S_IWUSR: Write by owner.
# stat.S_IXUSR: Execute by owner.
# stat.S_IRWXG: Read, write, and execute by group.
# stat.S_IRGRP: Read by group.
# stat.S_IWGRP: Write by group.
# stat.S_IXGRP: Execute by group.
# stat.S_IRWXO: Read, write, and execute by others.
# stat.S_IROTH: Read by others.
# stat.S_IWOTH: Write by others.
# stat.S_IXOTH: Execute by others
paths = "new folders1\\folder 7\\folder 9"
fd = os.open("food.txt", os.O_RDWR | os.O_CREAT)  # open a file, O_RDWR (readable writable) | os.O_Creat(create file)
# os.close(fd)  # closes the file with reference variable fd
os.dup(fd)  # return a duplicate of file descriptor fd
os.dup2(fd, fd2)  # Duplicate file descriptor fd to fd2, closing the latter first if necessary
os.fdopen(fd)  # Return an open file object connected to the file descriptor fd
os.fstat(fd2)  # Return status for file descriptor fd2, like stat().
os.fsync(fd2)  # Force write of file with file descriptor fd2 to disk
os.getcwd()  # Return a string representing the current working directory
os.getcwdb()  # Return a bytestring representing the current working directory
os.isatty(fd)  # Return True if file descriptor fd2 is open & connected to a tty(computer terminal) device, else False.
# os.link(path, dst)  # creates a hard link pointing to path named dst. Is very useful to create a copy of existing file
os.listdir("C:\\Users\TERRY\Documents")  # returns a list containing the names of the entries in the directory given
os.lseek(fd2, 0, 0)  # sets the current position of file descriptor fd to the given position
os.lstat(path)  # similar to fstat except doesn't follow soft link (shortcuts)
# os.makedirs(paths, 0x0777) create a directory recursively(but makes all intermediate directories), default mode 0x0777
# os.mkdir(path, mode) creates the directory specified
# os.pipe() creates a pipe and returns a pair of descriptors to be used to read/write
# os.popen(command, mode, buffersize) opens a pipe to or from command
os.read(fd2, 10)  # Read at most n(10) bytes from file descriptor fd2. Return a string containing the bytes read
# os.readlink(path) Return a string representing the path to which the symbolic link points.
# os.remove(path) remove the path specified
# os.removedirs(path) remove directories recursively(removes all intermediate directories)
# os.rename(old, new) renames the file or directory to whatever is specified
# os.rmdir(path) removes the directory path
os.stat(path)  # Perform a stat system call on the given path.
# os.stat_float_times(newvalue) Determine whether stat_result represents time stamps as float objects.
# os.statvfs_result(path) perform a statvfs system call on the given path.
# os.symlink(src,dst) Create a symbolic link pointing to src named dst, need to have admin privilege
# os.unlink(path) Remove the file path.
# os.utime(path) Set the access and modified times of the file specified by path.
