# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:55:45 2018

@author: he
"""

from pymongo import ASCENDING
import pandas as pd
import matplotlib.pyplot as plt
from database import DB_CONN
from stock_util import get_grading_dates

daily = DB_CONN['daily']
daily_hfq = DB_CONN['daily_hfq']

def stock_pool(begin_date, end_date):
    adjust_date_codes_dict = dict()
    
    all_dates = get_trading_dates(begin_date = begin_date, end_date = end_date)
    
    last_phase_codes = []
    adjust_interval = 7
    all_adjust_dates = []
    
    for _index in range(0, len(all_dates), adjust_interval):
        adjust_date = all_dates[_index]
        all_adjust_dates.append(adjust_date)
        print('adjust date: %s' % adjust_date, flush = True)
        
        daily_cursor = daily.find(
                {'date': adjust_date, 'pe': {'$lt': 30, '$gt': 0},
                 'is_trading': True},
                 sort = [('pe', ASCENDING)],
                 projection = {'code': True},
                 limit = 100)
        
        codes = [x['code'] for x in daily_cursor]
        
        this_phase_codes = []
        if len(last_phase_codes) > 0:
            suspension_cursor = daily.find(
                    {'code': {'$in': last_phase_codes}, 'date': adjust_date, 'is_trading': False},
                    projection = {'code': True})
            
            suspension_codes = [x['code'] for x in suspension_cursor]
            this_phase_codes = suspension_codes
            
        print('上期停牌:', flush = True)
        print(this_phase_codes, flush = True)
        
        this_phase_codes = codes[0: 100 - len(this_phase_codes)]
        last_phase_codes = this_phase_codes
        
        adjust_date_codes_dict[adjust_date] = this_phase_codes
        print('最终出票：', flush = True)
        print(this_phase_codes, flush = True)
        
    return all_adjust_dates, adjust_date_codes_dict

#def find_out_stocks(last_phase_codes, this_phase_codes):
    
    