import pandas as pd
import math
from Soil import *
from Pile import *
from LoadJson import *

#废弃
pile=Pile(0.8)
pile.show_message()
mydic_soil=data_process()
print(type(mydic_soil))
print(mydic_soil.keys())
for item in mydic_soil.keys():
    print(mydic_soil[item].show_message())















        

        
        




