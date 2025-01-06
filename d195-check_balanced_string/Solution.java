package check_balanced_string;

class Solution 
{  
    public static boolean isBalanced(String num)
    {
        int a = 0;
        int b = 0;
        for(int i = 0; i < num.length(); i++)
        {
            if(i % 2 == 0)
            {
                a += (num.charAt(i) - '0');
            }
            else
            {
                b += (num.charAt(i) - '0');
            }
        }

        return a == b;
    }

    public static void main(String[] args) 
    {
        System.out.println(isBalanced("123456"));
    }
}