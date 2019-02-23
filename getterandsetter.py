class laptop(object):
    def __init__(self):
        self._version=2018

    def getversion(self):
        print(self._version)

    def setversion(self,version):
        self._version = version


obj = laptop()
obj.getversion()
obj.setversion(2019)
obj.getversion()
print(obj._version)

