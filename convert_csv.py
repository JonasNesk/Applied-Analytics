import csv

with open('/Users/Jonas/Documents/Studium/Master/SS18/Applied Analytics/Challenge/Data/crypto/ada.csv','r') as csvinput:
    with open('/Users/Jonas/Documents/Studium/Master/SS18/Applied Analytics/output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('Name_Waehrung')
        all.append(row)

        for row in reader:
            row[0] = 'motherfucker'
            row.append(row[0])
            all.append(row)
            

        writer.writerows(all)