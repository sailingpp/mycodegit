import pandas as pd
import math
from Pile import *

class Soil:
    diameter=None
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
        self.Fqsi=qsi*self.length*adjust
        

    def show_message(self):
        print(f'{self.label}孔,{self.id}土,{self.layername},深度{self.length:0.3f},调整系数{self.adjust},测摩阻系数{self.qsi},端阻系数{self.qua}')

    def get_pile(self,diameter):
        pile =Pile(diameter)
        return pile.cir*self.Fqsi

        
        
    


