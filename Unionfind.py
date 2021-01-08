# UnionFind

Group = [i for i in range(n+1)] # グループ分け
Nodes = [1]*(n+1) # 各グループのノードの数

def find(x):
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):
    if find(x) != find(y):
        if Nodes[find(x)] < Nodes[find(y)]:
            
            Nodes[find(y)] += Nodes[find(x)]
            Nodes[find(x)] = 0
            Group[find(x)] = find(y)
            
        else:
            Nodes[find(x)] += Nodes[find(y)]
            Nodes[find(y)] = 0
            Group[find(y)] = find(x)
