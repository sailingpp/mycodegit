import pandas as pd
import math


class Pile:
    def __init__(self,diameter):
       self.diameter=diameter
       self.cir=math.pi*diameter
       self.area=math.pi*diameter*diameter/4

    def showmessage(self):
        print(f"桩的直径为：{self.diameter:0.3f},桩的半径为：{self.cir:0.3f},桩的面积为：{self.area:0.3f}")
    

if __name__=='main':
    pile=Pile(0.8)
    pile.showmessage()

