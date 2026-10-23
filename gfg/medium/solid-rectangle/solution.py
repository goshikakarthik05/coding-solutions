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