package height_checker;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution
{
    public static int heightChecker(int[] heights)
    {
        List<Integer> ordered = Arrays.stream(heights).boxed().collect(Collectors.toList());

        ordered.sort(null);

        int count = 0;

        for(int i = 0; i < ordered.size(); i++)
        {
            if(heights[i] != ordered.get(i))
            {
                ++count;
            }
        }
        return count;
    }

    public static void main(String[] args) 
    {
        System.out.println(heightChecker(new int[]{1,1,4,2,1,3}));
    }
}
