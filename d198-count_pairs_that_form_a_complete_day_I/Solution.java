package count_pairs_that_form_a_complete_day_I;

public class Solution
{
    public static void main(String[] args) 
    {
        Solution solution = new Solution();
        int[] hours = {12,12,30,24,24};
        System.out.println(solution.countCompleteDayPairs(hours));
    }

    public int countCompleteDayPairs(int[] hours)
    {
        int count = 0;

        for(int init = 0; init < hours.length; init++)
        {
            for(int end = init + 1; end < hours.length; end++)
            {
                if(((hours[init] + hours[end]) % 24) == 0)
                {
                    count++;
                }
            }
        }

        return count;
    }
}
