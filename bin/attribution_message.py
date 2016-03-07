#!/usr/bin/python
#_*_ coding:utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
def get_message(provinces,cities):
    count_area = {"east China":0,"south China":0,"central China":0,"north China":0,"north-east":0,"south-west":0,"north-west":0,"Hong Kong, Macao and Taiwan":0}
    count_stage = {"Stage1":0,"Stage2":0,"Stage3":0,"Stage4":0,"Stage5":0}
    
    area_index = {0:"east China",1:"south China",2:"central China",3:"north China",4:"north-east",5:"south-west",6:"north-west",7:"Hong Kong, Macao and Taiwan"}
    stage_index = {0:"Stage1",1:"Stage2",2:"Stage3",3:"Stage4",4:"Stage5"}

    temp = []

    #read imformation about area,save in area_num
    area_file = open("./data/cities_area",'r')   
    area = []

    for line in area_file:
        temp = line.split(" ")
        temp[-1] = temp[-1][:-2]
        area.append(temp)

    #read imformation about city's stage,save in stage_num
    stage_file = open("./data/stage",'r')
    stage = []

    for line in stage_file:
        temp = line.split(" ")
        temp[-1] = temp[-1][:-2]
        stage.append(temp)


    #count the amount of cities' number in differnt area
    for province in provinces:
        i = 0
        while i < 8:
            j = 0
            while j < len(area[i]):
	        is_match = (province == area[i][j])
                if is_match:
                    count_area[area_index[i]] = count_area[area_index[i]] + 1
                    break
	        else:
                    j = j + 1

            if is_match:
                break
            else:
                i = i + 1

	

    i = 0
    j = 0

    #count the amount of cities' number in differnt area
    for city in cities:
        i = 0
        while i < 5:
            j = 0

            while j < len(stage[i]):
	        is_match = (city == stage[i][j])
                if is_match:
                    count_stage[stage_index[i]] = count_stage[stage_index[i]] + 1
                    break
	        else:
                    j = j + 1

            if is_match:
                break
            else:
                i = i + 1

	data = []
	labels = []
	for key in count_area.keys():
		data.append(count_area[key])
	

	plt.figure()
	plt.axes()
	plt.title('Pie plot of client area distribution', size=14)
	plt.pie(data,labels = ('south-west', 'north-west', 'central China', 'north China', 'east China', 'north-east', 'Hong Kong, Macao and Taiwan', 'south China'))
	plt.savefig('./result/client_area.png', format='png')

	data = []
	labels = []
	for key in count_stage.keys():
		data.append(count_stage[key])

	plt.figure()
	plt.axes()
	plt.title('Pie plot of client citystage distribution', size=14)
	plt.pie(data,labels = ('Stage1', 'Stage2', 'Stage3', 'Stage4', 'Stage5'))
	plt.savefig('./result/client_city_stage.png', format='png')


