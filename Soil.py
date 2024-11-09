import pandas as pd
import math
import json

class Soil:
    def __init__(self,label,sid,layername,start,end,adjust,qsi,qua):
        self.label=label
        self.layername=layername
        self.id=sid
        self.start=start
        self.end=end
        self.adjust=adjust
        self.qsi=qsi
        self.qua=qua
        self.length=start-end
        self.Fqsi=qsi*self.length
        

    def show_message(self):
        print(f'{self.label}孔,第{self.id}层土,{self.layername},深度{self.length},调整系数{self.adjust},测摩阻系数{self.qsi},端阻系数{self.qua}')

        
    


