n=int(input())#记忆化搜索
g=[-1 for _ in range(1010)]
g[1]=1
def wa(n,g):
    if g[n]!=-1:
        return g[n]
    else:
        g[n]=sum(wa(i,g) for i in range(1,n//2+1))+1
        return g[n]
print(wa(n,g))