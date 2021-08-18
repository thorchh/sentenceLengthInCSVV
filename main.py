## import
from matplotlib import pyplot as plt
import csv
import re
## CSV filename
filename = "NAME.csv"
## initialise
rows = []
sentenceLength = []
## read csv
with open(filename) as csvfile:
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