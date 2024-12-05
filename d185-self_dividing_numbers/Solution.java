package self_dividing_numbers;

import java.util.ArrayList;
import java.util.List;

public class Solution
{
    public static List<Integer> selfDividingNumbers(int left, int right)
    {
        List<Integer> res = new ArrayList<Integer>();
        
        for(int i = left; i <= right; i++)
        {
            int aux = i;
            boolean insert = true;

            do
            {
                int num = (aux % 10);
                if(num == 0 || i % num != 0)
                {
                    insert = false;
                    break;
                }

                aux  = (int)(aux / 10);
            } while(aux > 0);

            if(insert)
            {
                res.add(i);
            }
        }

        return res;
    }

    public static void main(String[] args) 
    {
        List<Integer> res = new ArrayList<Integer>();
        res = selfDividingNumbers(1, 22);

        for(int i : res)
        {
            System.out.println(i);
        }
    }
}
