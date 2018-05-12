# use classes , create module , make superclasses, add machine learning 

import readFile #importing function from readFile.py
i = 0 
# used readFile.readFile() in order to organize data into an array 
dataArray = ['Arkansas Nuclear 1\n', '0\n', 'Arkansas Nuclear 2\n', '100\n', 'Beaver Valley 1\n', '55\n', 'Beaver Valley 2\n', '100\n', 'Braidwood 1\n', '92\n', 'Braidwood 2\n', '100\n', 'Browns Ferry 1\n', '100\n', 'Browns Ferry 2\n', '23\n', 'Browns Ferry 3\n', '87\n', 'Brunswick 1\n', '100\n', 'Brunswick 2\n', '100\n', 'Byron 1\n', '88\n', 'Byron 2\n', '100\n', 'Callaway\n', '100\n', 'Calvert Cliffs 1\n', '100\n', 'Calvert Cliffs 2\n', '100\n', 'Catawba 1\n', '100\n', 'Catawba 2\n', '65\n', 'Clinton\n', '0\n', 'Columbia Generating Station\n', '100\n', 'Comanche Peak 1\n', '100\n', 'Comanche Peak 2\n', '100\n', 'Cooper\n', '100\n', 'D.C. Cook 1\n', '100\n', 'D.C. Cook 2\n', '12\n', 'Davis-Besse\n', '100\n', 'Diablo Canyon 1\n', '100\n', 'Diablo Canyon 2\n', '100\n', 'Dresden 2\n', '100\n', 'Dresden 3\n', '100\n', 'Duane Arnold\n', '100\n', 'Farley 1\n', '13\n', 'Farley 2\n', '100\n', 'Fermi 2\n', '87\n', 'FitzPatrick\n', '100\n', 'Grand Gulf 1\n', '0\n', 'Harris 1\n', '30\n', 'Hatch 2\n', '95\n', 'Hope Creek 1\n', '6\n', 'Indian Point 2\n', '100\n', 'Indian Point 3\n', '100\n', 'LaSalle 1\n', '100\n', 'Oconee 1\n', '100\n', 'Oconee 2\n', '100\n', 'Oconee 3\n', '0\n',
    'Quad Cities 1\n', '87\n', 'Quad Cities 2\n', '98\n', 'Susquehanna 2\n', '85\n', 'Watts Bar 2\n', '58\n']
dataArraylen = len(dataArray)

# data in format Unit,Power
class dataElem: # using class for data length 
    def __init__(self, lenData):
        self.d = lenData

a = dataElem(dataArraylen)

while True:   # while loop to print all data 
        i+= 1
        if i == a.d:
            break
        print(dataArray[i])

# now print all even number as int to get power 

