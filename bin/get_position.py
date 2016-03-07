#!/usr/bin/python

def get_position(cities):
    cities_list=[]
    lats = []
    lons = []
    file = open("./data/positions",'r')
    for line in file:
         city,lat,lon = line.split(",")
         cities_list.append(city)
         lats.append(lat)
         lons.append(lon[:-2])

    lat_r = []
    lon_r = [] 

    #search the positions of cities and put them in two lists
    for temp in cities:
        i = 0
        while i < len(cities_list): 	
            if temp == cities_list[i]:
                lat_r.append(lats[i])
                lon_r.append(lons[i])
                break
            i = i + 1

    return lat_r,lon_r
