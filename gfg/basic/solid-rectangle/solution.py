class Solution:
    def printSolidRectangle(self, n, m):
        # code here
        for i in range(n):
           for j in range (m):
                print("*",end=" ")
           print()