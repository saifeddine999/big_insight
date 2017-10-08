# -*- coding: utf-8 -*- 
import csv, math, numpy

fname1 = "./mapper_score_res.csv"
file1 = open(fname1, "rb")

fname2 = "./score_max.csv"
file2 = open(fname2, "rb")

fname3 = "./score_min.csv"
file3 = open(fname3, "rb")

f = open('reduce_score_res.csv', 'w')

try:
    reader1 = csv.reader(file1, delimiter='\t')
    reader2 = csv.reader(file2, delimiter='\t')
    reader3 = csv.reader(file3, delimiter='\t')

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

    range_time = 0
    range_comments = 0
    range_shares = 0
    range_replies = 0
    range_comments_likes = 0
    range_none = 0
    range_like = 0
    range_love = 0
    range_wow = 0
    range_haha = 0
    range_sad = 0
    range_angry = 0
    range_thankful = 0

    f.write(''.join(["post_id", "\t", "place", "\t", "score", "\t", "hour", "\n"]))
            
    for row in reader2:
        if not(row[0] == "post_published_unix"):
            max_time = int(str(row[0]))
            max_comments = int(str(row[1]))
            max_shares = int(str(row[2]))
            max_replies = int(str(row[3]))
            max_comments_likes = int(str(row[4]))
            max_none = int(str(row[5]))
            max_like = int(str(row[6]))
            max_love = int(str(row[7]))
            max_wow = int(str(row[8]))
            max_haha = int(str(row[9]))
            max_sad = int(str(row[10]))
            max_angry = int(str(row[11]))
            max_thankful = int(str(row[12]))

    for row in reader3:
        if not(row[0] == "post_published_unix"):
            min_time = int(str(row[0]))
            min_comments = int(str(row[1]))
            min_shares = int(str(row[2]))
            min_replies = int(str(row[3]))
            min_comments_likes = int(str(row[4]))
            min_none = int(str(row[5]))
            min_like = int(str(row[6]))
            min_love = int(str(row[7]))
            min_wow = int(str(row[8]))
            min_haha = int(str(row[9]))
            min_sad = int(str(row[10]))
            min_angry = int(str(row[11]))
            min_thankful = int(str(row[12]))

            range_time = max_time - min_time
            range_comments = max_comments - min_comments
            range_shares = max_shares - min_shares
            range_replies = max_replies - min_replies
            range_comments_likes = max_replies - min_replies
            range_none = max_none - min_none 
            range_like = max_like - min_like 
            range_love = max_love - min_love 
            range_wow = max_wow - min_wow 
            range_haha = max_haha - min_haha 
            range_sad = max_sad - min_sad 
            range_angry = max_angry - min_angry
            range_thankful = max_thankful - min_thankful 
    
    for row in reader1:
        if not(row[0] == "post_id"):
            score = 0
            if row[1] != '' and not(range_time == 0):
                score = score +(((float(str(row[1]))-min_time)/range_time)*0.1)
            if row[2] != '' and  not(range_comments == 0):
                score = score +(((float(str(row[2]))-min_comments)/range_comments)*0.05)
            if row[3] != '' and  not(range_shares == 0):
                score = score +(((float(str(row[3]))-min_shares)/range_shares)*0.1)
            if row[4] != '' and  not(range_replies == 0):
                score = score +(((float(str(row[4]))-min_replies)/range_replies)*0.025)
            if row[5] != '' and  not(range_comments_likes == 0):
                score = score +(((float(str(row[5]))-min_comments_likes)/range_comments_likes)*0.025)
            if row[6] != '' and  not(range_none == 0):
                score = score +(((float(str(row[6]))-min_none)/range_none)*0.1)
            if row[7] != '' and  not(range_like == 0):
                score = score +(((float(str(row[7]))-min_like)/range_like)*0.05)
            if row[8] != '' and  not(range_love == 0):
                score = score +(((float(str(row[8]))-min_love)/range_love)*0.1)
            if row[9] != '' and  not(range_wow == 0):
                score = score +(((float(str(row[9]))-min_wow)/range_wow)*0.1)
            if row[10] != '' and  not(range_haha == 0):
                score = score +(((float(str(row[10]))-min_haha)/range_haha)*0.1)
            if row[11] != '' and  not(range_sad == 0):
                score = score +(((float(str(row[11]))-min_sad)/range_sad)*0.1)
            if row[12] != '' and  not(range_angry == 0):
                score = score +(((float(str(row[12]))-min_angry)/range_angry)*0.1)
            if row[13] != '' and  not(range_thankful == 0):
                score = score +(((float(str(row[13]))-min_thankful)/range_thankful)*0.05)

            f.write(''.join([row[0], "\t", row[14], "\t", str(score), "\t", row[15], "\n"]))
    
finally:
    file1.close()
    file2.close()
    file3.close()
