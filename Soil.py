import pandas as pd
import math
import json

class Soil:
    def __init__(self,sid,layername,startheight,endheight,adjust,qsi,qua):
        self.layername=layername
        self.id=sid
        self.start_height=startheight
        self.end_height=endheight
        self.adjust=adjust
        self.qsi=qsi
        self.qua=qua
        self.length=startheight-endheight
        self.Fqsi=qsi*self.length
        

    def show_message(self):
        print(f'该孔第{self.id}层土,{self.layername},深度{self.length},调整系数{self.adjust},测摩阻系数{self.qsi},端阻系数{self.qua}')

        
    


