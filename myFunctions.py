'''
Functions used for convert.py

'''

def readFile():
    i = 2
    txt = open("data.txt", "r")  # using open function to open  data file and "r" which reads
    while True:
        print(txt.readlines(i))
        i+=2                        # 2,4,6,8,10,12 need to print power values only 
        if i == 98:
            break

def readUnit():
    txt = open("organizedDataUnit.txt", "r")   # reads txt file and prints all data as an array
    print(txt.readlines())
      
def readPower():
    txt = open("organizedDataPower.txt", "r")  # same as above but the label data
    print(txt.readlines())
      
def writePower():
    txt = open("blank.txt","w") 
    a = str(readPower())       # this function takes output from readPower() and puts into blank txt file for storage so I can convert to an int array
    txt.write(a) 
    txt.close() 