fp=open('binary.txt','r')

#for part 1
gamma=""
epsilon=""
#it assumes there won't be equal amounts of 1's and 0's
for i in range(len(fp.readline().rstrip())):
    fp.seek(0)
    count=0
    while line := fp.readline().rstrip():
        if line[i] == '1':
            count+=1
        else:
            count-=1
  
    if count > 0:
        gamma=gamma+"1"
        epsilon=epsilon+"0"
    else:
        gamma=gamma+"0"
        epsilon=epsilon+"1"

#for part 2
fp.seek(0)
o2=[]
co2=[]

#I would use a do-while if I could be bothered enough
while line := fp.readline().rstrip():
    if line[0]==gamma[0]:
        o2.append(line)
    else:
        co2.append(line)

for j in range(1,12):
    temp=[]
    if len(o2)==1:
        break
    count=0
    for i in range(len(o2)):
        if o2[i][j]=='1':
            count+=1
        else:
            count-=1

    for x in range(len(o2)):
        if count>=0:
            if o2[x][j]=='1':
                temp.append(o2[x])
        else:
            if o2[x][j]=='0':
                temp.append(o2[x])
    o2=temp
    
for j in range(1,12):
    temp=[]
    if len(co2)==1:
        break
    count=0
    for i in range(len(co2)):
        if co2[i][j]=='1':
            count+=1
        else:
            count-=1

    for x in range(len(co2)):
        if count==0:
            if co2[x][j]=='0':
                temp.append(co2[x])
        elif count>0:
            if co2[x][j]=='0':
                temp.append(co2[x])
        else:
            if co2[x][j]=='1':
                temp.append(co2[x])
    co2=temp
    
print(int(o2[0],2) * int(co2[0],2))

fp.close()
#results
print(int(gamma, 2) * int(epsilon, 2))
