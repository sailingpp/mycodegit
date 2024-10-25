import pandas as pd
import math
from Soil import *
from Pile import *
from LoadData import *


pile=Pile(0.8)
pile.show_message()
list_soil=myfun()
for i in list_soil:
    print(i.Fqsi*pile.cir)




        

        
        




