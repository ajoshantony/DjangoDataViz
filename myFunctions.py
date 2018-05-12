def writeFile():
    txt = open("organizedData.txt","w") 
    txt.write("Hello World") 
    txt.close() 

def readFile():
    txt = open("data.txt", "r")  # using open function to open  data file and "r" which reads
    print(txt.readlines() )       # 2,4,6,8,10,12 need to print power values only 



