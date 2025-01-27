// 69. Sqrt(x)

public class Sqrt {
    public int mySqrt(int x) {
        long root = 0;
        long square = 0;
        while (square <= x) {
            root++;
            square = root * root;
        }
        return (int)root - 1;
    }
}
