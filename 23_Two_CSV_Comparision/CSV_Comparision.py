import csv

with open('movi.csv', mode='r') as csv_file1, open('item_sim.csv', mode='r') as csv_file2, open('result_csv.csv','w', newline='') as result_csv:
    movi_csv = list(csv.reader(csv_file1, delimiter=','))
    item_csv = list(csv.reader(csv_file2, delimiter=','))
    result_csv = csv.writer(result_csv, delimiter=',') 
    
    for i in range(len(movi_csv)):
            if movi_csv[i] not in item_csv:
                result_csv.writerow(movi_csv[i]) 
                
        