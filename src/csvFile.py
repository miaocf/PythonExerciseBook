# This scripy is for csv file practice.
# Author: miaochaofeng
# Time:   2021-11-11

import argparse, os, time, sys

class csvFile(object):
    def __init__(self, args):
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--test", action = "store", type = str, help = "This is a help message")
        parser.add_argument("-s", "--sourceFile", action = "store", type = str, default = os.path.abspath("../demo/test.csv"), 
                            help = "Specify the demo csv file path.")
        parser.add_argument("-d", "--destination", action = "store", type = str, default = os.path.abspath("../demo/result"), 
                            help = "Specify the result path")
        args = parser.parse_args()
        print(args)
        print('HELLO')
        self.sourceFile = args.sourceFile
        self.destination = args.destination
        self.test = args.test
#         print(args.test)
#         print(args.sourceFile)
        
    def run(self):
        print("run test!")
        print(self.test)
    
    def main(self):
        print('This is main function')
    
if __name__ == '__main__':
    start_time = time.time()
    cmdList ='F:\code\Python\ExerciseBook\src\csvFile.py -t miaochaofeng'
    sys.args = cmdList.split(' ')
    print(sys.args)
    demo = csvFile(sys.args)
    demo.run()
    # os.system(cmdList)
#     demo = csvFile('-t miaochaofeng -s C://')

    print('Total elapsed time: {0}\n'.format(time.time() - start_time))
    