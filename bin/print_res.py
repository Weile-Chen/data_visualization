import matplotlib.pyplot as plt	
import numpy as np
import numpy
from mpl_toolkits.basemap import Basemap
def print_area_bar(count_area):
	
	data = []
	for key in count_area.keys():
		data.append(count_area[key])	 

	data = np.array(data)

	ind = np.arange(8)  # the x locations for the groups
	width = 0.35       # the width of the bars
	 
	fig, ax = plt.subplots()
	ax.bar(ind, data, width, color='r')

	 
	# add some
	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('SE', 'NW', 'central', 'north', 'east', 'NE', 'others', 'south'))

	fig.savefig('./result/area_bar.png', format='png')

def print_stage_bar(count_stage):
	
	data = []
	for key in count_stage.keys():
		data.append(count_stage[key])	 

	data = np.array(data)

	ind = np.arange(5)  # the x locations for the groups
	width = 0.35       # the width of the bars
	 
	fig, ax = plt.subplots()
	ax.bar(ind, data, width, color='r')
	 
	# add some
	ax.set_xticks(ind+width)
	ax.set_xticklabels(('Stage1', 'Stage2', 'Stage3', 'Stage4', 'Stage5'))

	fig.savefig('./result/stage_bar.png', format='png')

def print_area_pie(count_area):

	data = []
	for key in count_area.keys():
		data.append(count_area[key])
	

	labels = ('south-west', 'north-west', 'central China', 'north China', 'east China', 'north-east', 'Hong Kong, Macao and Taiwan', 'south China')
	fig1 = plt.figure(num=1, figsize=(6, 6))
	plt.axes(aspect=1)
	plt.title('Pie plot of client area distribution', size=14)
	plt.pie(data,labels = labels)
	fig1.savefig('./result/area_pie.png', format='png')
	
def print_stage_pie(count_stage):
		
	data = []
	for key in count_stage.keys():
		data.append(count_stage[key])

	labels = ('Stage1', 'Stage2', 'Stage3', 'Stage4', 'Stage5')
	fig3 = plt.figure(num=2, figsize=(6, 6))
	plt.axes(aspect=1)
	plt.title('Pie plot of city\'s stage distribution', size=14)
	plt.pie(data,labels = labels)
	fig3.savefig('./result/city_stage_pie.png', format='png')

def print_heatmap(lats,lons):
	fig = plt.figure(figsize=(8,8))
	ax = fig.add_axes([0.1,0.1,0.8,0.8])

	data = np.zeros((100,150))

	i = 0
	j = 0
	for lat in lats:
		j += 1
	while i < j:
		data[int(float(lats[i]))][int(float(lons[i]))] += 1
		i += 1

	

	#draw map of china
	heat_map = Basemap(projection='stere',lon_0=115,lat_0=32.5,llcrnrlat=15,urcrnrlat=50,llcrnrlon=80,urcrnrlon=150,resolution='f')
	# draw coastlines
	heat_map.drawcoastlines()
	#draw country boundaries
	heat_map.drawcountries(color='k',linewidth=1)
	#add title
	plt.title('Heatmap of client distribution')
	#draw province
	heat_map.readshapefile("./data/map_source/CHN_adm0",'', drawbounds=True)
	heat_map.readshapefile("./data/map_source/CHN_adm1",'', drawbounds=True)

	lat = np.linspace(0,150,150)
	lon = np.linspace(0,100,100)

	x, y = numpy.meshgrid(lat, lon)

	x,y = heat_map(x,y)
		    
	heat_map.contourf(x, y, data)

	plt.savefig('./result/heatmap.png', format='png')



