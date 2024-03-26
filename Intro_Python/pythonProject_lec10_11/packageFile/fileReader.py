def fileReadByRead(filename):
    with open(filename,'rt') as fileRead:
        return fileRead.read()

def fileReadByWhileNumberSymbol(filename, numberSymbol):
    with open(filename,'rt') as f:
        string=''
        while True:
            fragment=f.read(numberSymbol)
            if not fragment:
                break
            string+=fragment
    return string

def fileReadlnByWhile(filename):
    text=''
    with open(filename, 'rt') as f:
        while True:
            line=f.readline()
            if not line:
                break
            text+=line
        for line in f:
            text+=line
    return text

def fileReadByLine(filename):
    text=''
    with open(filename, 'rt') as f:
        for line in f:
            text+=line
    return text

