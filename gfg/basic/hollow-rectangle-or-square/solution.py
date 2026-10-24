class Solution:
    def printHollowRect(self, n, m):
        # code here
        for i in range (n):
            for j in range(m):
                if i==0 or j==0 or i==n-1or j==m-1:
                  print("*",end="")
                else:
                  print( " ",end="")
            print()
                