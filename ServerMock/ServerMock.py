# -*- coding: utf-8 -*-
import os
import logging
import logging.config
import json
import datetime
from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)
dataMap = {}
#  模拟数据
descMap = {}
#  接口描述
nDataMap = {}
#  新的模拟数据（处理条件分支）


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
    i = 0
    for key, value in dataMap.items():
        #  url地址直接映射返回字符串
        if isinstance(value, str):
            i += 1
            res += cycle.format(i, key, "-", descMap.get(key, "-"))
        #  url地址+method映射返回字符串
        elif isinstance(value, dict):
            for method, response in value.items():
                i += 1
                res += cycle.format(i, key, method,
                                    descMap.get(key + '-' + method, "-"))
        else:
            continue
    res += tail
    logging.info("interface list:"+res)
    return res


@app.route('/refresh', methods=['GET', 'POST'])
@app.before_first_request
def loadInterfaceDef():
    for filename in os.listdir('./mock'):
        if len(filename) > 4 and filename[-3:] == 'ini':
            testFile = os.path.join('./mock', filename)
            print("testFile:", testFile)
            _loadFromFile(testFile)

    logging.info("datamap:%s", dataMap)

    _processConditon()
    return '<h1>已更新！</h1>'


#  处理条件分支
def _processConditon():
    for (k, v) in dataMap.items():
        if isinstance(v, dict):
            nDataMap[k] = {}
            for (key, value) in v.items():
                if "{condition}" in key:
                    print("condition:%s" % key)
                    conditions = key.split("{condition}")
                    if conditions[0] in nDataMap[k] and isinstance(
                            nDataMap[k][conditions[0]], dict):
                        nDataMap[k][conditions[0]][conditions[1]] = value
                    elif conditions[0] not in nDataMap[k]:
                        nDataMap[k][conditions[0]] = {conditions[1]: value}
                    else:
                        print("error , has key:%s and not condition"
                              % conditions[0])
                else:
                    nDataMap[k][key] = value
        else:
            nDataMap[k] = v


#  记录注释内容
def _recordDesc(curData, desc):
    if len(curData['iName']) > 0:
        descMap[curData['bName']+'-'+curData['iName']] = desc
    else:
        descMap[curData['bName']] = desc


def _loadFromFile(filename):
    try:
        f = open(filename, "r", encoding="utf8")
        bName = ''
        #  当前 URL地址
        iName = ''
        #  当前 请求method
        iData = ''
        #  当前 请求报文

        for line in f.readlines():
            #  跳过空行
            if len(line) < 1:
                continue
            elif line[0] == '#':
                _recordDesc({"bName": bName, "iName": iName}, line[1:])
            #  应用分支
            elif len(line) > 0 and line[0] == '$':
                #  转存、清理
                if len(bName) > 0:
                    if len(iName) > 0:
                        dataMap[bName][iName] = iData
                    else:
                        dataMap[bName] = iData
                    iData = ''
                    iName = ''
                bName = line[1:].strip()
                if bName not in dataMap:
                    dataMap[bName] = {}
            #  接口定义标记
            elif len(line) > 0 and line[0] == '@':
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


@app.route('/<path:name>', methods=['GET', 'POST'])
def processRequest(name):
    try:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
              'url:', name)
        bName = name
        method = request.args.get("method")
        if method:
            method = method.strip()
        logging.info("method:%s", method)
        print('method:', method)

        req = request.get_data()
        logging.info("reqData:'%s'", req)
        print('reqData:', req)

        if bName in dataMap:
            #  logging.info("dataMap:'%s'", dataMap)
            rBranch = dataMap.get(bName)
            if method:
                resData = rBranch.get(method, "{undefined method:%s}" % method)
                #  add branch condition process
                if isinstance(resData, dict):
                    for (k, v) in resData.items():
                        if eval(k):
                            resData = v
                            break
                        else:
                            resData = "{none condition equals:%s}" % req
            else:
                resData = rBranch
        else:
            resData = "{undefined branch:%s}" % bName

        logging.info("resData:'%s'", resData)
        print('resData:', resData)

        #  页面重定向
        if resData[0] == '>':
            return redirect(resData[1:]. strip(), 302)
        else:
            #  return jsonify(resData)
            #  return json.dumps(resData)
            return resData
    except:
        logging.exception("Unexpected exception", exc_info=True)
        return '<h1>内部异常！</h1>'


if __name__ == '__main__':
    '''
     #  flaskLog.txt - 输出日志文件     format - 输出log的格式
    logging.basicConfig(filename=os.path.join(os.getcwd(),'flaskLog.txt'),
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        level=logging.DEBUG)
    app.run(debug=True,host='0.0.0.0',port=5000)

    '''
    _loadFromFile("./mock/barter.ini")
    _loadFromFile("./mock/fams-ssop.ini")
    _processConditon()
    #  print("dataMap:",dataMap)
    with open("testJson.ini", "w") as of:
        json.dump(nDataMap, of)

    #  res = _getInterfaceList()
    #  print(res)
