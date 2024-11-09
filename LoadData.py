from Pile import *
from Soil import *
import json
import os
import pandas as pd

#不好用废弃
def myfun():
    mylist=[]
    json_file_path = r'C:\Users\17653\mycodegit\mycodegit\Soildata.json'

    with open(json_file_path, 'r',encoding='utf-8') as mydata:
                mydic=json.load(mydata)

    for i in mydic.values():
                for j in range(5):
                    k=Soil(mydic(i),list(i[j].values())[0],list(i[j].values())[1],list(i[j].values())[2],list(i[j].values())[3],list(i[j].values())[4],list(i[j].values())[5],list(i[j].values())[6])
                    mylist.append(k)
    return mylist  

