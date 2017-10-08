# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "./mapper_score_res.csv"
file1 = open(fname1, "rb")

f = open('score_max.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    i = 0
    max_time = 0
    max_comments = 0
    max_shares = 0
    max_replies = 0
    max_comments_likes = 0
    max_none = 0
    max_like = 0
    max_love = 0
    max_wow = 0
    max_haha = 0
    max_sad = 0
    max_angry = 0
    max_thankful = 0
    for row in reader1:
        if(i==0):
            f.write(''.join([row[1], "\t", row[2], "\t", row[3], "\t", row[4], "\t", row[5], "\t", row[6], "\t", row[7], "\t", row[8], "\t", row[9], "\t", row[10], "\t", row[11], "\t", row[12], "\t", row[13], "\n"]))
            i += 1
        else:
            if row[1] and max_time < int(str(row[1])):
                max_time = int(str(row[1]))

            if row[2] and max_comments < int(str(row[2])):
                max_comments = int(str(row[2]))

            if row[3] and max_shares < int(str(row[3])):
                max_shares = int(str(row[3]))

            if row[4] and max_replies < int(str(row[4])):
                max_replies = int(str(row[4]))

            if row[5] and max_comments_likes < int(str(row[5])):
                max_comments_likes = int(str(row[5]))

            if row[6] and max_none < int(str(row[6])):
                max_none = int(str(row[6]))

            if row[7] and max_like < int(str(row[7])):
                max_like = int(str(row[7]))

            if row[8] and max_love < int(str(row[8])):
                max_love = int(str(row[8]))

            if row[9] and max_wow < int(str(row[9])):
                max_wow = int(str(row[9]))

            if row[10] and max_haha < int(str(row[10])):
                max_haha = int(str(row[10]))

            if row[11] and max_sad < int(str(row[11])):
                max_sad = int(str(row[11]))

            if row[12] and max_angry < int(str(row[12])):
                max_angry = int(str(row[12]))

            if row[13] and max_thankful < int(str(row[13])):
                max_thankful = int(str(row[13]))

    f.write(''.join([str(max_time), "\t", str(max_comments), "\t", str(max_shares), "\t", str(max_replies), "\t", str(max_comments_likes), "\t", str(max_none), "\t", str(max_like), "\t", str(max_love), "\t", str(max_wow), "\t", str(max_haha), "\t", str(max_sad), "\t", str(max_angry), "\t", str(max_thankful), "\n"]))
     
finally:
    file1.close()