import csv
import numpy as np

def getDataSource(path):
    attendence = []
    score = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            attendence.append(int(row['Days Present']))
            score.append(float(row['Marks In Percentage']))

    return {'x' : attendence,
    'y' : score}

def findCorrelation(array1, array2):
    correlation = np.corrcoef(array1, array2)
    return correlation[0,1]

data = getDataSource('data2.csv')
answer = findCorrelation(data['x'], data['y'])

print("The correlation is - ", answer)