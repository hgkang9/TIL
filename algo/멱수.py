def power1(a,b):
    if b==0:
        return 1
    elif b==1:
        return 0
    else:
        return a*power1(a,b-1)
def power2(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        temp=power2(a,b//2)
        return temp*temp #짝수:temp*temp, 홀수:a*temp*temp
def power3(a,b):
    ans=1
    while b>0:
        if b%2==1:
            ans*=a
        a=a*a
        b//=2
    return ans