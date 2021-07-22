import os
import glob

def clearfiles():

    if glob.glob("players/*.txt"):
        files = glob.glob("players/*.txt")
        for f in files:
            os.remove(f)
            #print("removed ", f)

    #if glob.glob("data/nbirds/*.txt"):
    #    files = glob.glob("data/nbirds/*.txt")
    #    for f in files:
    #        os.remove(f)
    #        #print("removed ", f)

def savefile(filename, data):
    f = open("players/" + filename + ".txt", "a")
    f.write(str(data) + "\n")
    f.close()

def checksave(filename):
    if (os.path.exists("players/" + filename + '.txt')):
        return True
    else:
        return False
    
#clearfiles()
