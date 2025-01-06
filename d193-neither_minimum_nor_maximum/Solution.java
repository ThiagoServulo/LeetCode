package neither_minimum_nor_maximum;

import java.util.Arrays;

public class Solution
{
    public static int findNonMinOrMax(int[] nums)
    {
        if(nums.length <= 2)
        {
            return -1;
        }
        Arrays.sort(nums);
        return nums[1];
    }

    public static void main(String[] args) 
    {
        int[] nums = {3,2,1,4};
        System.out.println(findNonMinOrMax(nums)); // 2
    }
}
