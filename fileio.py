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

def clearfile(filename):
    if glob.glob("players/" + filename + ".txt"):
        os.remove("players/" + filename + ".txt")
    f = open("players/tracklist.txt", "r")
    dataLines = f.read()
    dataList = dataLines.splitlines()
    dataList.remove(filename)
    f.close()

    f = open("players/tracklist.txt", "w")
    for line in dataList:
        f.write(str(line) + "\n")
    f.close()


def savefile(filename, data):
    f = open("players/" + filename + ".txt", "a")
    f.write(str(data) + "\n")
    f.close()

    f = open("players/tracklist.txt", "a")
    f.write(str(filename) + "\n")
    f.close()

def savefile2(filename, eventid, alist, blist, victimName):
    f = open("players/" + filename + ".txt", "a")
    f.write(str(eventid) + "\n")
    f.write(str(victimName) + "\n")
    f.write(str(alist) + "\n")
    f.write(str(blist) + "\n")
    f.close()

def checksave(filename):
    if (os.path.exists("players/" + filename + '.txt')):
        return True
    else:
        return False

def getlastline(filename, lastlinetoretrieve):
    f = open("players/" + filename + ".txt", "r")
    dataLines = f.read()
    dataList = dataLines.splitlines()
    f.close()
    return(dataList[-lastlinetoretrieve])

def getlastevent(filename):
    f = open("players/" + filename + ".txt", "r")
    dataLines = f.read()
    dataList = dataLines.splitlines()
    f.close()
    return(dataList[-4])

def getPlayerId(filename):
    f = open("players/" + filename + ".txt", "r")
    dataLines = f.read()
    dataList = dataLines.splitlines()
    f.close()
    return(dataList[0])

def getListOfTrack():
    f = open("players/tracklist.txt", "r")
    dataLines = f.read()
    dataList = dataLines.splitlines()
    f.close()
    return(dataList)

#clearfiles()
#print(getlastline('Mushii', 2))
#print(getlastline('Mushii', 1))
