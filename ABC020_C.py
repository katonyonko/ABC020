import io
import sys

_INPUT = """\
6
2 3 10
S##
.#G
3 4 7
S##G
.##.
..#.
4 4 1000000000
S###
####
####
###G
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  def Dijkstra(G,s):
    done=[False]*len(G)
    inf=10**20
    C=[inf]*len(G)
    C[s]=0
    h=[]
    heappush(h,(0,s))
    while h:
      x,y=heappop(h)
      if done[y]:
        continue
      done[y]=True
      for v in G[y]:
        if C[v[1]]>C[y]+v[0]:
          C[v[1]]=C[y]+v[0]
          heappush(h,(C[v[1]],v[1]))
    return C

  H,W,T=map(int,input().split())
  S=[input() for _ in range(H)]
  l,r=1,10**10
  for i in range(H):
    for j in range(W):
      if S[i][j]=='S': si,sj=i,j
      if S[i][j]=='G': gi,gj=i,j
  while r-l>1:
    mid=(l+r)//2
    G=[[] for _ in range(H*W)]
    for i in range(H):
      for j in range(W):
        for k,l2 in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:
          if 0<=k<H and 0<=l2<W:
            if S[k][l2]=='#': G[i*W+j].append((mid,k*W+l2))
            else: G[i*W+j].append((1,k*W+l2))
    D=Dijkstra(G,si*W+sj)
    # if mid==4: print(D)
    if D[gi*W+gj]<=T: l=mid
    else: r=mid
  print(l)