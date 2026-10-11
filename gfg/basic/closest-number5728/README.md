# Closest to n and Divisible by m

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two integers  **n**  and  **m** (m != 0). The problem is to find the number closest to  **n**  and divisible by  **m**. If there is more than one such number, then output the one having the maximum absolute value.

 **Examples :** 

```
Input: n = 13, m = 4
Output: 12
Explanation: 12 is the Closest Number to 13 which is divisible by 4.
```

```
Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15 and divisible by 6, but -18 has the maximum absolute value. So, output is -18.
```

 **Constraints:** 
-105 ≤ n, m ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T12:36:40.507Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/closest-number5728/1)