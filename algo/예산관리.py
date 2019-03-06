B = 49 #40
n = 6
data = [2,5,9,13,21] #[7,13,17,19,29,31]
l=len(data)
ans=0
def budget(now, sum):
    global B, ans, l

    if sum > ans and sum<=B:
        ans = sum

    if sum > B:
        return

    if now+1 > l:
        return
    # if now+1<=6:
    budget(now+1, sum+data[now])
    budget(now+1, sum)

budget(0, 0)

print(ans)












# for i in range(1<<l):
#     subset = []
#     for j in range(l):
#         if i & (1<<j):
#             subset.append(data[j])
#     print(subset)