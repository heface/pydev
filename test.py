#!/data/data/com.termux/files/usr/bin/python
instr = 'to'
outstr = 'TO'
old_str = 'Hello world , welcome to use Python. 123456'
remove = '12345'
table = str.maketrans(instr,outstr,remove)
new_str = old_str.translate(table)
print(new_str)

