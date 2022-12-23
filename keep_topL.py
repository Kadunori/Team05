import numpy as np
import csv
from ngram import make_ngram
from topl import topl



train_file = "./train/train_all_true.csv"
train_sample = []

with open(train_file,encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    train_data_list = list(csv_reader)

XSS_all_ngram = []

#print(train_data_list)

for data in train_data_list:
    if data[0] == "1":
        data[1] = data[1].split()
        ngram = make_ngram(data)
        for i in range(len(ngram[1])):
            XSS_all_ngram.append(ngram[1][i])

#print(XSS_all_ngram)

XSS_topL_list = topl(XSS_all_ngram)

with open("topL_true.txt","w",encoding="utf-8") as f:
    for top in XSS_topL_list:
        txt = ",".join(top)
        txt = txt + "\n"
        f.write(txt)
