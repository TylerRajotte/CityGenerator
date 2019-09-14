class FileReader:
    def __init__(self, filelocation, action):
        self.filelocation = filelocation
        self.fileOutput = []

        if action == "read":
            self.__readfile()
        else:
            print("Unknown Action, you can \"read\"")

    def __readfile(self):
        file = open(self.filelocation, "r")
        self.fileOutput = file.read().split("\n")
        file.close()
