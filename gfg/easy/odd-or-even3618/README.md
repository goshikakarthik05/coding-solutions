# Odd or Even

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer  **n**, find if it is odd or even. Return true if the number is even else false.

 **Examples:** 

```
Input: n = 15
Output: false
Explanation: The number is not divisible by 2, Odd number.
```

```
Input: n = 44
Output: true
Explanation: The number is divisible by 2, Even number.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T11:47:29.016Z  

```py
class Solution:
    def isEven (self, n):
        # code here 
        return(n&1)==0
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/odd-or-even3618/1)