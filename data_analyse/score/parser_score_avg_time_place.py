# -*- coding: utf-8 -*- 
import csv, math, numpy, json
import time
from datetime import datetime

fname1 = "./score_avg_by_place_hour.csv"
file1 = open(fname1, "rb")

f = open('score_avg_by_place_hour.json', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    f.write("{'")
    ancienPlace = ""
    courentPlace = ""
    ancienTime = ""
    courentTime = ""
    i = 0
    for row in reader1:
        if(row[0] != 'place'):
            courantPlace = row [0]
            courantTime = row [1]

            if(ancienPlace == ""):
                f.write(row[0])
                f.write("': [[")
                row[1] = row [1]+":00"
                datetime_object = datetime.strptime(row [1], '%Y-%m-%d %H:%M')
                f.write(str(time.mktime(datetime_object.timetuple())))
                f.write(",")
                f.write(row[2])
                f.write("]")
                ancienTime = courantTime
                ancienPlace = courantPlace

            elif(ancienPlace==courantPlace):
                if(ancienTime!=courantPlace):
                    if not(row[2] == "avg"):
                        f.write(", [")
                        row[1] = row [1]+":00"
                        datetime_object = datetime.strptime(row [1], '%Y-%m-%d %H:%M')
                        f.write(str(time.mktime(datetime_object.timetuple())))
                        f.write(",")
                        f.write(row[2])
                        f.write("]")
                        ancienTime = courantTime
                        ancienPlace = courantPlace
            else:
                f.write("],")
                f.write(row[0])
                f.write("': [[")
                row[1] = row [1]+":00"
                datetime_object = datetime.strptime(row [1], '%Y-%m-%d %H:%M')
                f.write(str(time.mktime(datetime_object.timetuple())))
                f.write(",")
                f.write(row[2])
                f.write("]")
                ancienTime = courantTime
                ancienPlace = courantPlace

    f.write("]}")
finally:
    file1.close()