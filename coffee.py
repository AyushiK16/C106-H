import csv
import numpy as np

def getDataSource(path):
    coffeeAmt = []
    sleepTime = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            coffeeAmt.append(int(row["Coffee in ml"]))
            sleepTime.append(int(row["sleep in hours"]))
    
    return {'x': coffeeAmt,
    'y' : sleepTime}

def findCorrelation(array1, array2):
    correlation = np.corrcoef(array1, array2)
    return correlation

data = getDataSource('data1.csv')
answer = findCorrelation(data['x'], data['y'])

print('The Correlation is - ', answer[0,1])

        