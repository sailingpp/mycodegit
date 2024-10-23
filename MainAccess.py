from Ra import *
from Pile import *
import json
import os

ra=Ra()

json_file_path = r'C:\Users\17653\mycodegit\mycodegit\Soildata.json'
 
with open(json_file_path, 'r',encoding='utf-8') as mydata:
    mydic=json.load(mydata)

print(mydic)