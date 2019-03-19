a='0269FAC9A0'
# a='0DEC'
password={'001101':0,'010011':1,'111011':2,'110001':3,'100011':4,
          '110111':5,'001011':6,'111101':7,'011001':8,'101111':9}
data=list(map(str,a))
l=len(data)
lp=len(password)
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
print(r)
r=list(map(str,r))
print(r)
lr=len(r)
for j in range(lr-6):
    b=''.join(r[j:j+6])
    if b in password:
        print(password[b],end=' ')
        r[j:j+6]=['5','5','5','5','5','5']