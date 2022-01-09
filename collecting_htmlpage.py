# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 01:07:01 2022

@author: Ephron
"""

import os
import time
import requests
import sys


def retreive_html():
    for year in range(2016,2022):
        for month in range(1,13):
            if month<10:
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month, year)
            else:
                url=  'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month, year)
            
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')

            if not os.path.exists('Data/Html_data/{}'.format(year)):
                os.makedirs('Data/Html_data/{}'.format(year))
            with open("Data/Html_data/{}/{}.html".format(year, month),"wb") as output:
                output.write(text_utf)

                sys.stdout.flush()
        
if __name__=='__main__':
    start_time = time.time()
    retreive_html()
    end_time = time.time()
    print(f"Time Taken >> {end_time-start_time}")