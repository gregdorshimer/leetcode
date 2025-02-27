// 228. Summary Range

import java.util.ArrayList;
import java.util.List;

public class SummaryRanges {
    public List<String> summaryRanges(int[] nums) {
        List<String> ranges = new ArrayList<>();

        int i = 0;
        int j = 1;
        if (nums.length == 0) {
            return ranges;
        }
        while (j < nums.length) {
            if (j - i != nums[j] - nums[i]) {
                if (j - i == 1) {
                    ranges.add(Integer.toString(nums[i]));
                } else {
                    ranges.add(Integer.toString(nums[i]) + "->" + Integer.toString(nums[j - 1]));
                }
                i = j;
                j++;
            } else { j++; }
        }

        if (i + 1 < j) {
            ranges.add(nums[i] + "->" + nums[j - 1]);
        } else {
            ranges.add(Integer.toString(nums[i]));
        }

        return ranges;
    }
}
