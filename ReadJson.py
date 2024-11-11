import json
import pandas as pd
import io

#注意路径

data=pd.read_json('./mycodegit/Soildata.json') 
df=pd.DataFrame(data)
#输出df
print(df)
#输出df的行列
print(df.shape)
#输出具体
print(df['kc1'][0]['start'])
print(df['kc1'][0])
print(df['kc1'][0].keys())

print(df['kc1'][0].values())