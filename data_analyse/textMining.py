# -*- coding: utf-8 -*- 
import csv, math, numpy

tunis = ["tounes","tunis","تونس"];
sfax = ["sfax","صفاقس"];
sousse = ["sousse","soussa","سوسة"];
ariana = ["ariana","aryana","aryanah","أريانة"];
beja = ["béja","beja","baja","باجة"];
benArous = ["ben arous","benarous","ben arouss","benarouss","ben 3rouss","ben 3rouss","ben 3rous","ben 3rous","بن عروس"];
bizert = ["bizert","benzart","بنزرت"];
gabes = ["gabes","gabès","قابس"];
gafsa = ["gafsa","قفصة"];
jendouba = ["jendouba","جندوبة"];
kairouan = ["kairouan","kayrawen","9orwan","9ayrawen","قيروان"];
kasserine = ["kasserine","kasrine","قصرين"];
kebeli = ["kébili","kbeli","قبلي"];
kef = ["kef","كاف"];
mahdia = ["mahdia","mahdiya","مهدية"];
manouba = ["manouba","manoubah","mannouba","منوبة"];
medenine = ["médenine","medenine","mednine","médnine","مدنين"];
monastir = ["monastir","mestir","منستير"];
nabeul = ["nabeul","nabel","نابل"];
sidiBouzid = ["sidi bouzid","سيدي بوزيد"];
siliana = ["siliana","selyana","سليانة"];
tataouine = ["tataouine","tataouin","tatawine","tatawin","تطاوين"];
tozeur = ["tozeur","touzer","توزر"];
zaghouan = ["zaghouan","zaghwen","za8wen","za8ouan","زغوان"];


fname = "D:\hackaton big data\winou trottoir - 04-01-16 -- 04-03-16\group_1008279892518211_2017_09_11_13_24_52_fullstats.tab"
file = open(fname, "rb")

f = open('sortie_posts1.csv', 'w')

try:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        if row[4] == "post_message":
            f.write(''.join([''.join(e + "\t" for e in row), "place", "\n"]))
        test = 0 
        if test == 0:
            for name in tunis:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "tunis", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in sfax:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "sfax", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in sousse:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "sousse", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in ariana:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "ariana", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in beja:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "beja", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in benArous:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "benArous", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in bizert:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "bizert", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in gabes:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "gabes", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in gafsa:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "gafsa", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in jendouba:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "jendouba", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in kairouan:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "kairouan", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in kasserine:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "kasserine", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in kebeli:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "kebeli", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in kef:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "kef", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in mahdia:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "mahdia", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in manouba:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "manouba", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in medenine:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "medenine", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in monastir:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "monastir", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in nabeul:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "nabeul", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in sidiBouzid:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "sidiBouzid", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in siliana:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "siliana", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in tataouine:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "tataouine", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in tozeur:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "tozeur", "\n"]))
                    test = 1
                    break
        if test == 0:
            for name in zaghouan:
                if name in row[4]:
                    f.write(''.join([''.join(e + "\t" for e in row), "zaghouan", "\n"]))
                    test = 1
                    break

finally:
    file.close()