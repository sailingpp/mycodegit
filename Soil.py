import pandas as pd
import math

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

        
    


