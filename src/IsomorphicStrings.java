// 205. Isomorphic Strings

import java.util.HashMap;

public class IsomorphicStrings {
    public boolean isIsomorphic(String s, String t) {
        HashMap<String, String> sMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            String sChar = s.substring(i, i+1);
            String tChar = t.substring(i, i+1);

            String mappedChar = sMap.getOrDefault(sChar, null);
            boolean containsT = sMap.containsValue(tChar);

            if (mappedChar == null) {
                if (containsT) {
                    return false;
                } else {
                    sMap.put(sChar, tChar);
                }
            } else {
                if (!mappedChar.equals(tChar)) {
                    return false;
                }
            }
        }
        return true;
    }
}
