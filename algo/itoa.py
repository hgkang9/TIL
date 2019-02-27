def itoa(n):
    s=''
    while True:
        s=chr(n%10+48)+s
        n=n//10
        if n==0:
            return s

print(type(itoa(123)))