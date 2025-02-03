package find_missing_and_repeated_values;

import java.util.ArrayList;

public class Solution
{
    public static void main(String[] args) 
    {
        int[] aux = findMissingAndRepeatedValues(new int[][]{{9,1,7},{8,9,2},{3,4,6}});
        System.out.println(aux[0] + " " + aux[1]);

        aux = findMissingAndRepeatedValues(new int[][]{{3,4},{2,2}});
        System.out.println(aux[0] + " " + aux[1]);
    }

    public static int[] findMissingAndRepeatedValues(int[][] grid) 
    {
        ArrayList<Integer> list = new ArrayList<>();

        for(int i = 0; i< grid.length; i++)
        {
            for(int j = 0; j < grid.length; j++)
            {
                list.add(grid[i][j]);
            }
        }

        list.sort(null);

        int init = list.get(0);

        int missing = 0;
        int repeated = 0;

        while(missing == 0 || repeated == 0)
        {
            if(!list.contains(init))
            {
                missing = init;
            }
            else if(list.indexOf(init) != list.lastIndexOf(init))
            {
                repeated = init;
            }

            init++;

            if(init > list.get(list.size() - 1))
            {
                break;
            }
        }

        if(missing == 0)
        {
            if(list.get(0) == 1)
            {
                missing = init;
            }
            else
            {
                missing = 1;
            }
        }

        return new int[]{repeated, missing};
    }
}
