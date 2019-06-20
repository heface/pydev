# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 08:58:21 2019

@author: hca3085
"""

import os,sys
import os.path as path

def fsplit(filename,size=4.5):
    '''
    文件分割，将给定文件按照固定大小分割成多个文件。filename - 待分割文件名（全路径）,size - 分割后文件大小(M)
    '''
    newFileNames = []
    filesize = path.getsize(filename)
    splitLen = int(size*1024*1024)
    print("FileSize = %s ,Split Length = %s" % (filesize,splitLen))
    if filesize < splitLen:
        return
    
    try:
        f = open(filename,'rb')
        i = 1
        while i*splitLen < filesize:
            newFileNames.append(filename+'.dat'+str(i))
            fw = open(filename+'.dat'+str(i),'wb')            
            t = f.read(splitLen)
            fw.write(t)
            fw.close()
            i = i + 1
            
        newFileNames.append(filename+'.dat'+str(i))
        fw = open(newFileNames[-1],'wb') 
        t = f.read(splitLen)
        fw.write(t)
        fw.close()
    except BaseException as e:  
        print("OS error: {0}".format(e))
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        f.close()
    
    print('splite count:{}'.format(len(newFileNames)))
    return newFileNames

def _getOriginalName(filename):
    pos = filename.rfind('.dat')
    if pos != -1:
        return filename[:pos],filename[:pos+4]
    else:
        return "newFile.dat",filename[:-1]
    

def fjoin(filename):
    '''
    文件合并，将分割文件还原。 filename - 任意分割后文件名（全路径）    
    '''
    try:        
        newName,startName = _getOriginalName(filename)
        fw = open(newName,'wb')
        
        i=1
        rfname = '%s%d' % (startName,i)
        while os.access(rfname,os.F_OK):            
            filesize = path.getsize(rfname)
            f = open(rfname,'rb')
            t = f.read(filesize)
            fw.write(t)
            f.close()
            i = i + 1
            rfname = '%s%d' % (startName,i)

    except BaseException as e:  
        print("OS error: {0}".format(e))
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        fw.flush()
        fw.close()

        
if __name__ == '__main__':
    print('文件分割工具.')
    print('Version 0.1 Beta. Author HCA.')
    
    if len(sys.argv) < 2:
        print('Please input filename(full path) to be split.')
        targetFile = input('splitfile:')
        mode = 'split'
    elif sys.argv[1] == '-J':
        if len(sys.argv) < 3:
            print('Please input filename(full path) to be join')
            targetFile = input('joinfile:')
        else:
            targetFile = sys.argv[2]
        mode = 'join'
    else:
        targetFile = sys.argv[1]
        mode = 'split'
        
    if mode == 'join':
        print('join %s' % targetFile)
        fjoin(targetFile)
    elif mode == 'split':
        if len(sys.argv) > 2:
            print('split %s %s' % (targetFile,sys.argv[2]))
            fsplit(targetFile,float(sys.argv[2]))
        else:
            print('split %s' % targetFile)
            fsplit(targetFile)
    else:
        print('unknow mode!')
    #fsplit(r'D:\tmp\《Maven实战》完整高清版.pdf')
    #print(_getOriginalName(r'd:\tmp\SRSHK.warat81'))
    #fjoin(r'd:\tmp\《Maven实战》完整高清版.pdf.dat1')
    #abc = input("target filename:")
    #fsplit(abc)
    
    #ret = fsplit(r'E:\Ebook\Python\美河提供.Python核心编程.pdf')
    #print(ret)
    
    '''
    if len(sys.argv) < 2:
        print('Please input joinfile:')
        sendfile = input('joinfile:')
    else:
        sendfile = sys.argv[1]
    fjoin(sendfile)
    '''
    print('end split')
