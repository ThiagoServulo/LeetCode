package find_if_digit_game_can_be_won;

public class Solution
{
    public static boolean canAliceWin(int[] nums)
    {
        int singles = 0;
        int doubles = 0;

        for(int n: nums)
        {
            if(n <= 9)
            {
                singles += n;
            }
            else
            {
                doubles += n;
            }
        }

        return singles != doubles;
    }

    public static void main(String[] args) 
    {
        System.out.println(canAliceWin(new int[]{1,2,3,4,5,14})); // true
        System.out.println(canAliceWin(new int[]{1,2,3,4,10})); // false
    }
}
