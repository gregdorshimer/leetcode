// 202. Happy Number

import java.util.HashSet;

public class HappyNumber {
    public boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<Integer>();
        while (!seen.contains(n)) {
            seen.add(n);
            n = mySum(n);
            if (n == 1) {
                return true;
            }
        }
        return false;
    }

    static int mySum(int n) {
        String[] myChars = Integer.toString(n).split("");
        int mySum = 0;
        for (String myChar : myChars) {
            int myDigit = Integer.parseInt(myChar);
            mySum += myDigit * myDigit;
        }
        return mySum;
    }
}
