def fileWR(filename,text):
    f = open(filename, "wt")
    f.write(text)
    f.close()

def fileWRofPrint(filename,text):
    f = open(filename, "wt")
    print(text,file=f)
    f.close()

def fileWRofA(filename,text):
    f = open(filename, "at")
    f.write(text)
    f.close()

def fileWRwith(filename,text):
    with open(filename, "wt") as fileWr:
        fileWr.write(text)

if __name__ == '__main__':
    string="Був запущений, як програма файл fileWork.py"
    fileWR('../info.txt', string)
    # print("Був запущений, як програма файл fileWork.py",file=f)
