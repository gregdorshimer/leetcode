// 27. Remove Element

public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int j = nums.length - 1;
        while (i <= j) {
            while (i < nums.length && nums[i] != val) {
                i++;
            }
            while (j >= 0 && nums[j] == val) {
                j--;
            }
            if (i < j) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        return i;
    }
}
