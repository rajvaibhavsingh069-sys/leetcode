class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int cursum = 0;

            for (int j = i; j < n; j++) {
                cursum += nums[j];

                if (cursum == k) {
                    count++;
                }
            }
        }

        return count;
    }
}