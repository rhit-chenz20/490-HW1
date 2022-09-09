import numpy as np
import random
# a = np.array((1, 2))
# b = np.array((4, 5))

# dist = np.linalg.norm(a-b)

# print(dist)

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
totalDistance = 0
genomeLength = 15
genome = [1, 13, 2, 15, 9, 5, 7, 3, 12, 14, 10, 8, 6, 4, 11, 1]
for k in range(genomeLength):
    a = np.array(map.get(genome[k]))

    if ((k + 1) == genomeLength):
        b = np.array(map.get(genome[0]))
    else:
        b = np.array(map.get(genome[k+1]))
    
    totalDistance += np.linalg.norm(a-b)
print(totalDistance)
print(genome)
# for x in range(len(genome)):

#     if(random.uniform(0,1) <= .1):

#         anotherindex = random.randint(0, len(genome))

#         while(anotherindex==x):

#             anotherindex = random.randint(0, len(genome))

                

#         temp = genome[x]

#         genome[x] = genome[anotherindex]

#         genome[anotherindex] = temp
#         print(genome)
# gene1 = [1,2,3,4,5,6,7,8]
# gene2 = [8,7,6,5,4,3,2,1]

# start = random.randint(0, len(gene1))

# size = random.randint(0, len(gene1))

# childGenome = [None]*len(gene1)

# for x in range(start, (start + size), 1):
#     childGenome[x % len(gene1)] = gene1[x % len(gene1)]


# i = (start+size) % len(gene1)

# for x in range(len(gene2)):
#     if (gene2[x] not in childGenome):
#         childGenome[i] = gene2[x]
#         i = (i + 1) % len(gene1)
    
    

