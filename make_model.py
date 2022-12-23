import numpy as np
from sklearn import svm
import pickle
import csv
from ngram import make_ngram
from topl import topl
from vector import vector


train_file = "./train/train_all_true.csv"
train_sample = []

"""
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
#print(XSS_topL_list)
"""

topL_file = "./topL_true.txt"
topL_list = []

with open(topL_file,encoding="utf-8") as f:
    lines = f.read()
    for line in lines.split("\n"):
        top = line.split(",")
        topL_list.append(top)

with open(train_file,encoding="utf-8-sig") as f:
    csv_reader = csv.reader(f)
    train_data_list = list(csv_reader)

for train in train_data_list:
    train[1] = train[1].split()
    train_ngram = make_ngram(train)
    train_vector = vector(train_ngram[1],topL_list)
    #print(train)
    train_vector.insert(0, int(train[0]))
    train_sample.append(train_vector)

#print(sample_list)
#print(train_sample)

train_sample = np.array(train_sample)
train_label = train_sample[:, 0].astype(int)
train_data = train_sample[:, 1:10]

#print(train_sample)
#print(train_label)
#print(train_data)

#train_label = train_sample[0].astype(int)
#train_data = train_sample[1]
model = svm.SVC(gamma="scale")
model.fit(train_data, train_label)

model_file = 'finalized_model_true.sav'
pickle.dump(model, open(model_file, 'wb'))
