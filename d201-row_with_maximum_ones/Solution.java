package row_with_maximum_ones;

public class Solution
{
    public static void main(String[] args) 
    {
        int[] res = rowAndMaximumOnes(new int[][]{{0, 0, 0}, {0, 1, 1}});

        System.out.println("Row: " + res[0] + " Maximum number of 1s: " + res[1]);
    }

    public static int[] rowAndMaximumOnes(int[][] mat)
    {
        int max = -1;
        int ret[] = new int[2];
        for(int i = 0; i < mat.length; i++)
        {
            int count = 0;
            for(int j = 0; j < mat[i].length; j++)
            {
                if(mat[i][j] == 1)
                {
                    count += 1;
                }
            }

            if(count > max)
            {
                max = count;
                ret[0] = i;
                ret[1] = count;
            }
        }

        return ret;
    }
}
