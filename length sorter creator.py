import os
import csv
import re
fileNames = []

mainPath = 'E:\Programming\Pycharm\PycharmProjects\sentenceLengthInCSV' ##directory containing all csv files
## get all filenames and add to fileNames array
for file in [f for f in os.listdir(mainPath) if f.endswith('.csv')]:
    fileNames.append(os.path.join(file))
print("filenames: ")
print(fileNames)

## for every file
for i in range(len(fileNames)):
    ## CSV filename
    fileName = fileNames[i]
    fileNameForWrite = fileName[:-4] + "Edited_25-=30.csv"
    print(fileNameForWrite)
    print("current filename: ")
    print(fileName)
    ## initialise
    rows = []
    sentenceLength = []
    ## read csv
    with open(fileName, "r") as csvfile:
        ## CSV reader
        reader = csv.reader(csvfile)
        ## for every row in the csv
        print(reader)
        count = 0
        for row in reader:
            #print("row")
            #print(row)
            ## make sure to include the headers row
            if ((count == 0) or ((30 >= len(re.findall(r'\w+', row[0]))) and (25 < len(re.findall(r'\w+', row[0]))))):
                ## append rows to rows
                rows.append(row)
            count += 1
        print(sentenceLength)
        ## get total number of rows
        print("Total number of rows: %d" % (reader.line_num))


    with open(fileNameForWrite, 'w') as writeFile:
        print(rows)
        writer = csv.writer(writeFile)
        writer.writerows(rows)

