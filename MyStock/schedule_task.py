# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:28:23 2018

@author: he
"""

#shudule_task.py
'''
每天下午（周一到周五）15:30执行抓取
'''

def crawl_daily():
    dc = DaillyCrawler()
    now_date = datetime.now()
    weekday = now_date.strftime('%w')
    if 0 < weekday < 6:
        now = now_date.strftime('%Y-%m-%d')
        dc.crawl_index(begin_date = now, end_date = now)
        dc.crawl(begin_date = now, end_date = now)
        

if __name__ == '__main__':
    schedule.every().day.at("15:30").do(crawl_daily)
    while True:
        schedule.run_pending()
        time.sleep(10)
        