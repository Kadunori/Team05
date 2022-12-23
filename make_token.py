import txtlist as mklist
import csv

csv_name = "./XSS_data_all.csv"
before_data_list = mklist.Maketxt(csv_name)
normal_list = before_data_list[0]
XSS_list = before_data_list[1]

for n in range(len(normal_list)-1):
    normal_list[n][0] = "0"

for i in XSS_list:
    for j in i:
        if j == "=":
            XSS_list[XSS_list.index(i)][i.index(j)-1] = "OreVar"
        elif j == "(":
            XSS_list[XSS_list.index(i)][i.index(j)-1] = "OreDef"

for i in range(len(XSS_list)):
    txt = " ".join(XSS_list[i][1])
    XSS_list[i][1] = txt

for i in range(len(normal_list)):
    txt = " ".join(normal_list[i][1])
    normal_list[i][1] = txt

print(XSS_list)
print(normal_list)

n_normal = len(normal_list)
n_XSS = len(XSS_list)

diff = n_normal - n_XSS

if diff < 0:
    all_num = n_normal
else:
    all_num = n_XSS

num = int(all_num * 0.8)

train_normal_list = normal_list[:num]
test_normal_list = normal_list[num:all_num]
train_XSS_list = XSS_list[:num]
test_XSS_list = XSS_list[num:all_num]

train_list = train_normal_list + train_XSS_list
test_list = test_normal_list + test_XSS_list

with open("./train/train_all.csv","w",encoding="utf-8",newline="") as tr:
    tr_wirter = csv.writer(tr)
    tr_wirter.writerows(train_list)

with open("./test/test_all.csv","w",encoding="utf-8",newline="") as te:
    te_wirter = csv.writer(te)
    te_wirter.writerows(test_list)
