# Print Hollow Rectangle

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two integers  **n**  and  **m**, print a hollow rectangle pattern consisting of n rows and m columns using  **'*'** character **.** 

 **Examples:** 

```
Input: n = 3, m = 5
Output:
  *
 ** 
  *
Explanation: It's a hollow rectangle with 3 rows and 5 columns.
```

```
Input: n = 4, m = 3
Output:
***
 ** 
 **   
***
Explanation: It's a hollow rectangle with 4 rows and 3 columns.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T12:57:22.545Z  

```py
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
                
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/hollow-rectangle-or-square/1)