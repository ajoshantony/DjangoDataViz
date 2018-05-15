'''
This File is for converting data into usable format

'''


from myFunctions import * #importing functions from myFunctions.py

# testing write functionality
## myFunctions.writeFile()
#Step 1 - use myFunctions.readFile() in order to organize data into an array and print that

i = 1 

intData = ['Arkansas Nuclear 1\n', '0\n', 'Arkansas Nuclear 2\n', '100\n', 'Beaver Valley 1\n', '55\n', 'Beaver Valley 2\n', '100\n', 'Braidwood 1\n', '92\n', 'Braidwood 2\n', '100\n', 'Browns Ferry 1\n', '100\n', 'Browns Ferry 2\n', '23\n', 'Browns Ferry 3\n', '87\n', 'Brunswick 1\n', '100\n', 'Brunswick 2\n', '100\n', 'Byron 1\n', '88\n', 'Byron 2\n', '100\n', 'Callaway\n', '100\n', 'Calvert Cliffs 1\n', '100\n', 'Calvert Cliffs 2\n', '100\n', 'Catawba 1\n', '100\n', 'Catawba 2\n', '65\n', 'Clinton\n', '0\n', 'Columbia Generating Station\n', '100\n', 'Comanche Peak 1\n', '100\n', 'Comanche Peak 2\n', '100\n', 'Cooper\n', '100\n', 'D.C. Cook 1\n', '100\n', 'D.C. Cook 2\n', '12\n', 'Davis-Besse\n', '100\n', 'Diablo Canyon 1\n', '100\n', 'Diablo Canyon 2\n', '100\n', 'Dresden 2\n', '100\n', 'Dresden 3\n', '100\n', 'Duane Arnold\n', '100\n', 'Farley 1\n', '13\n', 'Farley 2\n', '100\n', 'Fermi 2\n', '87\n', 'FitzPatrick\n', '100\n', 'Grand Gulf 1\n', '0\n', 'Harris 1\n', '30\n', 'Hatch 2\n', '95\n', 'Hope Creek 1\n', '6\n', 'Indian Point 2\n', '100\n', 'Indian Point 3\n', '100\n', 'LaSalle 1\n', '100\n', 'Oconee 1\n', '100\n', 'Oconee 2\n', '100\n', 'Oconee 3\n', '0\n',
    'Quad Cities 1\n', '87\n', 'Quad Cities 2\n', '98\n', 'Susquehanna 2\n', '85\n', 'Watts Bar 2\n', '58\n']

dataArraylen = len(intData)

# data in format Unit,Power
class dataElem: # using class for data length 
    def __init__(self, lenData):
        self.d = lenData

a = dataElem(len(intData))

# while True:   # while loop to print all data 
#         print(dataArray[i])
#         i+= 1
#         if i == a.d:
#             break
# Step 2 - use write function to print all even numbers as int into organized.txt
"""
while True:   # while loop to print either the powerplant name or power level
        i+= 2
        print(i)
        if i == a.d+1:
            break
        else:
            print(intData[i])  #modified myFunctions.py 
"""
#myFunctions.readUnit()

# myFunctions.readPower()

def PowerDataOutput():
    i = 1
    while True:   # while loop to print all data 
            i+= 2
            #print(i)
            if i == a.d+1:
                break
            else:
                print(intData[i])

writePower()  #look at myFunctions

# ouput from myFunctions.readPower()
powerData = ['0\n', '100\n', '55\n', '100\n', '92\n', '100\n', '100\n', '23\n', '87\n', '100\n', '100\n', '88\n', '100\n', '100\n', '100\n', '100\n', '100\n',
'65\n', '0\n', '100\n', '100\n', '100\n', '100\n', '100\n', '12\n', '100\n', '100\n', '100\n', '100\n', '100\n', '100\n', '13\n', '100\n', '87\n',
'100\n', '0\n', '30\n', '95\n', '6\n', '100\n', '100\n', '100\n', '100\n', '100\n', '0\n', '87\n', '98\n', '85\n', '58']

powerData = list(map(int, powerData)) # makes str in list into into using map function


print(powerData)  


"""
SaveOutput = list(map(int, SaveOutput)) # makes str in list into into using map function

print(SaveOutput)

"""