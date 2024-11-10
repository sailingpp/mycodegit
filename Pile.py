import pandas as pd
import math


class Pile:
    def __init__(self,diameter):
       self.diameter=diameter
       self.cir=math.pi*diameter
       self.area=math.pi*diameter*diameter/4

    def show_message(self):
        print(f"桩的直径为：{self.diameter:0.3f},桩的半径为：{self.cir:0.3f},桩的面积为：{self.area:0.3f}")
    
    

