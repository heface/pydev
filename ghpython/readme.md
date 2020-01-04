##第一章代码问题：  
printf调用时，传入的字符串需要转换为byte数组，这是因为python3与python2的字符串是不一样的，py2中字符串就是字符数组，原生不支持UTF8；而py3为了支持utf8字符串和py2不一样了。  
##第三章代码问题：  
创建进程原文中用的是kernel32.CreateProcessA，需要改成kernel32.CreateProcessW，其实仍然是字符串问题，CreateProcessW是支持宽字符的。  

创建进程函数：  
BOOL WINAPI CreateProcessW(  
    LPCSTR lpApplicationName,  --执行程序的路径  
    LPTSTR lpCommandLine,  --传入参数  
    LPSECURITY_ATTRIBUTES lpProcessAttributes,  
    LPSECURITY_ATTRIBUTES lpThreadAttributes,  
    BOOL bInheritHandles,  
    DWORD dwCreationFlags,  --创建标记  
    LPVOID lpEnvironment,  
    LPCTSTR lpCurrentDirectory,  
    LPSTARTUPINFO lpStartupInfo,  --创建子进程时设置属性  
    LPPROCESS_INFORMATION lpProcessInformation  --创建进程后接收信息  
);  

获取进程句柄：  
HANDLE WINAPI OpenProcess(  
    DWORD dwDesiredAccess,  --对将要打开的进程拥有什么样的权限  
    BOOL bInheritHandle，  
    DWORD dwProcessId  --希望获得句柄的进程 ID  
);  

附加到目标进程：  
BOOL WINAPI DebugActiveProcess(  
    DWORD dwProcessId  
);  

捕获调试事件：  
BOOL WINAPI WaitForDebugEvent(  
    LPDEBUG_EVENT lpDebugEvent,  --调试事件  
    DWORD dwMilliseconds  --时长，设置为INFINITE（无限等待）  
);  

调试事件处理后使进程继续执行：  
BOOL WINAPI ContinueDebugEvent(  
    DWORD dwProcessId,  --进程ID（WaitForDebugEvent时获取）  
    DWORD dwThreadId,  --线程ID（WaitForDebugEvent时获取）  
    DWORD dwContinueStatus  --继续执行(DBG_CONTINUE)或抛出异常(DBG_EXCEPTION_NOT_HANDLED)  
);  

获取线程句柄：  
HANDLE WINAPI OpenThread(  
    DWORD dwDesiredAccess,  
    BOOL bInheritHandle,  
    DWORD dwThreadId  --线程标识符  
);  

枚举所有线程：  
HANDLE WINAPI CreateToolhelp32Snapshot(  
    DWORD dwFlags,  --收集的数据类型（线程，进程-TH32CS_SNAPTHREAD，模块，或者堆）  
    DWORD th32ProcessID  
);  

BOOL WINAPI Thread32First(  
    HANDLE hSnapshot,  
    LPTHREADENTRY32 lpte  
);  

BOOL WINAPI Thread32Next(  
    HANDLE hSnapshot,  
    LPTHREADENTRY32 lpte  
);  

获取/改变寄存器的值：  
BOOL WINAPI GetThreadContext(  
    HANDLE hThread,  
    LPCONTEXT lpContext  
);  
BOOL WINAPI SetThreadContext(  
    HANDLE hThread,  
    LPCONTEXT lpContext  
);  


