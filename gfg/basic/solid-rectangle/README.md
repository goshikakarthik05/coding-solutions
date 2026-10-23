# Solid Rectangle

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two integers  **n**  and  **m**, print a solid rectangle pattern of n rows and m columns using the "  *" character.

 **Examples:** 

```
Input: n = 3, m = 5
Output:
 **   **  *
 **   **  *
 **   **  *
Explanation: A solid rectangle with 3 rows and 5 columns.
```

```
Input: n = 4, m = 2
Output:
 ** 
 ** 
 ** 
 ** 
Explanation: A solid rectangle with 4 rows and 2 columns.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T14:26:47.818Z  

```py
class Solution:
    def printSolidRectangle(self, n, m):
        # code here
        for i in range(n):
           for j in range (m):
                print("*",end=" ")
           print()
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/solid-rectangle/1)