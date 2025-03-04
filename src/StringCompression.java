// 443. String Compression

public class StringCompression {
    public int compress(char[] chars) {
        int i = 0;
        StringBuilder res = new StringBuilder();
        for (int j = 0; j < chars.length; j++) {
            if (chars[i] != chars[j]) {
                int count = j - i;
                res.append(chars[i]);
                if (count > 1) {
                    res.append(count);
                }
                i = j;
            }
        }
        res.append(chars[i]);
        if (chars.length - i > 1) {
            res.append(chars.length - i);
        }

        chars = res.toString().toCharArray();
        return chars.length;
    }
}
