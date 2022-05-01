import io
import sys

_INPUT = """\
6
1 23
999 999
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=input().split()
  print(2*int(A+B))