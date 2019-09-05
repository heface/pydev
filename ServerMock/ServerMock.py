# -*- coding: utf-8 -*-
import os
import logging
import logging.config
import json
import datetime
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import make_response

app = Flask(__name__)
dataMap = {} #模拟数据
descMap = {} #接口描述

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return _getInterfaceList()
    except:
        logging.exception("Unexpected exception", exc_info=True)
        return '<h1>内部异常！</h1>'

def _getInterfaceList():
    head = '''<!DOCTYPE HTML><html>
	<head><title>MockInterface</title></head>
	<body>		
		<form method="POST" action="/refresh">
            <input type="submit" value="refresh" />
		<table border="1">
			<caption>模拟接口</caption>			
			<thead><tr><th>No.</th><th>URL</th><th>method</th><th>describe</th></tr></thead>
            <tbody>'''
    tail = '''</tbody><tfoot><tr><th colspan="5"> & copy; 2019 Bank of China</th></tr></tfoot>
		</table></body></html>'''
    cycle = '''<tr><th>{0}</th><td>{1}</td><td>{2}</td><td>{3}</td></tr>'''
    res = head
    i = 0 #计数
    for key,value in dataMap.items():
        if isinstance(value,str):#url地址直接映射返回字符串
            i+=1
            res += cycle.format(i,key,"-",descMap.get(key,"-"))
            
        elif isinstance(value,dict):#url地址+method映射返回字符串
            for method,response in value.items():
                i+=1
                res += cycle.format(i,key,method,descMap.get(key+'-'+method,"-"))
        else:
            continue
    
    res += tail
    logging.info("interface list:"+res)
    return res
    
        
@app.route('/refresh', methods=['GET', 'POST']) 
@app.before_first_request
def loadInterfaceDef():
    for filename in os.listdir('./mock'):
        if len(filename)> 4 and filename[-3:] == 'ini':
            testFile = os.path.join('./mock',filename)
            print("testFile:"+testFile)
            _loadFromFile(testFile)

    logging.info("datamap:%s",dataMap)
    return '<h1>已更新！</h1>'


#记录注释内容    
def _recordDesc(curData,desc):
    if len(curData['iCondition']) > 0:
        descMap[curData['bName']+'-'+curData['iName']+'-'+curData['iCondition']] = desc
    elif len(curData['iName']) > 0:
        descMap[curData['bName']+'-'+curData['iName']] = desc
    else:        
        descMap[curData['bName']] = desc

        
#缓存清理、转储
#curData -
def _memory(curData,data,level,dest):
    if level == 2:#condition
        pass
    elif level == 1:#method
        pass
    elif level == 0:#url
        pass
    else:
        return
        



def _loadFromFile(filename):
    try:
        f = open(filename,"r",encoding="utf8")
        curData = {
            'bName':'',#当前 URL地址
            'iName':'',#当前 请求method
            'iCondition':'',#条件
            'iData':''#返回报文模拟数据
        }
        for line in f.readlines():
            if len(line) < 1:#跳过空行
                continue
            elif line[0] == '#':
                _recordDesc(curData,line[1:])
            elif len(line) > 0 and line[0] == '$':#应用分支
                if len(bName) > 0: #转存、清理
                    if len(iName) > 0:
                        dataMap[bName][iName] = iData
                    else:
                        dataMap[bName] = iData
                    iData = ''
                    iName = ''
                bName = line[1:].strip()
                if bName not in dataMap:
                    dataMap[bName] = {}    
            elif len(line) > 0 and line[0] == '@':#接口定义标记
                if len(iName) > 0:                    
                    dataMap[bName][iName] = iData
                    iData = ''
                    iName = ''
                iName = line[1:].strip()
            else:
                iData = iData + line
        
        if bName:
            if iName:
                dataMap[bName][iName] = iData
            else:
                dataMap[bName] = iData

    except:
        logging.info("Except in loadInterfaceDef.")
        logging.exception("Unexpected exception", exc_info=True)
    finally:
        f.close()

def _loadFromFileNew(filename):
    try:
        f = open(filename,"r",encoding="utf8")
        bName = ''#URL地址
        iName = ''#请求method
        iData = ''#返回模拟数据
        for line in f.readlines():
            if len(line) < 1:#跳过空行
                continue
            elif line[0] == '#':
                if len(iName) > 0:
                    descMap[bName+'-'+iName] = line[1:]
                else:
                    descMap[bName] = line[1:]
            elif len(line) > 0 and line[0] == '$':#应用分支
                if len(bName) > 0: #转存、清理
                    if len(iName) > 0:
                        dataMap[bName][iName] = iData
                    else:
                        dataMap[bName] = iData
                    iData = ''
                    iName = ''
                bName = line[1:].strip()
                if bName not in dataMap:
                    dataMap[bName] = {}    
            elif len(line) > 0 and line[0] == '@':#接口定义标记
                if len(iName) > 0:                    
                    dataMap[bName][iName] = iData
                    iData = ''
                    iName = ''
                iName = line[1:].strip()
            elif len(line) > 0 and line[:11] == '&condition:':#特殊标记（增加条件支持）
                if len(iName) > 0:#有method定义
                    if isinstance(dataMap[bName][iName], str):
                        dataMap[bName][iName] = iData
                    elif isinstance(dataMap[bName][iName], list):
                        if len(dataMap[bName][iName]) > 0:#已经存在列表
                            dataMap[bName][iName][-1]["data"]=iData
                            dataMap[bName][iName].append({"condition":line[12:],"data":""})
                        else:
                            dataMap[bName][iName].append({"condition":line[12:],"data":""})
                else:#无method定义
                    if isinstance(dataMap[bName], str):
                        dataMap[bName] = iData
                    elif isinstance(dataMap[bName], list):
                        if len(dataMap[bName]) > 0:#已经存在列表
                            dataMap[bName][-1]["data"]=iData
                            dataMap[bName].append({"condition":line[12:],"data":""})
                        else:
                            dataMap[bName].append({"condition":line[12:],"data":""})


            else:
                iData = iData + line
        
        if bName:
            if iName:
                dataMap[bName][iName] = iData
            else:
                dataMap[bName] = iData

    except:
        print("Except in loadFile:%s" % filename)
        logging.info("Except in loadInterfaceDef.")
        logging.exception("Unexpected exception", exc_info=True)
    finally:
        f.close()
        
@app.route('/<path:name>', methods=['GET', 'POST'])
def processRequest(name):
    try:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'url:',name)
        bName = name
        
        method = request.args.get("method")
        if method:
            method = method.strip()
        logging.info("method:%s", method)
        print('method:',method)
        
        reqData = request.get_data()
        logging.info("reqData:'%s'", reqData)
        print('reqData:',reqData)

        if bName in dataMap:
            logging.info("dataMap:'%s'", dataMap)
            rBranch = dataMap.get(bName)
            if method:
                resData = rBranch.get(method,"{undefined method:%s}" % method)
            else:
                resData = rBranch
        else:
            resData = "{undefined branch:%s}" % bName
        
        logging.info("resData:'%s'",resData)
        print('resData:',resData)
        
        if resData[0] == '>':#页面重定向
            return redirect(resData[1:].strip(),302)
        else:
            #return jsonify(resData)
            #return json.dumps(resData)
            return resData
    except:
        logging.exception("Unexpected exception", exc_info=True)
        return '<h1>内部异常！</h1>'            

if __name__ =='__main__':

    logging.basicConfig(filename=os.path.join(os.getcwd(),'flaskLog.txt'), #输出日志文件
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',   #输出log的格式、
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        level=logging.DEBUG)
    app.run(debug=True,host='0.0.0.0',port=5000)
    
    '''
    _loadFromFile("./mock/iams.ini")
    #print("dataMap:",dataMap)
    res = _getInterfaceList()
    print(res)
    '''
