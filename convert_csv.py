import csv
import inspect, os

for file in os.listdir(os.getcwd() + '/Data/crypto'):
    if file.endswith(".csv"):
                 
        filename = os.path.splitext(file)[0] #ohne endung
        filename2 = (os.path.normpath(file)) # mit endung

        #filepath_in = os.path.realpath(file) schneidet letzte zwei Ordner weg, deswegen die Zeile drunter
        filepath_in = os.path.dirname(os.path.abspath(file)) + "/Data/crypto/" + filename2
        filepath_out = filepath_in[0:-4] + "_neu" + ".csv"
        if "neu" not in filename:
            with open(filepath_in,'r') as csvinput:
                with open(filepath_out, 'w') as csvoutput:
                    os.remove(filepath_in)
                    writer = csv.writer(csvoutput, lineterminator='\n')
                    reader = csv.reader(csvinput)

                    all = []
                    row = next(reader)

                    row.append('currencyName')
                    all.append(row)
                    row_length = len(row)

                    for row in reader:
                        try:
                            row[row_length-1] = filename
                            all.append(row)
                        except:
                            print("Schonmal konvertiert")
                    
                    writer.writerows(all)