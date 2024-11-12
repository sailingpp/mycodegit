import pandas as pd
import math
from Pile import *
from SoilLayer import *
from Soil import *
      
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)
pd.set_option('display.expand_frame_repr',False)
data=pd.read_json('./mycodegit/Soildata.json') 


df=pd.DataFrame(data)

layer_dic={}

print(df.columns)
for index in df.columns:
    layer_list=[]
    for i in df[index]:
        layer_list.append(SoilLayer(i['sid'],i['layer_name'],i['start'],i['end'],i['adjust'],i['qsi'],i['qua']))
    layer_dic[index]=layer_list

print(layer_dic)

print('----')

soildf=pd.DataFrame(layer_dic)

print(soildf)

soil1=Soil('kc1',layer_dic['kc1'])


for i in soil1.dict:
    print(i.show_message(0.8))

soil2=Soil('kc2',layer_dic['kc2'])

for i in soil2.dict:
    print(i.show_message(0.8))