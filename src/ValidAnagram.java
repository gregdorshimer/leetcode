// 242. Valid Anagram

import java.util.HashMap;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> chars = new HashMap<>();
        for (String u : s.split("")) {
            chars.put(u, chars.getOrDefault(u, 0) + 1);
        }
        for (String v : t.split("")) {
            int count = chars.getOrDefault(v, 0);
            if (count == 0) {
                return false;
            } else if (count == 1) {
                chars.remove(v);
            } else {
                chars.put(v, count - 1);
            }
        }
        return chars.keySet().isEmpty();
    }
}
