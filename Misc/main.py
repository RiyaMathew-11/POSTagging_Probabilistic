# This is a sample Python script that demonstrates file handling
import os
import io

os.open('/code.txt',
        os.O_RDWR | os.O_CREAT)

file = open('code.txt', mode='w', encoding='utf8')
file.write('''Hi, I am Riya and I am gonna write some code.
Coding is my favourite activity to do.
I love coding in python.''')
file.close()

# printing line by line.
file = open('code.txt', 'r')
for line in file:
    print(line)

file.close()

# Appending to a file

file = open('code.txt', mode='a+', encoding='utf8')
file.write('''\nPython is a scripting language''')

file.close()

file = open('code.txt', 'r')
for line in file:
    print(line)

file.close()