from ctypes import *
import time
msvcrt = cdll.msvcrt
counter = 0
while 1:
    msvcrt.printf(("Loop iteration %d!\n" % counter).encode())
    time.sleep(2)
    counter += 1
    
