# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "./mapper_score_res.csv"
file1 = open(fname1, "rb")

f = open('score_min.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    i = 0
    min_time = 0
    min_comments = 0
    min_shares = 0
    min_replies = 0
    min_comments_likes = 0
    min_none = 0
    min_like = 0
    min_love = 0
    min_wow = 0
    min_haha = 0
    min_sad = 0
    min_angry = 0
    min_thankful = 0
    for row in reader1:
        if(i==2):
            if row[1] and min_time > int(str(row[1])):
                min_time = int(str(row[1]))

            if row[2] and min_comments > int(str(row[2])):
                min_comments = int(str(row[2]))

            if row[3] and min_shares > int(str(row[3])):
                min_shares = int(str(row[3]))

            if row[4] and min_replies > int(str(row[4])):
                min_replies = int(str(row[4]))

            if row[5] and min_comments_likes > int(str(row[5])):
                min_comments_likes = int(str(row[5]))

            if row[6] and min_none > int(str(row[6])):
                min_none = int(str(row[6]))

            if row[7] and min_like > int(str(row[7])):
                min_like = int(str(row[7]))

            if row[8] and min_love > int(str(row[8])):
                min_love = int(str(row[8]))

            if row[9] and min_wow > int(str(row[9])):
                min_wow = int(str(row[9]))

            if row[10] and min_haha > int(str(row[10])):
                min_haha = int(str(row[10]))

            if row[11] and min_sad > int(str(row[11])):
                min_sad = int(str(row[11]))

            if row[12] and min_angry > int(str(row[12])):
                min_angry = int(str(row[12]))

            if row[13] and min_thankful > int(str(row[13])):
                min_thankful = int(str(row[13]))
        if(i == 1):
            min_time = int(str(row[1]))
            min_comments = int(str(row[2]))
            min_shares = int(str(row[3]))
            min_replies = int(str(row[4]))
            min_comments_likes = int(str(row[5]))
            min_none = int(str(row[6]))
            min_like = int(str(row[7]))
            min_love = int(str(row[8]))
            min_wow = int(str(row[9]))
            min_haha = int(str(row[10]))
            min_sad = int(str(row[11]))
            min_angry = int(str(row[12]))
            min_thankful = int(str(row[13]))
            i+=1
        if(i == 0):
            f.write(''.join([row[1], "\t", row[2], "\t", row[3], "\t", row[4], "\t", row[5], "\t", row[6], "\t", row[7], "\t", row[8], "\t", row[9], "\t", row[10], "\t", row[11], "\t", row[12], "\t", row[13], "\n"]))
            i += 1

    f.write(''.join([str(min_time), "\t", str(min_comments), "\t", str(min_shares), "\t", str(min_replies), "\t", str(min_comments_likes), "\t", str(min_none), "\t", str(min_like), "\t", str(min_love), "\t", str(min_wow), "\t", str(min_haha), "\t", str(min_sad), "\t", str(min_angry), "\t", str(min_thankful), "\n"]))
     
finally:
    file1.close()