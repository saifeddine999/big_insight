# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "../sortie_posts1.csv"
file1 = open(fname1, "rb")

fname2 = "../sortie_posts2.csv"
file2 = open(fname2, "rb")

fname3 = "../sortie_posts3.csv"
file3 = open(fname3, "rb")

fname4 = "../sortie_posts4.csv"
file4 = open(fname4, "rb")

fname5 = "../sortie_posts5.csv"
file5 = open(fname5, "rb")

fname6 = "../sortie_posts6.csv"
file6 = open(fname6, "rb")

fname7 = "../sortie_posts7.csv"
file7 = open(fname7, "rb")

fname8 = "../sortie_posts8.csv"
file8 = open(fname8, "rb")

fname9 = "../sortie_posts9.csv"
file9 = open(fname9, "rb")

f = open('mapper_score_res.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    reader2 = csv.reader(file2, delimiter='\t')
    reader3 = csv.reader(file3, delimiter='\t')
    reader4 = csv.reader(file4, delimiter='\t')
    reader5 = csv.reader(file5, delimiter='\t')
    reader6 = csv.reader(file6, delimiter='\t')
    reader7 = csv.reader(file7, delimiter='\t')
    reader8 = csv.reader(file8, delimiter='\t')
    reader9 = csv.reader(file9, delimiter='\t')
    for row in reader1:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader2:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader3:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader4:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader5:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader6:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader7:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader8:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))
    for row in reader9:
        f.write(''.join([row[2], "\t", row[10], "\t", row[13], "\t", row[15], "\t", row[19], "\t", row[20], "\t", row[21], "\t", row[22], "\t", row[23], "\t", row[24], "\t", row[25], "\t", row[26], "\t", row[27], "\t", row[28], "\t", row[29], "\t", row[11], "\n"]))

finally:
    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()
    file7.close()
    file8.close()
    file9.close()