# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "./reduce_score_res.csv"
file1 = open(fname1, "rb")

f = open('mapper_score_time_place_res.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    
    f.write(''.join([ "place", "\t", "hour", "\t", "score", "\n"]))
            
    for row in reader1:
        f.write(''.join([row[1], "\t", row[3][:13], "\t", row[2], "\n"]))
    
finally:
    file1.close()
