class Solution:
    def closestNumber(self, n, m):
        # code here 
      m=abs(m) 
      lower = (n//m)*m
      upper =lower +m
      if abs(n-lower) < abs(upper-n):
          return lower
      if abs(n-lower)> abs(upper-n):
          return upper
      else:
          return lower if abs(lower) > abs(upper) else upper