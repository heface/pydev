from ctypes import *
import platform

#windows版本
def testWinDLL():
    msvcrt = cdll.msvcrt
    print(msvcrt.printf)
    msg = b"Hello"
    msvcrt.printf(b"test msg:%s Windows!\n", msg)

#linux版本
def testLinuxSO():
    libc = CDLL('libc.so.6')
    msg = b"Hello"
    libc.printf(b"test msg:%s Linux!\n", msg)

if __name__ == '__main__':
    sysName = platform.system()
    if(sysName == "Windows"):    
        testWinDLL()
    elif(sysName == "Linux"):
        testLinuxSO()
    else:
        print("unknown system.")