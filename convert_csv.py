import csv
import inspect, os
from pathlib import Path

for file in os.listdir("/Users/Jonas/Documents/Studium/Master/SS18/Applied Analytics/Challenge/Data/crypto"):
    if file.endswith(".csv"):
        filename = os.path.splitext(file)[0] #ohne endung
        filename2 = (os.path.normpath(file)) # mit endung

        #filepath_in = os.path.realpath(file) schneidet letzte zwei Ordner weg, deswegen drunter
        filepath_in = os.path.dirname(os.path.abspath(file)) + "/Data/crypto/" + filename2
        filepath_out = filepath_in + filename + ".csv"
        print(filepath_out)
        

        #filepath_in = '/Users/Jonas/Documents/Studium/Master/SS18/Applied Analytics/Challenge/Data/crypto/ada.csv'
        with open(filepath_in,'r') as csvinput:
            with open(filepath_out, 'w') as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                all = []
                row = next(reader)

                row.append('currencyName')
                all.append(row)
                row_length = len(row)

                for row in reader:
                    row[row_length-1] = 'motherfucker'
                    all.append(row)
                
                writer.writerows(all)

