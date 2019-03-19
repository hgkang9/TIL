a='01D06079861D79F99F'
# a='0F97A3'
data=list(map(str,a))
l=len(data)
r=[0]*(4*l)
for i in range(0,l):
    if data[i].isnumeric():
        for j in range((i+1)*4-1,(i+1)*4-5,-1):
            r[j]=int(data[i])%2
            data[i]=int(data[i])//2
    else:
        for j in range((i+1)*4-1,(i+1)*4-5,-1):
            if str(data[i]).isnumeric():
                r[j] = int(data[i]) % 2
                data[i] = int(data[i]) // 2
            else:
                r[j]=(ord(data[i])-55)%2
                data[i]=(ord(data[i])-55)//2
# print(r)
s=0
for i in range(len(r)):
    s=s*2+int(r[i])
    if (i+1)%7==0:
        print(s,end=' ')
        s=0
    elif i==len(r)-1:
        print(s)