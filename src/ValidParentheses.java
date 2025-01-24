// 20. Valid Parentheses

import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<String>();
        for (int i = 0; i < s.length(); i++) {
            String myChar = s.substring(i, i+1);
            if ((myChar.equals("(") || myChar.equals("[")) || myChar.equals("{")) {
                stack.push(myChar);
            }
            else if (stack.empty()) {
                return false;
            }
            else {
                String stackChar = stack.pop();
                if (!(myChar.equals(")") && stackChar.equals("(")) &&
                        !(myChar.equals("]") && stackChar.equals("[")) &&
                        !(myChar.equals("}") && stackChar.equals("{"))) {
                    return false;
                }
            }
        }
        return stack.empty();
    }
}
