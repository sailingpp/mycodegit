from Ra import *
from Pile import *
from Soil import *
import json
import os
import pandas as pd

ra=Ra()

json_file_path = r'C:\Users\17653\mycodegit\mycodegit\Soildata.json'
 
with open(json_file_path, 'r',encoding='utf-8') as mydata:
    mydic=json.load(mydata)

#print(mydic)
#for k, v in mydic:
#k=Soil(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7])
#print(mydic['kc1'][0]['sid'])

#print(mydic.keys())
for i in mydic.values():
    print(i)

for k,v in mydic.items():
    print(k)