from zipfile import ZipFile
import json
import os
import shutil
import csv
import pandas as pd


def json2csv(passJson): ### THIS IS A DEAD FUNCTION
    with open(passJson, "r") as read_file:
        data = json.load(read_file)
    df = pd.json_normalize(data)
    df.to_csv(r'outputFile.csv', index = None)
    #print(data)
    print("wat?")

def keyd(passJson2):
    
    with open(passJson2, "r") as read_file:
        dataJson = json.loads(read_file.read())

    keysList = []
    with open('keys\keys.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            keysList.append(row)

    completeList = []
    keyd = []

    airline = dataJson['organizationName']
    completeList.append(airline)
    for i in range(len(keysList)):
        keyMatch = keysList[i][0]
        if keyMatch == airline:
            keyRow = i
            break

    keydRange = range(10) 
    for j in keydRange:
        keyd = list((keysList[keyRow][j+1]).split(", "))

        indexList = dataJson['boardingPass']
        for q in keyd:
            if q == "":
                completeList.append(" ")
                continue
            elif q.isnumeric():
                m = int(q)
            else:
                m = str(q)
            print(m)
            indexList = indexList[m]
        if indexList == dataJson['boardingPass']:
            continue
        else:
            indexList = indexList.replace("\n", " - ")
            completeList.append(indexList)
            print(indexList)
    with open('outputFile.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow(completeList)

def unzipper():
    # assign directory
    dir1 = 'pkpass'
    dir2 = 'passes'
    dir3 = 'unzipped'
    j = 0

    for filename in os.listdir(dir1):
        f = os.path.join(dir1, filename)

        if os.path.isfile(f):

            with ZipFile(f, 'r') as zipObject:
                listOfFileNames = zipObject.namelist()

                for passName in listOfFileNames:

                    if passName == "pass.json":
                        j += 1
                        zipObject.extract(passName, dir3)
                        shutil.move((dir3 + "/" + passName), (dir2 + "/" + str(j) + passName)) 
                        thisFile = dir2 + "/" + str(j) + passName

                        keyd(thisFile)                     
                
unzipper()
