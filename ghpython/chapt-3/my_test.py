#my_test.py
import my_debugger
debugger = my_debugger.debugger()
debugger.load(r"C:\Windows\System32\calc.exe")
#pid = input("Enter the PID of the process to attach to:")
#debugger.attach(int(pid))

#printf_address = debugger.func_resolve("msvcrt.dll", "printf")
#print("[*] Address of printf:0x%08x" % printf_address)
#debugger.bp_set(printf_address)

# 3.2输出寄存器信息
#list = debugger.enumerate_threads()
#print("thread count:%d" % len(list))
# For each thread in the list we want to
# grab the value of each of the registers
# Building a Windows Debugger 37
'''
for thread in list:
    thread_context = debugger.get_thread_context(thread)
    # Now let's output the contents of some of the registers
    print("[*] Dumping registers for thread ID: 0x%08x" % thread)
    print("[**] Dr0: 0x%08x" % thread_context.Dr0)
    print("[**] Dr1: 0x%08x" % thread_context.Dr1)
    print("[**] Dr2: 0x%08x" % thread_context.Dr2)
    print("[**] Dr3: 0x%08x" % thread_context.Dr3)
    print("[**] Dr6: 0x%08x" % thread_context.Dr6)
    print("[**] Dr7: 0x%08x" % thread_context.Dr7)
    print("[**] EIP: 0x%08x" % thread_context.Eip)
    print("[**] ESP: 0x%08x" % thread_context.Esp)
    print("[**] EBP: 0x%08x" % thread_context.Ebp)
    print("[**] EAX: 0x%08x" % thread_context.Eax)
    print("[**] EBX: 0x%08x" % thread_context.Ebx)
    print("[**] ECX: 0x%08x" % thread_context.Ecx)
    print("[**] EDX: 0x%08x" % thread_context.Edx)
    print("[*] END DUMP")
'''
print('start run.')
debugger.run()
print('end run.')
debugger.detach()
