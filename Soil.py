import pandas as pd
from SoilLayer import *


class Soil:
    dict={}
    def __init__(self,label,dic):
        self.label=label
        self.dict=dic

          
    def show_soilmessage(self):
        print(self.label)
        print(self.dict.items())





   