// 5. Jump Game

public class JumpGame {
    public boolean canJump(int[] nums) {
        int i = nums.length - 2;
        int j = nums.length - 1;
        // i is the current index
        // j is the left-most index that we know can reach the end of the array

        while (i >= 0) {
            if (nums[i] >= j - i) {
                j = i;
                i--;
            }
        }
        return j == 0;
    }
}
