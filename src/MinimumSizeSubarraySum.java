// 209. Minimum Size Subarray Sum

public class MinimumSizeSubarraySum {
    public int minSubArrayLen(int target, int[] nums) {
        int minLen = -1;
        int i = 0;
        int j = 0;
        int curSum = nums[0];
        while (i <= j) {
            if ((j + 1 - i < minLen || minLen < 0) && curSum >= target) {
                minLen = j + 1 - i;
            }

            if (curSum > target) {
                curSum -= nums[i];
                i++;
            }
            else { // if (curSum < target)
                j++;
                if (j < nums.length) {
                    curSum += nums[j];
                } else { break; }
            }
        }
        return Math.max(minLen, 0);
    }
}
