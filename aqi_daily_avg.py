# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 01:42:09 2022

@author: Ephron
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_date_2016():
    temp_i = 0
    average=[]
    for rows in pd.read_csv('Data/AQI/newaqi2016.csv', chunksize=24):
        add_var = 0
        avg=0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg= add_var/24
        temp_i=temp_i + 1
        
        average.append(avg)
    return average
                
    
def avg_date_2017():
    temp_i = 0
    average=[]
    for rows in pd.read_csv('Data/AQI/newaqi2017.csv', chunksize=24):
        add_var = 0
        avg=0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg= add_var/24
        temp_i=temp_i + 1
        
        average.append(avg)
    return average
                
def avg_date_2018():
    temp_i = 0
    average=[]
    for rows in pd.read_csv('Data/AQI/newaqi2018.csv', chunksize=24):
        add_var = 0
        avg=0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg= add_var/24
        temp_i=temp_i + 1
        
        average.append(avg)
    return average
                
    
def avg_date_2019():
    temp_i = 0
    average=[]
    for rows in pd.read_csv('Data/AQI/newaqi2019.csv', chunksize=24):
        add_var = 0
        avg=0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg= add_var/24
        temp_i=temp_i + 1
        
        average.append(avg)
    return average
       
def avg_date_2020():
    temp_i = 0
    average=[]
    for rows in pd.read_csv('Data/AQI/newaqi2020.csv', chunksize=24):
        add_var = 0
        avg=0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg= add_var/24
        temp_i=temp_i + 1
        
        average.append(avg)
    return average
    
def avg_date_2021():
    temp_i = 0
    average=[]
    for rows in pd.read_csv('Data/AQI/newaqi2021.csv', chunksize=24):
        add_var = 0
        avg=0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg= add_var/24
        temp_i=temp_i + 1
        
        average.append(avg)
    return average
    
        
if __name__ == '__main__':
    lst2016 = avg_date_2016()
    lst2017 = avg_date_2017()
    lst2018 = avg_date_2018()
    lst2019 = avg_date_2019()
    lst2020 = avg_date_2020()
    lst2021 = avg_date_2021()
    
    
    print("done")