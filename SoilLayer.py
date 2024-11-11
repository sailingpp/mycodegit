import pandas as pd
import math
from Pile import *

class SoilLayer:
     def __init__(self,sid,layername,start,end,adjust,qsi,qua):
        self.id=sid
        self.layername=layername
        self.start=start
        self.end=end
        self.adjust=adjust
        self.qsi=qsi
        self.qua=qua
        self.length=start-end
        self.layer_qsi=qsi*self.length*adjust


     def show_message(self):
        print(f'{self.id}土,{self.layername},深度{self.length:0.3f},调整系数{self.adjust},测摩阻系数{self.qsi},端阻系数{self.qua}')


