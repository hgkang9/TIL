# data=[1,2,4,7,8,3]
# data=[6,6,7,7,6,7]
# data=[0,5,4,0,6,0]
# data=[1,0,1,1,2,3]
data=[1,3,8,2,7,9]
res=[]
for i1 in range(len(data)):
    for i2 in range(len(data)):
        if i1!=i2:
            for i3 in range(len(data)):
                if i3!=i1 and i3!=i2:
                    for i4 in range(len(data)):
                        if i4!=i1 and i4!=i2 and i4!=i3:
                            for i5 in range(len(data)):
                                if i5!=i1 and i5!=i2 and i5!=i3 and i5!=i4:
                                    for i6 in range(len(data)):
                                        if i6 != i1 and i6 != i2 and i6 != i3 and i6 != i4 and i6!=i5:
                                            res+=[[data[i1],data[i2],data[i3],data[i4],data[i5],data[i6]]]

for y in range(len(res)):
    if res[y][0]==res[y][1]:
        if res[y][1]==res[y][2]:
            if res[y][3]==res[y][4]:
                if res[y][4]==res[y][5]:
                    print('baby-gin!')
                    break
            if res[y][4]-res[y][3]==1:
                if res[y][5]-res[y][4]==1:
                    print('baby-gin!')
                    break
    if res[y][1] - res[y][0] == 1:
        if res[y][2] - res[y][1] == 1:
            if res[y][4]-res[y][3]==1:
                if res[y][5]-res[y][4]==1:
                    print('baby-gin!')
                    break