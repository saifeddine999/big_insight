# -*- coding: utf-8 -*- 
import csv, math, numpy, json

fname1 = "./reducer_score_avg_sorted.csv"
file1 = open(fname1, "rb")

f = open('reducer_score_avg.json', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    f.write("{'")
    i = 0
    for row in reader1:
        if(row[0] != 'place'):
            if i == 1:
                f.write(", '") 
            i = 1
            f.write(row[0])
            f.write("': ")
            f.write(str(float(row[1])*100))
    f.write("}")
finally:
    file1.close()