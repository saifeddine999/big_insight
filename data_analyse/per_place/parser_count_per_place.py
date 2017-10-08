# -*- coding: utf-8 -*- 
import csv, math, numpy, json

fname1 = "./count_by_gov_sorted.csv"
file1 = open(fname1, "rb")

f = open('count_by_gov_sorted.json', 'w')

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
            f.write(row[1])    
    f.write("}")
finally:
    file1.close()