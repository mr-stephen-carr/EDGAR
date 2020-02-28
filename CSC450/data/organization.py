'''
Alyssa Slayton 2020

This is going to be a bit of a bigger commitment than I originally anticipated...

Initial format of data:
Only including relavent paths
will delete anything not included in this tree to conserve space

C:\\Users\\alyss\\Documents\\EDGAR\\CSC450\\data\\big-boy\\IEMOCAP_full_release\\
    SessionX (1-5)
        dialog
            EmoEvaluation
                Categorical
                    .anvil files and .txt files for each session
                    I DELETED THE .anvil FILES BEFOREHAND
                    on cmd travel to directory and type:
                        del *.anvil
        sentences
            wav
                bunch of directories
                    each one containss a bunch of data

each .txt file corresponds to one subdirectory in sentences\\wav\\

TREE NEEDS TO BE STRUCTURED LIKE THIS FOR THE PROGRAM TO WORK
'''
'''
Final format of data tree:

C:\\Users\\alyss\\Documents\\EDGAR\\CSC450\\data\\IEMOCAP\\
    angry
    fearful
    happy
    neutral
    sad

IEMOCAP has more than this, I only keep the ones we're using.
'''
from os import walk, remove, listdir


class travelFolders:
    def __init__(self, root):
        self.root = root

    def getSessions(self):
        contents = listdir(self.root)
        sessions = []
        for i in contents:
            if i[0] == 'S':     # just checking if the item is a session name
                sessions.append(self.root + i)
        return(sessions)

    def getSubsessions(self, session):
        contents = listdir(session + "\\sentences\\wav")
        subsessions = []
        for i in contents:
            subsessions.append(session + "\\sentences\\wav\\" + i)
        return(subsessions)

    def getWavs(self, subsession):
        return(listdir(subsession))

    def getGuideFilesList(self, session):
        temp = listdir(session + "\\dialog\\EmoEvaluation\\Categorical\\")
        for i in range(len(temp)):
            temp[i] = session + "\\dialog\\EmoEvaluation\\Categorical\\" + temp[i]
        return(temp)

class classify:
    def __init__(self, sessions):
        self.sessions = sessions

def main():
    initRoot = "C:\\Users\\alyss\\Documents\\EDGAR\\CSC450\\data\\big-boy\\IEMOCAP_full_release\\"
    finalRoot = "C:\\Users\\alyss\\Documents\\EDGAR\\CSC450\\data\\IEMOCAP\\"

    traversal = travelFolders(initRoot)
    sessions = traversal.getSessions()
    for session in sessions:
        subsessions = traversal.getSubsessions(session)
        contentFiles = traversal.getGuideFilesList(session)
        for i in range(len(subsessions)):
            wavs = traversal.getWavs(subsessions[i])
            file1 = contentFiles[i*3]
            file2 = contentFiles[i*3+1]
            file3 = contentFiles[i*3+2]

            print(file1, " ", file2, " ", file3)
        
    wavs = traversal.getWavs(subsessions[0])

    
    print("traveling")

if __name__ == '__main__':
    main()