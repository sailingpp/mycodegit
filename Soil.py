import pandas as pd
from SoilLayer import *


class Soil:
    dict={}
    sum=0
    def __init__(self,label,dic):
        self.label=label
        self.dict=dic

    def get_sumfqsi(self,dimater):
        for i in self.dict:
            self.sum=self.sum+i.get_fqsi(dimater)
        return self.sum

    def show_soilmessage(self,diameter):
        print(self.label)
        print(f'桩直径：{diameter:0.3f}')
        for i in self.dict:
            print(i.show_message(diameter))
        print(f'总的侧阻力：{self.get_sumfqsi(diameter):0.3f}KN')



   