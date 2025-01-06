package calculate_money_in_leetcode_bank;

public class Solution
{
    public static int totalMoney(int n)
    {
        int aux = 0;
        int res = 0;

        for(int i = 1; i <= n; i++)
        {
            res += (i - (7 * aux)) + aux;

            if(i % 7 == 0)
            {
                aux += 1;
            }           
        }

        return res;
    }

    public static void main(String[] args) 
    {
        System.out.println(totalMoney(10)); // 37
        System.out.println(totalMoney(20)); // 96
    }
}
