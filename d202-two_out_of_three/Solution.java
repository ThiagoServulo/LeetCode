package two_out_of_three;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution
{
    public static void main(String[] args) 
    {
        int[] nums1 = {1, 1, 3, 2};
        int[] nums2 = {2, 3};
        int[] nums3 = {3};
        List<Integer> aux = new ArrayList<>();
        aux = twoOutOfThree(nums1, nums2, nums3);

        for(int n: aux)
        {
            System.out.println(n);
        }
    }

    public static int contains(int[] nums, int n)
    {
        for(int i = 0; i < nums.length; i++)
        {
            if(nums[i] == n)
            {
                return 1;
            }
        }

        return 0;
    }

    public static List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3)
    {
        Set<Integer> set1 = new HashSet<>();
        List<Integer> result = new ArrayList<>();

        for(int n: nums1)
        {
            set1.add(n);
        }

        for(int n: nums2)
        {
            set1.add(n);
        }

        for(int n: nums3)
        {
            set1.add(n);
        }

        for(int n: set1)
        {
            int aux = contains(nums1, n) + contains(nums2, n) + contains(nums3, n);
            if(aux == 3)
            {
                result.add(0, n);
            }
            else if (aux == 2)
            {
                result.add(n);
            }
        }

        return result;
    }
}
