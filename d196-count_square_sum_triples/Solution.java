package count_square_sum_triples;

public class Solution
{
    public static void main(String[] args) 
    {
        System.out.println(countTriples(5)); // 2
        System.out.println(countTriples(10)); // 4
    }
    
    public static int countTriples(int n)
    {
        int array[] = new int[n];

        for(int i = 1; i <= n; i++)
        {
            array[i - 1] = i * i;
        }

        int count = 0;

        for(int i = 0; i < n; i++)
        {
            for(int j = i + 1; j < n; j++)
            {
                int aux = array[i] + array[j];

                for(int k = 0; k < n; k++)
                {
                    if(array[k] == aux)
                    {
                        count += 2;
                    }
                }
            }
        }

        return count;
    }
}
