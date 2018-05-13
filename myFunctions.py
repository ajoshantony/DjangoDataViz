def writeFile():
    txt = open("organizedData.txt","w") 
    txt.write("Hello World") 
    txt.close() 


def readFile():
    i = 2
    txt = open("data.txt", "r")  # using open function to open  data file and "r" which reads
    while True:
        print(txt.readlines(i))
        i+=2                        # 2,4,6,8,10,12 need to print power values only 
        if i == 98:
            break


def readUnit():
    txt = open("organizedDataUnit.txt", "r") 
    print(txt.readlines())
      

def readPower():
    txt = open("organizedDataPower.txt", "r") 
    print(txt.readlines())
      
