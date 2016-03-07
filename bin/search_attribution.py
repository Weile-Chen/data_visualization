# !/usr/bin/python
from pandas import DataFrame

def search_attribution(path,frame):
    i = 0
    cities = []
    provinces = []
    count = {}
    num = open(path,'r')

    for client_num in num:
        
        while frame.values[i][1] != client_num[:7]:
            i = i + 1
            
            if i > 56134:
                i=-1
                break
         
        if i != -1:
             cities.append(frame.values[i][0])
             provinces.append(frame.values[i][2])

                      
    for city in cities:
        if city in count:
            count[city] = count[city]+1
        else:
            count[city] = 1

    return count,provinces,cities
