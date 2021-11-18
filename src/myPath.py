import path, os, shutil

class MyPath(object):
    def __init__(self, argv):
        self.dirRoot = os.path.abspath(argv)
        self.dirOut = os.path.abspath(self.dirRoot + '/out')
        self.dirDemo = os.path.abspath(self.dirRoot + '/demo')
        self.dirDemoCsv = os.path.abspath(self.dirDemo + '/csv')
        self.csvDemoName = 'test.csv'
        self.creatFolder()
        self.copyCsvFile()
        
    def copyCsvFile(self):
        csvDemoPath = os.path.join(self.dirDemoCsv, self.csvDemoName)
        if os.path.isfile(csvDemoPath):
            shutil.copyfile(csvDemoPath, self.dirDemo + '/test.csv')
        else:
            print('csvFile dees not exit!')
    
    
    def creatFolder(self):
        self.mkdirOut()
        self.mkdirDemo()
        self.mkdirDemoCsv()
        
    def mkdirOut(self):
        if (os.path.exists(self.dirOut)):
            pass
        else:
            os.mkdir(self.dirOut)
            
    def mkdirDemo(self):
        if (os.path.exists(self.dirDemo)):
            pass
        else:
            os.mkdir(self.dirDemo)
            
    def mkdirDemoCsv(self):
        if (os.path.exists(self.dirDemoCsv)):
            pass
        else:
            os.mkdir(self.dirDemoCsv)
    
    def getCsvFileName(self):
        return 'test.csv'
        
myPath = MyPath('../.')

if __name__ == '__main__':
    # initial class object by __init__ func
#     myPath = MyPath('../.')
    print(myPath.dirRoot)
    print(myPath.dirOut)
    print(myPath.dirDemoCsv)
    print(myPath.getCsvFileName())
    print(os.path.join(myPath.dirOut, myPath.getCsvFileName()))
    print('This is a test message')