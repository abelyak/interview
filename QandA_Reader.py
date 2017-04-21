import os

def myQSort(x):
    x = os.path.basename(x)
    pos = x.find('q')
    return int(x[:pos])

def myASort(x):
    x = os.path.basename(x)
    pos = x.find('a')
    return int(x[:pos])

class qareader:
    def __init__(self, path):
        contents = os.listdir(path)  # contents of the current directory
        self.q = []
        self.a = []
        for fname in contents:
            if fname.find('q') > 0:
                self.q.append(path + "/" + fname)
            else:
                self.a.append(path + "/" + fname)

        self.q = sorted(self.q, key=myQSort)
        self.a = sorted(self.a, key=myASort)

    def getQ(self):
        return self.q

    def getA(self):
        return self.a
