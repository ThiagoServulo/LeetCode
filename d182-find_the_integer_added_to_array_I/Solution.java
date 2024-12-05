package find_the_integer_added_to_array_I;
import java.util.Arrays;

class Solution 
{
    public static int addedInteger(int[] nums1, int[] nums2) 
    {
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        return nums2[0] - nums1[0];
    }
    
    public static void main(String[] args) 
    {
        int[] nums1 = {2, 1, 3};
        int[] nums2 = {5, 6, 4};

        System.out.println(addedInteger(nums1, nums2));
    }
}