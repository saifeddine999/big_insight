# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "./reduce_score_res_sort.csv"
file1 = open(fname1, "rb")

f = open('reducer_score_avg.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')

    f.write(''.join(["place", "\t", "avg", "\n"]))
    ancien = ""
    courent = ""
    i = 0
    v = 0
    for row in reader1:
        if not(row[2] == "score"):
            courant = row [1]
            if((ancien == "")or(ancien==courant)):
                i+=1
                v+=float(str(row[2]))
                ancien = courant
            else:
                a = v/i
                f.write(''.join([ancien, "\t", str(a), "\n"]))
                i = 1
                v=float(str(row[2]))
                ancien = courant
    a = v/i
    f.write(''.join([ancien, "\t", str(a), "\n"]))
    
finally:
    file1.close()
