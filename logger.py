import datetime

def writeLine(file,line):
    date = datetime.datetime.now() 
    file.write(str(date) + "  " +line)
