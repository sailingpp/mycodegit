import pandas as pd
import math
from Pile import *
from SoilLayer import *


class Soil:
    dict={}
    pile=Pile(0.8)
    def __init__(self,label,dic):
        self.label=label
        self.dict=dic
          
    def show_message(self):
        print(self.label)




   