# solid-rectangle

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T14:30:48.360Z  

```py
class GFG {
    static void printSolidRectangle(int n, int m)
    {
        // Iterate through each row.
        for (int i = 1; i <= n; i++) {

            // Print m stars in the current row.
            for (int j = 1; j <= m; j++) {
                System.out.print("* ");
            }

            // Move to the next line after printing each
            // row.
            System.out.println();
        }
    }

    public static void main(String[] args)
    {
        int n = 3, m = 5;
        printSolidRectangle(n, m);
    }
}
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/solid-rectangle/1)