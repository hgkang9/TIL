def atoi(s):
    n=0
    for i in range(len(s)):
        if s[i]=='A' or s[i]=='B' or s[i]=='C' or s[i]=='D' or s[i]=='E' or s[i]=='F':
            n += 16**(len(s)-1-i)*(ord(s[i])-55)
        else:
            n += 16**(len(s)-1-i)*(ord(s[i])-48)
    return n

print(atoi('42FB'))