# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "./mapper_score_time_place_res_sorted.csv"
file1 = open(fname1, "rb")

f = open('score_avg_by_place_hour.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    ancienPlace = ""
    courentPlace = ""
    ancienTime = ""
    courentTime = ""
    v = 0
    i = 0
    f.write(''.join(["place", "\t", "hour", "\t", "avg", "\n"]))
    for row in reader1:
        courantPlace = row [0]
        courantTime = row [1]
        if((ancienPlace == "")or(ancienPlace==courantPlace)):
            if((ancienTime == "")or(ancienTime==courantPlace)):
                if not(row[2] == "score"):
                    i+=1
                    v += float(str(row[2]))
                    ancienTime = courantTime
                    ancienPlace = courantPlace
            else:
                a = v/i
                f.write(''.join([ancienPlace, "\t", ancienTime, "\t", str(a), "\n"]))
                i = 1
                v = float(str(row[2]))
                ancienTime = courantTime
                ancienPlace = courantPlace
        else:
            a = v/i
            f.write(''.join([ancienPlace, "\t", ancienTime, "\t", str(a), "\n"]))
            i = 1
            v = float(str(row[2]))
            ancienTime = courantTime
            ancienPlace = courantPlace
    a = v/i
    f.write(''.join([ancienPlace, "\t", ancienTime, "\t", str(a), "\n"]))
finally:
    file1.close()