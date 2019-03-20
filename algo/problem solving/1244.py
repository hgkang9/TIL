import sys
sys.stdin = open("input.txt","r")
SN = int(input())
SW = list(map(int, input().split()))
# 학생수
N = int(input())
# M이 1이면 남자 2면 여자
# L = [0] * SN
for i in range(N):
    M,U=map(int, input().split())
    if M==1:
        # L[NUM] += 1
        # % NUM 이 아니라 반복문으로 할 것
        for k in range(1,U+1):
            if k*U-1<SN:
                if SW[k*U-1]==0:
                    SW[k*U-1]=1
                elif SW[k*U-1]==1:
                    SW[k*U-1]=0
    elif M==2:
        # if SW[NUM-1] == 1:
        #     SW[NUM-1] = 0
        # for y in range(SN):
        for x in range(SN):
            if U-x-1>=0and U+x-1<SN:
                # if SW[U+x-1]==SW[U-x-1]:
                if SW[U+x-1]==1:
                    SW[U+x-1]=0
                    SW[U-x-1]=0
                elif SW[U+x-1]==0:
                    SW[U+x-1]=1
                    SW[U-x-1]=1
        # ans=" ".join(map(str,SW))
        # for z in range(20):
        #     if len(ans) > 20:
        #         ans[20].(print())
        #         # ans[z]
        # print(ans)
        print(SW)
        # for i in range(SN):
        #     print(SW[i],end=' ')
        #     if i % 20 == 19 :
        #         print()


        # elif SW[NUM] == 0:
        #     SW[NUM] = 1
        #     for y in range(SN):
        #         for x in range(SN//2):
        #             if y-x != 0 and y+x < SN:
        #                 if SW[y+x] == SW[y-x]:
        #                     if SW[y+x] and SW[y-x] == 1:
        #                         SW[y+x] = 0
        #                         SW[y-x] = 0
        #                     elif SW[y+x] and SW[y-x] == 0:
        #                         SW[y+x] = 1
        #                         SW[y-x] = 1

# 1 0 0 0 1 1 0 1
