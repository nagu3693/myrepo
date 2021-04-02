#!/usr/local/bin/python3.6
"""
This wll open the file
"""
xmen_file= open('xmen_base.txt')

"""
This below read command will show the contents of the file that is store in xmen_file
"""

xmen_file.read()

"""
seek is going to position the read pointe to top of the file when value is 0  and alters the posistion base on input provide by user
"""

xmen_file.seek(0)

"""
To know the file name assigned to xmen_file
"""
xmen_file.name

"""
write a file by truncating the content of file or creating a new file with w option
"""

new_file = open('new_file.txt', 'w')

"""
write and close a file by adding content by appending it
"""

with open('new_file.txt', 'a') as f:
        f.write("Professor Xavier\n")
