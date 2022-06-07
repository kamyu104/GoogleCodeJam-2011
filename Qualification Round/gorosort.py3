# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2011 Qualification Round - Problem D. GoroSort
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432f3a/0000000000432ccf
#
# Time:  O(N)
# Space: O(1)
#

def gorosort():
    N = int(input())
    a = list(map(lambda x: int(x)-1, input().split()))
    return sum(x != i for i, x in enumerate(a))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, gorosort()))
