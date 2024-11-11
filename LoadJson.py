from Pile import *
from Soil import *
import json
import pandas as pd





mydic_soil={}

def data_process():
    json_file_path = r'C:\Users\17653\mycodegit\mycodegit\Soildata.json'

    with open(json_file_path, 'r',encoding='utf-8') as mydata:
        mydic=json.load(mydata)
        df=pd.DataFrame(mydic)


    for i in df.columns:#获取kc
        for j in df[i]:
            mydic_soil[i]=Soil(i,j['sid'],j['layer_name'],j['start'],j['end'],j['adjust'],j['qsi'],j['qua'])
           
            
    return mydic_soil

    
