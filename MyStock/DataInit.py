# -*- coding = utf-8 -*-
from __future__ import print_function
import tushare as ts
import pandas as pd
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def initClassified(path):
    try:
        df = ts.get_industry_classified()
        df.to_csv(path + 'industry.csv')

        df = ts.get_concept_classified()
        df.to_csv(path + 'concept.csv')

        df = ts.get_area_classified()
        df.to_csv(path + 'area.csv')

        df = ts.get_sme_classified()
        df.to_csv(path + 'sme.csv')

        df = ts.get_gem_classified()
        df.to_csv(path + 'gem.csv')

        df = ts.get_st_classified()
        df.to_csv(path + 'st.csv')

        df = ts.get_hs300s()
        df.to_csv(path + 'hs300s.csv')
     
        df = ts.get_sz50s()
        df.to_csv(path + 'sz50s.csv')
    except:
        logging.error("initClassified Error.",exc_info=True)

def initBasicInfo(path,year,M):
    try:
        df = ts.get_stock_basics()
        df.to_csv(path + 'basics.csv')

        df = ts.get_report_data(year,M)
        df.to_csv(path + 'report'+str(year)+'-'+str(M)+'.csv')

        df = ts.get_profit_data(year,M)
        df.to_csv(path + 'profit'+str(year)+'-'+str(M)+'.csv')

        df = ts.get_operation_data(year,M)
        df.to_csv(path + 'operation'+str(year)+'-'+str(M)+'.csv')

        df = ts.get_growth_data(year,M)
        df.to_csv(path + 'growth'+str(year)+'-'+str(M)+'.csv')

        df = ts.get_debtpaying_data(year,M)
        df.to_csv(path + 'debtpaying'+str(year)+'-'+str(M)+'.csv')

        df = ts.get_cashflow_data(year,M)
        df.to_csv(path + 'cashflow'+str(year)+'-'+str(M)+'.csv')
    except:
        logging.error("initBasicInfo Error.",exc_info=True)

def initHistData(path,code):
    try:
        df = ts.get_hist_data(code)
        df.to_csv(path + code + '.csv')
        ts.get_hist_data(code,ktype='W')
        df.to_csv(path + code + '-W.csv')
        ts.get_hist_data(code,ktype='M')
        df.to_csv(path + code + '-M.csv')
        ts.get_hist_data(code,ktype='5')
        df.to_csv(path + code + '-5.csv')
        ts.get_hist_data(code,ktype='15')
        df.to_csv(path + code + '-15.csv')
        ts.get_hist_data(code,ktype='30')
        df.to_csv(path + code + '-30.csv')
        ts.get_hist_data(code,ktype='60')
        df.to_csv(path + code + '-60.csv')

        #df = ts.get_tick_data(path + '000756-tick','2015-03-27')
    except:
        logging.error("initHistData Error.",exc_info=True)

def getRealTimeData(path):
    try:
        df = ts.get_realtime_quotes('000581')
        df.to_csv(path + '000581-rt.csv')
    except:
        logging.error("getRealTimeData Error.",exc_info=True)
    
if __name__ == "__main__":
    logging.basicConfig(level=4,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='D:\\stock\\DataInit.log',
                    filemode='w')
    #print("start get basic data.")
    #initClassified('d:\\stock\\classified\\')
    #initBasicInfo('d:\\stock\\basic\\',2018,2)
    #print("end get basic data.")
    print("start get history data.")
    logging.error('start get history data...')
    df = pd.read_csv('D:\\stock\\basic\\basics.csv',dtype = object)
    for item in df['code']:
        logging.error('get data:{}'.format(item))
        initHistData('D:\\stock\\his\\',item)
    logging.error('end get history data...')
    print("end get history data.")
    