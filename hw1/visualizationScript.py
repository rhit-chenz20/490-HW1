from matplotlib import pyplot as plt
import csv
from labellines import labelLine, labelLines


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
map = {1:[-0.0000000400893815,0.0000000358808126],

        2:[-28.8732862244731230,-0.0000008724121069],

        3:[-79.2915791686897506,21.4033307581457670],

        4:[-14.6577381710829471,43.3895496964974043],

        5:[-64.7472605264735108,-21.8981713360336698],

        6:[-29.0584693142401171,43.2167287683090606],

        7:[-72.0785319657452987,-0.1815834632498404],

        8:[-36.0366489745023770,21.6135482886620949],

        9:[-50.4808382862985496 ,-7.3744722432402208],

        10:[-50.5859026832315024 ,21.5881966132975371],

        11:[-0.1358203773809326,28.7292896751977480],

        12:[-65.0865638413727368,36.0624693073746769],

        13:[-21.4983260706612533,-7.3194159498090388],

        14:[-57.5687244704708050,43.2505562436354225],

        15:[-43.0700258454450875,-14.5548396888330487]}

x =[]
y =[]
for k in range(15):
    x.append(map.get(k+1)[0])
    y.append(map.get(k+1)[1])
generations = {}
with open('77431_geno.csv', 'r') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if (count > 0):
            generations[row[0]] = row[1:]
        count = count + 1

print(generations)
myList = list(generations.keys())
for j in range(10):
    for k in range(14):
        plt.plot([map.get(int(generations.get(str(myList[j]))[k]))[0],map.get(int(generations.get(str(myList[j]))[k+1]))[0]], [map.get(int(generations.get(str(myList[j]))[k]))[1],map.get(int(generations.get(str(myList[j]))[k+1]))[1]], label=str(k), alpha=.5, linewidth=5)
    plt.grid()
    plt.scatter(x, y)
    plt.legend()
    plt.savefig("ANDEREAD" + str(myList[j]) + ".jpeg")
    plt.clf()
