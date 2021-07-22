import os
import glob

def clearfiles():

    if glob.glob("data/*.txt"):
        files = glob.glob("data/*.txt")
        for f in files:
            os.remove(f)
            #print("removed ", f)

    if glob.glob("data/nbirds/*.txt"):
        files = glob.glob("data/nbirds/*.txt")
        for f in files:
            os.remove(f)
            #print("removed ", f)

def savefile(filename, data):
    f = open("data/" + filename + ".txt", "a")
    f.write(str(data) + "\n")
    f.close()

clearfiles()
