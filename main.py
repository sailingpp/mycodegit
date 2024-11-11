import pandas as pd
import math
from Pile import *
from SoilLayer import *
from Soil import *
      
data=pd.read_json('./mycodegit/Soildata.json') 
df=pd.DataFrame(data)

layer_dic={}

print(df.columns)
for index in df.columns:
    for i in df[index]:
        layer_dic[index]=SoilLayer(i['sid'],i['layer_name'],i['start'],i['end'],i['adjust'],i['qsi'],i['qua'])

print(layer_dic)
print(type(layer_dic))

soil=Soil('kc1',layer_dic['kc1'])

print(soil.dict)
