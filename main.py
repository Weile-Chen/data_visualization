#!/usr/bin/python
#_*_ coding:utf-8 _*_
import pandas as pd
from pandas import DataFrame
import time

from bin.search_attribution import *
from bin.get_num_attribution import *
from bin.get_position import *
from bin.attribution_message import *
from bin.get_message import *
from bin.print_res import *


	
run_time = time.time()

count,provinces,cities = search_attribution("./data/test",get_num_attribution("./data/attributions"))
lats,lons = get_position(cities)

count_area,count_stage = get_message(provinces,cities)

print_stage_pie(count_stage)
print_area_pie(count_area)

print_area_bar(count_area)
print_stage_bar(count_stage)

print_heatmap(lats,lons)

run_time = time.time() - run_time

print "\n"
print "\n"
print "\n"
print "Costed",run_time,"s"

