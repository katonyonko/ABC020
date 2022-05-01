import io
import sys

_INPUT = """\
6
1
2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  Q=int(input())
  if Q==1: print('ABC')
  else: print('chokudai')