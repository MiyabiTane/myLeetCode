class UnionFind:
    def __init__(self, n): #最初はn個の要素全てが親
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n #木の高さ
        self.size = [1] * n #iを根とするグループのサイズ
    
    def find_root(self, x): #xの根を見つける
        if self.parent[x]==x:
            return x
        #xを根に直接くっつけて経路圧縮
        self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]
    
    def unite(self, x, y): #xとyの属する集合を合体
        x = self.find_root(x)
        y = self.find_root(y)
        if x!=y:
            if self.rank[x]<self.rank[y]:
                self.parent[x]=y
                self.size[y]+=self.size[x]
            else:
                self.parent[y]=x
                self.size[x]+=self.size[y]
                if self.rank[x]==self.rank[y]:
                    self.rank[x]+=1
        
    def is_same(self,x,y): #x,yが同じ集合に属するかどうか
        return self.find_root(x)==self.find_root(y)

    def group_size(self,x): #xが属するグループの大きさ
        return self.size[self.find_root(x)]

N, M, K=map(int,input().split())
A,B = [0] * M, [0] * M 
C,D = [0] * K, [0] * K

direct=[[] for i in range(N)] #同じ集合の友達もしくはブロック関係の人
unionfind=UnionFind(N) #N個の根をもつUnion Find木

for i in range(M):
    A[i],B[i]=map(int, input().split())
    A[i] -= 1
    B[i] -= 1
    direct[A[i]].append(B[i])
    direct[B[i]].append(A[i])
    unionfind.unite(A[i],B[i])
for i in range(K):
    C[i], D[i] = map(int, input().split())
    C[i] -= 1
    D[i] -= 1
    if unionfind.is_same(C[i],D[i]):
        direct[C[i]].append(D[i])
        direct[D[i]].append(C[i])
    
ans = [0] * N
for i in range(N):
    #友達候補 ＝ 木の大きさ - (元から友達の人＋ブロックリストの人) - 自分自身
    ans[i] = unionfind.group_size(i) - len(direct[i]) - 1
print(*ans)

#Union-Findデータ構造：https://atc001.contest.atcoder.jp/tasks/unionfind_a
