import pandas as pd
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


     def show_message(self,diameter):
        pile=Pile(diameter)
        print(f'{self.id}土,{self.layername},深度{self.length:0.3f},调整系数{self.adjust},侧摩阻系数{self.qsi},侧摩阻力{pile.cir*self.layer_qsi:0.3f},端阻系数{self.qua},端阻力{pile.area*self.qua:0.3f}')

     def get_fqsi(self,diameter):
         pile=Pile(diameter)
         fqsi=pile.cir*self.layer_qsi
         return fqsi

