# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "./mapper_sort.csv"
file1 = open(fname1, "rb")

f = open('count_by_gov.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    ancien = ""
    courent = ""
    i = 0
    f.write(''.join(["place", "\t", "count", "\n"]))
    for row in reader1:
        courant = row [0]
        if((ancien == "")or(ancien==courant)):
            i+=1
            ancien = courant
        else:
            f.write(''.join([ancien, "\t", str(i), "\n"]))
            i = 1
            ancien = courant
    f.write(''.join([ancien, "\t", str(i), "\n"]))
finally:
    file1.close()