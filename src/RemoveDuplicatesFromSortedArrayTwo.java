// 80 Remove Duplicates from Sorted Array II

public class RemoveDuplicatesFromSortedArrayTwo {
    public int removeDuplicates(int[] nums) {
        int k = 0;

        for (int num : nums) {
            if (k < 2 || num != nums[k]) {
                nums[k] = num;
                k++;
            }
        }

        return k;
    }
}