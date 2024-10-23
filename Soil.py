import pandas as pd
import math
import json

class Soil:
    def __init__(self,layername,sid,startheight,endheight,adjust,qsi,qua):
        self.layername=layername
        self.id=sid
        self.start_height=startheight
        self.end_height=endheight
        self.adjust=adjust
        self.qsi=qsi
        self.qua=qua
        self.length=startheight-endheight

    def showmessage(self):
        print(f'该孔第{self.id}层土,{self.layername},深度{self.length},调整系数{self.adjust},测摩阻系数{self.qsi},端阻系数{self.qua}')

        
if __name__=='main':
    k1=Soil('粘土','1',20.5,20,1,20,200)
    k1.showmessage()

    


