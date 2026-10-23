# Floyd's Triangle

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **n**, print Floyd's triangle with n lines.

Floyd’s Triangle is a pattern of consecutive natural numbers arranged in rows, where the i-th row contains i numbers.

 **Examples:** 

```
Input: n = 4
Output:
1
2 3
4 5 6
7 8 9 10
Explanation: The triangle has 4 rows. Numbers start from 1 and increase sequentially across rows, and each row i contains i elements.
```

```
Input: n = 5 
Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
Explanation: The triangle has 4 rows, and each row i contains i numbers.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T13:19:38.412Z  

```py
class Solution:
    def printFloydTriangle(self, n):
        # code here
        num=1
        for i in range (1,n+1):
            for j in range (i):
                print(num,end=" ")
                num+=1
            print()
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/floyds-triangle1222/1)