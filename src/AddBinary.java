// 67. Add Binary

import static java.lang.Math.*;

public class AddBinary {
    public String addBinary(String a, String b) {
        Integer carryBit = 0;
        StringBuilder result = new StringBuilder();

        StringBuilder myA = new StringBuilder(a);
        StringBuilder myB = new StringBuilder(b);

        if (a.length() < b.length()) {
            myA.insert(0, "0".repeat(abs(a.length() - b.length())));
        } else if (a.length() > b.length()) {
            myB.insert(0, "0".repeat(abs(a.length() - b.length())));
        }

        for (int i = myA.length() - 1; i >= 0; i--) {
            if (Integer.parseInt(myA.substring(i, i+1)) + Integer.parseInt(myB.substring(i, i+1)) + carryBit == 3) {
                result.insert(0, "1");
            } else if (Integer.parseInt(myA.substring(i, i+1)) + Integer.parseInt(myB.substring(i, i+1)) + carryBit == 2) {
                result.insert(0, "0");
                carryBit = 1;
            } else if (Integer.parseInt(myA.substring(i, i+1)) + Integer.parseInt(myB.substring(i, i+1)) + carryBit == 1) {
                result.insert(0, "1");
                carryBit = 0;
            } else { // = 0
                result.insert(0, "0");
                carryBit = 0;
            }
        }
        if (carryBit == 1) {
            result.insert(0, "1");
        }
        return result.toString();
    }
}
