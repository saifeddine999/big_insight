# -*- coding: utf-8 -*- 
import csv, math, numpy, json
import time
from datetime import datetime

fname1 = "./count_by_hour.csv"
file1 = open(fname1, "rb")

f = open('count_by_hour_data.json', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    f.write("([")
    i = 0
    for row in reader1:
        if(row[0] != 'hour'):
            if(i==1):
                f.write(", ")
            i = 1
            f.write("[")
            row[0] = row[0].replace("T", " ")
            row[0] = row [0]+":00"
            datetime_object = datetime.strptime(row [0], '%Y-%m-%d %H:%M')
            f.write("Date.UTC(")
            f.write(str(datetime_object.year))
            f.write(",")
            f.write(str(datetime_object.month))
            f.write(",")
            f.write(str(datetime_object.day))
            f.write("), ")
            f.write(row[1])  
            f.write("]")
    f.write("])")
finally:
    file1.close()