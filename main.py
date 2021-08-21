fileNames = []
totalFilesLength = []
def getALLCSV():
    import os
    mainPath = 'E:\Programming\Pycharm\PycharmProjects\sentenceLengthInCSV' ##directory containing all csv files
    for file in [f for f in os.listdir(mainPath) if f.endswith('.csv')]:
        fileNames.append(os.path.join(file))
    print(fileNames)

def sentenceLengthInCSV(filename):
    ## import
    from matplotlib import pyplot as plt
    import csv
    import re
    plt.figure()
    ## CSV filename
    fileName = filename
    ## initialise
    rows = []
    sentenceLength = []
    ## read csv
    with open(fileName) as csvfile:
        ## CSV reader
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            if row[1] != "Type": ##edit this depending on if you have headers for your data e.g. this data had sentence and type as the two headers.
                rows.append(row)
                sentenceLength.append(len(re.findall(r'\w+', row[0])))
        print(sentenceLength)
        ## get total number of rows
        print("Total number of rows: %d" % (csvReader.line_num))
    ## create histogram
    plt.hist(sentenceLength)
    ## show graph
    plt.show()


def main():
    getALLCSV()
    print("heyo1")
    for i in range(len(fileNames)):
        sentenceLengthInCSV(fileNames[i])



import os
from matplotlib import pyplot as plt
import csv
import re

mainPath = 'E:\Programming\Pycharm\PycharmProjects\sentenceLengthInCSV' ##directory containing all csv files
for file in [f for f in os.listdir(mainPath) if f.endswith('.csv')]:
    fileNames.append(os.path.join(file))
print(fileNames)



## for every file
for i in range(len(fileNames)):
    ## new plot figure
    plt.figure()
    ## CSV filename
    fileName = fileNames[i]
    ## initialise
    rows = []
    sentenceLength = []
    ## read csv
    with open(fileName) as csvfile:
        ## CSV reader
        csvReader = csv.reader(csvfile)
        ## for every row in the csv
        for row in csvReader:
            ## not the headers
            if row[1] != "Type": ##edit this depending on if you have headers for your data e.g. this data had sentence and type as the two headers.
                ## append rows to rows
                rows.append(row)
                ## append the length to sentenceLength and totalFilesLength
                sentenceLength.append(len(re.findall(r'\w+', row[0])))
                totalFilesLength.append(len(re.findall(r'\w+', row[0])))
        print(sentenceLength)
        ## get total number of rows
        print("Total number of rows: %d" % (csvReader.line_num))
    ## create histogram
    plt.hist(sentenceLength)
    ## show graph
plt.figure()
plt.hist(totalFilesLength)
plt.show()



