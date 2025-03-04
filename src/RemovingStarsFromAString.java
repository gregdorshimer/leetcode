// 2390. Removing Stars from a String

import java.util.Stack;

public class RemovingStarsFromAString {
    public String removeStars(String s) {
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (!s.substring(i, i+1).equals("*")) {
                stack.push(s.substring(i, i+1));
            } else {
                stack.pop();
            }
        }
        StringBuilder myResult = new StringBuilder();
        while (!stack.isEmpty()) {
            myResult.insert(0, stack.pop());
        }
        s = myResult.toString();
        return s;
    }
}
