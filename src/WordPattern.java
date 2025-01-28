import java.util.HashMap;

public class WordPattern {
    public boolean wordPattern(String pattern, String s) {
        HashMap<String, String> myMap = new HashMap<>();
        String[] words = s.split(" ");
        String[] chars = pattern.split("");
        if (words.length != chars.length) {
            return false;
        }
        for (int i = 0; i < words.length; i++) {
            String existingValue = myMap.getOrDefault(chars[i], "");
            boolean containsWord = myMap.containsValue(words[i]);
            // 1. neither key no val is already seen, so put them in
            if (existingValue.isEmpty() && !containsWord) {
                myMap.put(chars[i], words[i]);
            }
            // 2. key is seen with a different value, so return false
            else if (!existingValue.equals(words[i])) {
                return false;
            }
            // 3. value is seen with a different key, so return false
            // -->same check as 2.
            // 4. key and value were both seen together, continue in loop
            // -->do nothing
        }
        return true;
    }
}
