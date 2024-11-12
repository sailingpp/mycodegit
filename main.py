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
data=pd.read_json('./mycodegit/Soildata.json') 
df=pd.DataFrame(data)
#将读入json给soill类
#new一个空字典
layer_dic={}
for index in df.columns:
    layer_list=[] #new一个list，放在这里重要性 第二次就重新建立new
    for i in df[index]:
        layer_list.append(SoilLayer(i['sid'],i['layer_name'],i['start'],i['end'],i['adjust'],i['qsi'],i['qua']))
    layer_dic[index]=layer_list
#
print(layer_dic)

soildf=pd.DataFrame(layer_dic)

soil1=Soil('kc1',layer_dic['kc1'])

for i in soil1.dict:
    print(i.show_message(0.8))

soil2=Soil('kc2',layer_dic['kc2'])

for i in soil2.dict:
    print(i.show_message(0.8))