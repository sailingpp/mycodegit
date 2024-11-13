import pandas as pd
import math
from Pile import *
from SoilLayer import *
from Soil import *

#输出显示完整性    
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)
pd.set_option('display.expand_frame_repr',False)

#读入json
soil_data=pd.read_json('./mycodegit/Soildata.json') 
df=pd.DataFrame(soil_data)
#将读入json给soill类
#new一个空字典
layer_dic={}
for index in df.columns:
    layer_list=[] #new一个list，放在这里重要性 第二次就重新建立new
    for i in df[index]:
        layer_list.append(SoilLayer(i['sid'],i['layer_name'],i['start'],i['end'],i['adjust'],i['qsi'],i['qua']))
    layer_dic[index]=layer_list

print(layer_dic.keys())

#根据字典创建一个dataframe ，暂时不用
soildf=pd.DataFrame(layer_dic)
#print(soildf)
#soildf.to_excel('./mycodegit/soil.xlsx')

soil=[]
for k in layer_dic.keys():
    soil.append(Soil(k,layer_dic[k]))

for item in soil:
    print(item.show_soilmessage(0.6))

print('20241113')



