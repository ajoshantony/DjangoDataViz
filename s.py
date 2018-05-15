from myFunctions import *
import re
newUnit = str(readUnit())
if newUnit.endswith('None'):
    newUnit = newUnit[:-4]



print(newUnit)