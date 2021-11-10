# This scripy is for csv file practice.
# Author: miaochaofeng
# Time:   2021-11-11

import argparse, os, time, sys
from csvFile import csvFile
    
if __name__ == '__main__':
    start_time = time.time()
    cmdList ='F:\code\Python\ExerciseBook\src\csvFile.py -t miaochaofeng'
    sys.args = cmdList.split(' ')
    csvFile = csvFile('-t linkaife')
    print(sys.args)
    print(csvFile.test)
    print(csvFile.destination)
#     demo = csvFile(sys.args)
#     demo.run()
#     os.system(cmdList)
#     demo = csvFile('-t miaochaofeng -s C://')

    print('Total elapsed time: {0}\n'.format(time.time() - start_time))