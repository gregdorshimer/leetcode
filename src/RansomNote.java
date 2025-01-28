// 383. Ransom Note

import java.util.HashMap;

public class RansomNote {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<String, Integer> magazineChars = new HashMap<>();
        for (String s : magazine.split("")) {
            magazineChars.put(s, magazineChars.getOrDefault(s, 0) + 1);
        }
        for (String t : ransomNote.split("")) {
            int count = magazineChars.getOrDefault(t, 0);
            if (count == 0) {
                return false;
            } else if (count == 1) {
                magazineChars.remove(t);
            } else {
                magazineChars.put(t, count - 1);
            }
        }
        return true;
    }
}
