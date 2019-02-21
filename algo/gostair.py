def gostair(here):
    global ans
    if here == howmany:
        ans += 1
        return
    if here > howmany:
        return
    gostair(here+1)
    gostair(here+2)
    #here+1로 갔다가 부모로 올라간다음 here+2 한 다음 자연사 / 스택구조

ans = 0
howmany = 3

start = 0
gostair(start)

print('ans = %d' %ans)
