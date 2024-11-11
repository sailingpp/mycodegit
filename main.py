import pandas as pd
import math
from Pile import *
from SoilLayer import *
from Soil import *
      
data=pd.read_json('./mycodegit/Soildata.json') 
df=pd.DataFrame(data)

layer_dic={}
layer_list=[]
print(df.columns)
for index in df.columns:
    for i in df[index]:
        layer_list.append(SoilLayer(i['sid'],i['layer_name'],i['start'],i['end'],i['adjust'],i['qsi'],i['qua']))
    layer_dic[index]=layer_list

print(layer_dic)

print(type(layer_dic))

soildf=pd.DataFrame(layer_dic)



soil=Soil('kc1',layer_dic['kc1'])

for i in soil.dict:
    print(i.show_message())