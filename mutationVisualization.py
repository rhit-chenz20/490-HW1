from matplotlib import pyplot as plt
import csv
import os
directory = r"C:\Users\deckerza\Desktop\Rose-Hulman\Junior_Year\Fall\CSSE490\490-HW1\Mutation"
runMap = [1283.0, 2891.0, 1345.0, 457.0, 56865.0, 34565.0, 25554.0, 765.0, 25645.0, 94843.0]
GenX= []
lowMutationBest={}
lowMutationWorst={}
lowMutationAvg={}
medMutationBest={}
medMutationWorst={}
medMutationAvg={}
highMutationBest={}
highMutationWorst={}
highMutationAvg={}
for k in range(10):
    runMap[k] = str(runMap[k])
for k in range(5001):
    GenX.append(k)
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, 'r') as file:
            reader = csv.reader(file)
            count = 1
            for row in reader:
                if (count > 1 and (count % 2 != 0)):
                    match filename.split("_")[1]:
                        case ".001":
                            if not ((filename.split("_")[2]) in lowMutationBest):
                                lowMutationBest[filename.split("_")[2]] = [round(float(row[2]))]

                            else:
                                lowMutationBest[filename.split("_")[2]].append(round(float(row[2])))
                            if not (filename.split("_")[2] in lowMutationAvg):
                                lowMutationAvg[filename.split("_")[2]] = [round(float(row[3]))]
                            else:
                                lowMutationAvg[filename.split("_")[2]].append(round(float(row[3])))
                            if not (filename.split("_")[2] in lowMutationWorst):
                                lowMutationWorst[filename.split("_")[2]] = [round(float(row[4]))]
                            else:
                                lowMutationWorst[filename.split("_")[2]].append(round(float(row[4])))
                        case ".01":
                            if not (filename.split("_")[2] in medMutationBest):
                                medMutationBest[filename.split("_")[2]] = [round(float(row[2]))]
                            else:
                                medMutationBest[filename.split("_")[2]].append(round(float(row[2])))
                            if not (filename.split("_")[2] in medMutationAvg):
                                medMutationAvg[filename.split("_")[2]] = [round(float(row[3]))]
                            else:
                                medMutationAvg[filename.split("_")[2]].append(round(float(row[3])))
                            if not (filename.split("_")[2] in medMutationWorst):
                                medMutationWorst[filename.split("_")[2]] = [round(float(row[4]))]
                            else:
                                medMutationWorst[filename.split("_")[2]].append(round(float(row[4])))
                        case ".1":
                            if not (filename.split("_")[2] in highMutationBest):
                                highMutationBest[filename.split("_")[2]] = [round(float(row[2]))]
                            else:
                                highMutationBest[filename.split("_")[2]].append(round(float(row[2])))
                            if not (filename.split("_")[2] in highMutationAvg):
                                highMutationAvg[filename.split("_")[2]] = [round(float(row[3]))]
                            else:
                                highMutationAvg[filename.split("_")[2]].append(round(float(row[3])))
                            if not (filename.split("_")[2] in highMutationWorst):
                                highMutationWorst[filename.split("_")[2]] = [round(float(row[4]))]
                            else:
                                highMutationWorst[filename.split("_")[2]].append(round(float(row[4])))
                count = count + 1

data = [lowMutationBest, lowMutationAvg, lowMutationWorst, medMutationBest, medMutationAvg, medMutationWorst, highMutationBest, highMutationAvg, highMutationWorst]      
fig, axs = plt.subplots(3, 3)    
fig.set_size_inches(8.5, 10)      
x = 0
y = 0
z = 0
for i in range(9):
    for j in range(10):
        if (j == z):
            axs[x, y].plot(GenX, data[i].get(runMap[j]), label=str(runMap[j]))
        else:
            axs[x, y].plot(GenX, data[i].get(runMap[j]))
    z = z + 1
    if (y < 2):
            y = y + 1
    else:
        y = 0
        x = x + 1
fig.legend()
fig.savefig("DONE.jpeg")

            
                
