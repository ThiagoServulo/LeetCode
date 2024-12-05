package minimum_operations_to_make_the_array_increasing;
public class Solution 
{
    public static int minOperations(int[] nums)
    {
        int res = 0 ;
        for(int i = 1; i < nums.length; i++)
        {
            if(nums[i] <= nums[i - 1])
            {
                int aux = (nums[i - 1] - nums[i] + 1);
                res += aux;
                nums[i] = aux + nums[i];
            }
        }

        return res;
    }
    
    public static void main(String[] args) 
    {
        int[] nums1 = {1,5,2,4,1};

        System.out.println(minOperations(nums1));
    }
}
