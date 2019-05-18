# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:25:56 2018

@author: he
"""

'''
compute pe -- 计算市盈率
condition:
    0<PE<30
    PE从小到大排序,剔除停牌,取前100
    再平衡周期:7个交易日
'''

from pymongo import DESCENDING, UpdateOne

from database import DB_CONN
from stock_util import get_all_codes

finance_report_collection = DB_CONN['finance_report']
daily_collection = DB_CONN['daily']

def compute_pe():
    codes = get_all_codes()
    
    for code in codes:
        daily_cursor = daily_collection.find(
                {'code':code},
                projection = {'close':True,'date':True})
        
        update_requests = []
        for daily in daily_cursor:
            _date = daily['date']
            
            finance_report = finance_report_collection.find_one(
                    {'code': code, 'report_date': {'$regex': '\d{4}-12-31'}, 'announced_date': {'$lte': _date}},
                    sort = [('announced_date', DESCENDING)])

            if finance_report is None:
                continue
            
            eps = 0
            if finance_report['eps'] != '-':
                eps = finance_report['eps]
                
            if eps != 0:
                update_requests.append(UpdateOne(
                        {'code': code, 'date': _date},
                        {'$set': {'pe': round(daily['close'] / eps, 4)}}))
            
        if len(update_requests) > 0:
            update_result = daily_collection.bulk_write(update_requests, prderaed = False)
            print('update PE, %s, update: %d' % (code, update_result.modified_count))
            
            

def get_all_codes(date=None):
    datetime_obj = datetime.now()
    if date is None:
        date = datetime_obj.strftime('%Y-%m-%d')
        
    codes = []
    while len(codes) == 0:
        code_cursor = DB_CONN.basic.find(
                {'date': date},
                projection = {'code': True, '_id': False})
        
        codes = [x['code'] for x in code_cursor]
        
        datetime_obj = datetime_obj - timedelta(days=1)
        date = datetime_obj.strftime('%Y-%m-%d')
        
    return codes


if __name__ == '__main__':
    compute_pe()
    